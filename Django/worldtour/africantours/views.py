from django.shortcuts import render
from .models import Afrotours

# Create your views here.
def index(request):
    tours = Afrotours.objects.all()
    context = {"tours": tours}
    return render(request, "index.html", context)
