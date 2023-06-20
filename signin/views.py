from django.http import HttpResponse
from django.shortcuts import render
from .models import data
# from .import models

# Create your views here.


def signin(request):
    return render(request, 'signin/signin.html')


# def home(request):
#     db = data.objects.all()
#     print(db)
#     if (request.method == 'POST'):
#         emailid = request.POST.get('Email', 'default').upper()
#         password = request.POST.get('Password', 'default')
#         print(emailid)
#         print(password)
#         if(emailid!='' and password!=''):
#             print('Something wrong')
#             return render(request,'signin/fail.html')
#         return render(request,'signin/home.html')

def home(request):
    db = data.objects.all()
    print(db)
    length = len(db)
    print(length)
    inner = data.objects.values('emailid', 'password').all()
    print(inner)
    # print('Inside Hello')
    if (request.method == 'POST'):
        emailid = request.POST.get('Email', 'default').upper()
        password = request.POST.get('Password', 'default')
        print(emailid)
        print(password)
        if (emailid != '' and password != ''):
            for i in range(length):
                if (emailid == inner[i]['emailid'].upper() and password == inner[i]['password']):
                    return render(request, 'home.html')
            return render(request, 'signin/failure.html')
    print('Hello')
    return render(request, 'signin/signin.html')
