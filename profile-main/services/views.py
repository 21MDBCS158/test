from django.shortcuts import render

# Create your views here.

def services_pro(request):
    return render(request, 'serve/serve.html',{'p': "Services"})