from django.shortcuts import render
from django.http  import  HttpResponse

# Create your views here.
def sandhay(request):
    return HttpResponse('<marquee>sandhy is mental girl</marquee>')