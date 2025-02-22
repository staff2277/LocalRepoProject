from django.shortcuts import render
from .models import Africatour

# Create your views here.
tours = Africatour.objects.all()
context = {"tours": tours}

def index(request):
    return render(request, "index.html", context)