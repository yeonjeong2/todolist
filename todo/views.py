from django.shortcuts import render
from django.shortcuts import redirect
from .forms import Writingform
from .models import Writing
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User

def main(request):
    user = request.user
    # 입력받은 글들을 main에 띄우는 코드
    posts = Writing.objects.filter(user = request.user.id)
    return render(request, 'main.html',{'user':user,'posts':posts})

def writingcreate(request):
    if request.method == "POST":
        user = request.user
        content = request.POST.get('content')
        userpost = Writingform({
            "user":user,
            "content":content
        })
        if userpost.is_valid():
            userpost.save()
            return redirect('main')
    else:
        userpost = Writingform()
    return render(request, 'main.html')

