from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world, this is the beginning of my bandish.studio project!')
