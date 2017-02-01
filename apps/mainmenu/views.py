from django.shortcuts import render

def index(request):
    return render(request, 'login/base.html')

def create(request):
    return render(request, 'login/base.html')

def delete(request):
    return render(request, 'login/base.html')

def hall(request):
    return render(request, 'login/base.html')
