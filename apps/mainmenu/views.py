from django.shortcuts import render, redirect
from django.contrib import messages
from random import randint
import random
from django.core.urlresolvers import reverse
from .models import Characters
from ..login.models import Users


def index(request):
    return render(request, 'mainmenu/index.html')


def showcreate(request):
	return render(request, 'mainmenu/newchar.html')


def create(request):
	if request.method=='POST':
		user = Users.objects.get(id=request.session['user_id'])
		response_from_models=Characters.objects.add_char(request.POST, user)
		if not response_from_models['status']:
			for error in response_from_models['errors']:
				messages.info(request, error)
			return redirect(reverse('Mainmenu:show'))
		else:
			return redirect('/game')
	return redirect(reverse('Mainmenu:show'))

def delete(request):
    return render(request, 'login/base.html')

def admin_menu(request):
	return render(request, 'gameadmin/adminmenu.html')

def hall(request):
    return render(request, 'mainmenu/hall.html')

def update(request):
	# Not being used right now
	if request.method=="POST":
		if request.POST['fighter']=="Fighter":
			request.session['fighter']="Fighter"
			context = {
			'str': random.randint(1,10),
			'dex': random.randint(1,10),
			'int': random.randint(1,10),
			'hea': random.randint(1,10),
			'name': request.POST['char_name']
			}
			return redirect(reverse('Mainmenu:create'), context)
		if request.POST['rogue']=="Rogue":
			request.session['rogue']="Rogue"
			context = {
			'str': random.randint(1,10),
			'dex': random.randint(1,10),
			'int': random.randint(1,10),
			'hea': random.randint(1,10),
			'name': request.POST['char_name']
			}
			return redirect(reverse('Mainmenu:create'), context)
		if request.POST['wizard']=="Wizard":
			request.session['wizard']="Wizard"
			context = {
			'str': random.randint(1,10),
			'dex': random.randint(1,10),
			'int': random.randint(1,10),
			'hea': random.randint(1,10),
			'name': request.POST['char_name']
			}
			return redirect(reverse('Mainmenu:create'), context)
	else:
		return redirect(reverse('Mainmenu:create'))
def roll(request):
	strength= (random.randrange(1,5) + random.randrange(1,5) + random.randrange(1,5))
	dexterity= (random.randrange(1,5) + random.randrange(1,5) + random.randrange(1,5))
	intelligence= (random.randrange(1,5) + random.randrange(1,5) + random.randrange(1,5))
	health= (random.randrange(1,5) + random.randrange(1,5) + random.randrange(1,5))
	context = {
			'str': strength,
			'dex': dexterity,
			'int': intelligence,
			'hea': health
			}
	return render(request, 'mainmenu/newchar.html', context)
