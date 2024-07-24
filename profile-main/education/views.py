from django.shortcuts import render

# Create your views here.
def skills_pro(request):
    return render(request, 'skills/skills.html', {'p': 'Skills'})
