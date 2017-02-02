from django.shortcuts import render, redirect
from django.contrib import messages
from models import Users, Characters, Monsters, Rooms, Items, Traps, Treasures, Exits
from django.template import Context
from random import randint


def index(request):
    context = {
    'users': Users.objects.all().order_by('username'),
    'characters': Characters.objects.all().order_by('name'),
    'monsters': Monsters.objects.all().order_by('name'),
    'rooms': Rooms.objects.all().order_by('id'),
    'items': Items.objects.all().order_by('name'),
    'traps': Traps.objects.all().order_by('name'),
    'treasures': Treasures.objects.all().order_by('name'),
    'exits': Exits.objects.all(),
    }
    return render(request, 'game/base.html', context)

def start_combat(request):
    request.session['character_id']="1",
    request.session['room_id']="2",
    hero=Characters.objects.get(id=request.session['character_id']),
    room=Rooms.objects.get(id=request.session['room_id']),
    monsters=Monster.ojbects.filter(Monsters__populating_id=request.session['room_id'])
    combat = Combat.objects.add_combat(hero, room, monsters);
    print combat
    context = {
        'combat': combat
    }
    return render(request, 'game/combat.html, session')
