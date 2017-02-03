from django.shortcuts import render, redirect
from django.contrib import messages
from random import randint
import random
from django.core.urlresolvers import reverse
from ..game.models import Characters, Rooms
from ..login.models import Users


def index(request):
	request.session['starting_room']="1"
	return render(request, 'mainmenu/index.html')


def showcreate(request):
	return render(request, 'mainmenu/newchar.html')


def create(request):
	if request.method=='POST':
		user = Users.objects.get(id=request.session['user_id'])
		response_from_models=Characters.objects.add_char(request.POST, user)
		if response_from_models['status']:
			hero=response_from_models["character"]
			room=Rooms.objects.get(id=request.session['starting_room'])
			room.explored_by.add(hero)
			room.currently_in.add(hero)
			request.session['character_id']=hero.id
			return redirect('/game')
		else:
			for error in response_from_models['errors']:
				messages.info(request, error)
	return redirect(reverse('Mainmenu:show'))


def delete(request):
    return render(request, 'login/base.html')


def admin_menu(request):
	return render(request, 'gameadmin/adminmenu.html')


def hall(request):
	context = {
	'characters':Characters.objects.filter(level__gt=0).order_by('-gold'),
	}
	return render(request, 'mainmenu/hall.html', context)

def update(request):
	context = {
	'characters':Characters.objects.filter(level>0).order_by('gold'),
	}
	return render(request, 'mainmenu/hall.html', context)


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


def select_character(request):
    context = {
        'characters': Characters.objects.filter(owned_by__id=request.session['user_id']).order_by('name'),
        }
    return render(request, 'mainmenu/select_character.html', context)
