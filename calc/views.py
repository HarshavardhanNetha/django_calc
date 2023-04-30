from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("<h1>Hello World!</h1>"
    print(request.method, "req method")
    if(request.method == "POST"):
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        return render(request, 'form.html', {"title":"Result | Calculator App", "result": num1+num2, "req":request})
    else:
        return render(request, 'form.html', {"title": "Input | Calculator App"})

def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    
    print(num1, num2)
    return render(request , 'result.html', {"res":num1+num2})