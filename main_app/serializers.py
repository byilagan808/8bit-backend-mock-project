from rest_framework import serializers 
from .models import  *

class MiscImageSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = MiscImage 
        fields = '__all__'

class TvShowSerializer(serializers.ModelSerializer):
    images = MiscImageSerializer(many=True) 
    class Meta: 
        model = TvShow
        fields = ['name','short_description','images']
