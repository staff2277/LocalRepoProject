from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("contact/", views.contact_page, name="contact"),
    path("contact_success/", views.contactSucess_page, name="contactSucess_page"),
]
