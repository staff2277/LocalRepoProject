from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("contact/",views.contactPage, name="contact"),
    path("contactSuccess/",views.contactSucess, name="contactSuccess"),
]
