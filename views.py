from django.shortcuts import render, redirect
from .models import ClientRegister_Model

def login(request):
    return render(request, 'RUser/login.html')


def Register1(request):
    if request.method == "POST":
        ClientRegister_Model.objects.create(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            phoneno=request.POST.get('phoneno'),
            country=request.POST.get('country'),
            state=request.POST.get('state'),
            city=request.POST.get('city'),
            address=request.POST.get('address'),
            gender=request.POST.get('gender'),
        )
        return redirect('login')

    return render(request, 'RUser/Register1.html')
