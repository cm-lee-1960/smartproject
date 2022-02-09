from django.db.models.signals import post_save
from django.dispatch import receiver
#from .models import Restapp, Restapp2
from.models import Restapp
from .telegram import sendmessage
#from .serializers import RestappSerializer

#@receiver(post_save, sender=Restapp)
#def create_nqi(sender, instance, created, **kwargs):
def post_data(data, **kwargs):
    #print("helloworld")
    #if created == True:
    nqi = data
    print("nqi는")
    print(nqi)
    #Restapp2.objects.create(number=nqi.number, boot=nqi.boot, address=nqi.address)
    if nqi['address'] == "도봉구":
        message = nqi['address'] + nqi['phonenumber'] + nqi['boot']
        #print(nqi.phonenumber + nqi.boot + nqi.address)
        print(message)
        sendmessage(message)
#post_save.connect(create_nqi, sender=Smart)