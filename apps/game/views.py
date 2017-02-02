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
    return render(request, 'game/megaadd.html', context)


def add_monster(request):
    if request.method=="POST":
        Monsters.objects.add_monster(request.POST)
    return redirect('/game')


def delete_monster(request):
    if request.method=="POST":
        Monsters.objects.add_monster(request.POST)
    return redirect('/game')


def room_monster(request):
    monsterse = Monsters.objects.exclude(rooms__id=request.POST['room_id'])
    print monsterse
    context = {
    'room': Rooms.objects.get(id=request.POST['room_id']),
    'monsters': Monsters.objects.all(),
    'monsterse': monsterse
    }
    return render(request, 'game/add_monster.html', context)


def assign_monster(request):
    if request.method=="POST":
        room=Rooms.objects.get(id=request.POST['room'])
        monsterin=Monsters.objects.get(id=request.POST['monster'])
        room.monster.add(monsterin)

    return redirect('/game')


def assign_trap(request):
    if request.method=="POST":
        room=Rooms.objects.get(id=request.POST['room'])
        trap=Traps.objects.get(id=request.POST['trap'])
        room.objects.add(trap=trap)
    return redirect('/game')


def assign_treasure(request):
    if request.method=="POST":
        room=Rooms.objects.get(id=request.POST['room'])
        treasure=Treasures.objects.get(id=request.POST['treasure'])
        room.objects.add(treasure=treasure)
    return redirect('/game')


def room_visitor(request):
    characterse = Characters.objects.exclude(populating=request.POST['room_id'])
    print characterse
    context = {
    'room': Rooms.objects.get(id=request.POST['room_id']),
    'characters': Characters.objects.all(),
    'characterse': characterse
    }
    return render(request, 'game/currently_in.html', context)


def assign_visitor(request):
    if request.method=="POST":
        room=Rooms.objects.get(id=request.POST['room'])
        character=Characters.objects.get(id=request.POST['character'])
        room.currently_in.add(character)
    return redirect('/game')


def room_explorer(request):
    characterse = Characters.objects.exclude(explored=request.POST['room_id'])
    print characterse
    context = {
    'room': Rooms.objects.get(id=request.POST['room_id']),
    'characters': Characters.objects.all(),
    'characterse': characterse
    }
    return render(request, 'game/explored_by.html', context)


def assign_explorer(request):
    if request.method=="POST":
        room=Rooms.objects.get(id=request.POST['room'])
        character=Characters.objects.get(id=request.POST['character'])
        room.explored_by.add(character)
    return redirect('/game')

def add_item(request):
    if request.method=="POST":
        print request.POST['consumeable']
        Items.objects.add_item(request.POST)
    return redirect('/game')


def delete_item(request):
    if request.method=="POST":
        print request.POST['consumeable']
        Items.objects.add_item(request.POST)
    return redirect('/game')


def add_treasure(request):
    if request.method=="POST":
        Treasures.objects.add_treasure(request.POST)
    return redirect('/game')


def delete_treasure(request):
    if request.method=="POST":
        Treasures.objects.add_treasure(request.POST)
    return redirect('/game')


def add_room(request):
    if request.method=="POST":
        Rooms.objects.add_room(request.POST)
    return redirect('/game')


def delete_room(request):
    if request.method=="POST":
        Rooms.objects.add_room(request.POST)
    return redirect('/game')


def add_trap(request):
    if request.method=="POST":
        Traps.objects.add_trap(request.POST)
    return redirect('/game')


def delete_trap(request):
    if request.method=="POST":
        Traps.objects.add_trap(request.POST)
    return redirect('/game')
