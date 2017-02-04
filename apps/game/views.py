from django.shortcuts import render, redirect
from django.contrib import messages
from models import Users, Characters, Monsters, Rooms, Items, Traps, Treasures, Exits
from django.template import Context
from random import randint
import string

def index(request):
    return render(request, 'game/game.html')


def calculate_stats(request, character):
    return_to_view=Characters.objects.calculate_stats(character)
    return return_to_view


def main(request):
    # request.session['character_id']="2"
    hero=Characters.objects.get(id=request.session['character_id'])
    stats=calculate_stats(request, hero)
    request.session['room_id']=Rooms.objects.get(currently_in__id=hero.id).id
    hero=request.session['character_id']
    room=request.session['room_id']

    context = {
    # 'users': Users.objects.filter(id=request.session['']).order_by('username'),
        'location': Rooms.objects.get(id=room),
        'hero': Characters.objects.get(id=hero),
        'characters': Characters.objects.filter(populating__id=room).exclude(killed_by__isnull=True).order_by('name').exclude(id=hero),
        'corpses': Characters.objects.filter(populating__id=room).exclude(killed_by__isnull=False).order_by('name'),
        'monsters': Monsters.objects.filter(denizen__id=room).order_by('name').exclude(killed_by__id=hero),
        'monsters_dead': Monsters.objects.filter(denizen__id=room).order_by('name').filter(killed_by__id=hero),
        'peeks': Exits.objects.filter(leads_to__id=room),
        'items': Items.objects.filter(owned_by__id=hero).order_by('name'),
        'traps': Traps.objects.filter(dangers__id=room).order_by('name'),
        'treasures': Treasures.objects.filter(reward__id=room).order_by('name'),
        'exits': Exits.objects.filter(leads_to__id=room),
        'rooms': Rooms.objects.all(),
        'stats': stats,
        }
    return render(request, 'game/main.html', context)


def start_combat(request):
    hero=Characters.objects.get(id=request.session['character_id']),
    room=Rooms.objects.get(id=request.session['room_id']),
    monsters=Monster.ojbects.filter(Monsters__populating_id=request.session['room_id'].exclude(killed_by__id=hero.id))
    combat = Combat.objects.add_combat(hero, room, monsters);
    print combat
    context = {
        'combat': combat
    }
    return render(request, 'game/combat.html, session')


def combat_round(request):
    pass
    # TODO combat round logic

def victory(request):
    pass
    # TODO win result

def defeat(request):
    pass
    # TODO win result

def engage_trap(request):
    pass
    # TODO trap page

def reward(request):
    pass
    # TODO get Treasure

def equip_item(request):
    pass
    # TODO equip item

def death(request):
    pass
    # TODO character death

def flee(request):
    pass
    # TODO run away!!!

def explored(request):
    pass
    # TODO explored room.

def start_game(request):
    if request.method == "POST":
        request.session['character_id'] = request.POST['character']
        if len(Rooms.objects.filter(currently_in__id=request.session['character_id']))==0:
            character=Characters.objects.get(id=request.session['character_id'])
            room=Rooms.objects.get(id=2)
            room.currently_in.add(character)
        return redirect("/game/")
    return redirect("/mainmenu/select_character")


def move(request):
    if request.method == "POST":
        hero=Characters.objects.get(id=request.session['character_id'])
        room=Rooms.objects.get(id=request.POST['room'])
        destination = Rooms.objects.get(id=request.POST['destination'])
        response_from_models=Characters.objects.move(hero, room, destination)
        if not response_from_models['status']:
            for errors in response_from_models['errors']:
                messages.error(request, errors)
    return redirect('/game/main')
