from django.shortcuts import render, redirect
from .forms import contactForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def contact_page(request):
    if request.method == "POST":
       form = contactForm(request.POST)
       if form.is_valid():
           form.sendMessage()
           return redirect("contact_success")
    else:
        form = contactForm()

    context = {"form": form}
    return render(request, "contact.html", context)

def contactSucess_page(request):
    return render(request, "contactSuccess.html")
    
    

