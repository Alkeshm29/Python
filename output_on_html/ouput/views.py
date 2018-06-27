from django.shortcuts import render

# Create your views here.

def home(request):
    a="alk"
    return render(request,"home.html", {'b':a})

