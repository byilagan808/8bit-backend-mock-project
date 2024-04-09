from django.shortcuts import render
from .models import *
from rest_framework.views import APIView 
from .serializers import * 
from rest_framework.response import Response
from .pagination import TvShowPagination


# Create your views here.
def index(request):
    shows = TvShow.objects.prefetch_related("images").all()

    return render(request,"index.html",{"shows":shows})

class GetTvShows(APIView): 
    def get(self, request): 
        queryset=TvShow.objects.prefetch_related("images").all() 
        serializer = TvShowSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)

class GetTvShowsPagination(APIView): 
    pagination_class = TvShowPagination 
    def get(self, request, *args, **kwargs): 
        queryset=TvShow.objects.prefetch_related("images").all() 
        paginator = self.pagination_class()
    
        page = paginator.paginate_queryset(queryset, request) 
        if page is not None: 
            serializer = TvShowSerializer(page, many=True) 
            return paginator.get_paginated_response(serializer.data) 
        serializer = TvShowSerializer(queryset, many=True) 
        return Response(serializer.data)

