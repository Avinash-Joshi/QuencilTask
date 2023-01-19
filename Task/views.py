from django.http import HttpResponse
from django.shortcuts import render

# import sys
# sys.path.append("E:\Quncil_Task\Task\signin\models.py")

from signin import models


def signup(request):
    return render(request, 'signup.html')


def home(request):
    db = models.data.objects.all()
    print(db)
    length = len(db)
    print(length)
    inner = models.data.objects.values('emailid').all()
    print(inner)
    if (request.method == 'POST'):
        name = request.POST.get('Name', 'default')
        username = request.POST.get('Username', 'default')
        emailid = request.POST.get('Email', 'default').upper()
        dob = request.POST.get('DOB', 'default')
        password = request.POST.get('Password', 'default')
        print("I am Avinash joshi")
        print(name)
        print(username)
        print(emailid)
        print(dob)
        print(password)
        if (name != '' and emailid != '' and password != '' and dob != '' and username != ''):
            for i in range(length):
                if (emailid == inner[i]['emailid'].upper()):
                    return render(request, 'fail.html')
            user = models.data(name=name, username=username,emailid=emailid, dob=dob, password=password)
            user.save()
            return render(request, 'home.html')
        return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')


def home1(request):
    db = models.data.objects.all()
    print(db)
    length = len(db)
    print(length)
    inner = models.data.objects.values('emailid','password').all()
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
            return render(request,'failure.html')
    return render(request, 'signin.html')