from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, "home.html" )

def contactSucess(request):
    return render(request, "contactSuccess.html" )


def contactPage(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("contactSuccess")
        
    context = {"form": form}
    return render(request, "contact.html", context )

