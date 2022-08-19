from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

def badlogin(request):
    return render(request, 'bad_login.html')

def logout(request):
    auth.logout(request)
    return redirect('main')

def join(request):
    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('confirmpwd'):
            user = User.objects.create(username = request.POST['name'], password = request.POST['password'])
            auth.login(request,user)
            return redirect('login')
    return render(request, 'join.html')

   