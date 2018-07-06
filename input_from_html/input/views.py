from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",{})

def disp(request):
    request.method == 'POST'
    name = request.POST.get('name', None)
    print("Name",name)

    return render(request,"disp.html",{'name':name})
