from rest_framework import serializers
from .models import Restapp

class RestappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restapp
        fields = ['num','phonenumber', 'boot', 'address', 'm_rsrp', 'dl_th','ul_th']