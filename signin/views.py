from django.http import HttpResponse
from django.shortcuts import render
from .models import data

# Create your views here.
def signin(request):
    return render(request,'signin/signin.html')


def home(request):
    db = data.objects.all()
    print(db)
    if (request.method == 'POST'):
        emailid = request.POST.get('Email', 'default').upper()
        password = request.POST.get('Password', 'default')
        print(emailid)    
        print(password)
        if(emailid!='' and password!=''):
            print('Something wrong')
            return render(request,'signin/fail.html')
        return render(request,'signin/home1.html')