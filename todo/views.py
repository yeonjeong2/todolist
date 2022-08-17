from django.shortcuts import render
from django.shortcuts import redirect
from .forms import Writingform
from .models import Writing
from django.views.decorators.csrf import csrf_exempt

def main(request):
    return render(request, 'main.html')

def writingcreate(request):
    if (request.method == "POST"):
        post = Writing()
        post.content = request.POST['content']
        post.save()
    return redirect('main')