from django.shortcuts import render

# Create your views here.
def contact_pro(request):
    context = {"home": "active"}
    return render(request,'cont/contact.html'  ,{'p': 'Contacts'},   )