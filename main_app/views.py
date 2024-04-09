from django.shortcuts import render
from .models import *
from rest_framework.views import APIView 
from .serializers import * 
from rest_framework.response import Response


# Create your views here.
def index(request):
    shows = TvShow.objects.prefetch_related("images").all()

    return render(request,"index.html",{"shows":shows})

class GetTvShows(APIView): 
    def get(self, request): 
        queryset=TvShow.objects.prefetch_related("images").all() 
        serializer = TvShowSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)

