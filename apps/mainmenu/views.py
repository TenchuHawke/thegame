from django.shortcuts import render, redirect
from random import randint
import random
from django.core.urlresolvers import reverse
# from .models import Users

def index(request):
    return render(request, 'mainmenu/index.html')

def create(request):
	adderror=Users.objects.check_user(request)
	if not adderror ==[]:
		for error in adderror:
			messages.info(request, error)
		return redirect(reverse('Mainmenu:create'))
	else:
		return redirect('/game/')
	return render(redirect('Mainmenu:create'))

def delete(request):
    return render(request, 'login/base.html')

def hall(request):
    return render(request, 'login/base.html')

def update(request):
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
	context = {
			'str': random.randrange(1,10),
			'dex': random.randrange(1,10),
			'int': random.randrange(1,10),
			'hea': random.randrange(1,10),
			}
	
	print context
	return render(request, 'mainmenu/newchar.html', context)














