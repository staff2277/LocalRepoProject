from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def home_page(request):
    return render(request, "home.html")

def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.post)
        if form.is_valid:
            form.sendEmail()
            return redirect("contact_success")
    else:
        form = ContactForm()
        context = {"form": form}
        return render(request, "contact.html", context)
    
def contactSucess_page(request):
    return render(request, "contact_success.html")
