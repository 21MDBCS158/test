from django.shortcuts import render

# Create your views here.

def home_page (request):
    context =  {"home" : "active"}
    return render(request, 'core/core.html', {"p": 'Home page'})