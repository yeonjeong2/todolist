from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username = userid, password = pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('main')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
