from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Users
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name = re.compile(r'^[a-zA-Z]')


def index(request):
    return render(request, 'login/login.html')


def main(request):
    return render(request, 'login/login.html')


def login(request):
    if request.method == "POST":
        response_from_models = Users.objects.check_user(request.POST)
        # check to make sure it passed validation
        route = check_login(request, response_from_models)
        if route:
            return redirect(reverse('Mainmenu:index'))
    return redirect('/login/main')


def register(request):
    if request.method == "POST":
        response_from_models = Users.objects.add_user(request.POST)
        # check to make sure it passed validation
        route = check_login(request, response_from_models)
        if route:
            return redirect(reverse('Mainmenu:index'))
    return redirect('/login/main')


def check_login(request, response_from_views):
    if not response_from_views['status']:
        for error in response_from_views['errors']:
            messages.error(request, error)
        return False
    else:
        request.session['user_id'] = response_from_views['user'][0].id
        request.session['username'] = Users.objects.only('username').get(id=request.session['user_id']).username
        return True


def logout(request):
    request.session.clear()
    return redirect('/')
