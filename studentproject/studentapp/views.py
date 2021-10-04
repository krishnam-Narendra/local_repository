from django.shortcuts import render , redirect
from . import forms
from django.contrib.auth import authenticate, login , logout
from .models import StudentRegister , MarksDetails

# Create your views here.
def homeView(request):
    return render(request, 'studentapp/home.html',)

def registerView(request):
    form = forms.StudentRegisterForm()
    return render(request,'studentapp/register.html',{'form':form})

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user.is_valid():
            login(request,user)
            return redirect('detail')
    return render(request,'studentapp/login.html')

def logout(request):
    logout(request)
    return redirect('/')
def detailview(request):
    if request.method=="POST":

        rollno=request.POST.get('rollno')

        data=StudentRegister.objects.filter(roolno=rollno)

        return render(request, 'studentapp/home.html' ,{'rollno':rollno, 'data': data})

    return render(request, 'studentapp/home.html')






