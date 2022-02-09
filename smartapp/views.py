from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Restapp
from .serializers import RestappSerializer
from rest_framework.parsers import JSONParser
from .signals import post_data

# Create your views here.

@csrf_exempt
def restapp_list(request):
    if request.method == 'GET':
        query_set = Restapp.objects.all()
        serializer = RestappSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False) ## 제이슨 형식으로 리턴 
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RestappSerializer(data=data) ## 시리얼 라이저 모델이랑 비교
        if serializer.is_valid():  ## 같으면 저장
            #serializer.save()
            post_data(data)
            #print(data)
            print("성공")
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def restapp(request, pk):
    
    obj = Restapp.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = RestappSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RestappSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DEL':
        obj.delete()
        return HttpResponse(status=204)
    
# @csrf_exempt
# def login(request):
#     if request.mothod == 'POST':
#         data = JSONParser().parse(request)
#         search_number = data['number']  ## 넘버로 프라이머키]
#         obj = Restapp.objects.get(name=search_number)
        
#         if data['adress'] == obj.adress:
#             return HttpResponse(status=200)
#         else:
#             return HttpResponse(status=200)        
        
 