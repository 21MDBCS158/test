from django.urls import path
from . import views

urlpatterns = [
    path("skills/", views.skills_pro, name="skills")
]
