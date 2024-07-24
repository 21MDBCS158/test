from django.urls import path
from . import views

urlpatterns = [
    path("contacts/", views.contact_pro, name="contactus")
]
