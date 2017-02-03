from django.shortcuts import render, redirect
from django.contrib import messages
from models import Users, Characters, Monsters, Rooms, Items, Traps, Treasures, Exits
from django.template import Context
from random import randint


def index(request):
    return render(request, 'game/game.html')

def main(request):
    request.session['character_id']="3"
    request.session['room_id']="2"
    hero=request.session['character_id']
    room=request.session['room_id']
    context = {
    # 'users': Users.objects.filter(id=request.session['']).order_by('username'),
        'location': Rooms.objects.get(id=room),
        'hero': Characters.objects.get(id=hero),
        'characters': Characters.objects.filter(populating__id=room).order_by('name'),
        'characters': Characters.objects.filter(populating__id=room).filter(notkilled_by__=None).order_by('name'),
        'monsters': Monsters.objects.filter(denizen__id=room).order_by('name').exclude(killed_by__id=hero),
        'monsters_dead': Monsters.objects.filter(denizen__id=room).order_by('name').filter(killed_by__id=hero),
        'peeks': Rooms.objects.filter(exits__comes_from__id=room).order_by('direction'),
        'items': Items.objects.filter(owned_by__id=hero).order_by('name'),
        'traps': Traps.objects.filter(dangers__id=room).order_by('name'),
        'treasures': Treasures.objects.filter(reward__id=room).order_by('name'),
        'exits': Exits.objects.filter(leads_to__id=room),
        'exits': Exits.objects.filter(leads_to__id=room),
        'rooms': Rooms.objects.all(),
        }
    return render(request, 'game/main.html', context)

def start_combat(request):
    hero=Characters.objects.get(id=request.session['character_id']),
    room=Rooms.objects.get(id=request.session['room_id']),
    monsters=Monster.ojbects.filter(Monsters__populating_id=request.session['room_id'])
    combat = Combat.objects.add_combat(hero, room, monsters);
    print combat
    context = {
        'combat': combat
    }
    return render(request, 'game/combat.html, session')
