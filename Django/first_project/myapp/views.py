from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello World how are u all doing right now")