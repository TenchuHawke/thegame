from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Users
import re, bcrypt
EMAIL_REGEX=re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name=re.compile(r'^[a-zA-Z]')


def index(request):
    return render(request, 'login/base.html')


def loginreg(request):
	return render(request, 'login/login.html')

def login(request):
    if request.method=="POST":
        log=Users.objects.check_user(request)
        print log
        if not log ==[]:
            for error in log:
                messages.info(request, error)
            return redirect(reverse('Login:login'))
        else:
            request.session['id']=Users.objects.only('id').get(username=request.POST['username']).id
            request.session['name']=Users.objects.only('username').get(id=request.session['id']).username
            return redirect(reverse('Mainmenu:index'))


def register(request):
   errors=Users.objects.add_user(request)
   if not errors ==[]:
      for error in errors:
         messages.info(request, error)
      return redirect(reverse('Login:login'))
   else:
      return redirect(reverse('Mainmenu:index'))
   return redirect(reverse('Login:login'))

def logout(request):
	for sesskey in request.session.keys():
		del request.session[sesskey]
	return redirect(reverse('Login:index'))
