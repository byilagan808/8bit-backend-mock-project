from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    shows = TvShow.objects.prefetch_related("images").all()

    return render(request, "index.html",{"shows":shows})


