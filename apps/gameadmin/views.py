from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import Context
from random import randint
from ..game.models import Users, Characters, Monsters, Rooms, Items, Traps, Treasures, Exits



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
    if request.method == "POST":
        Monsters.objects.add_monster(request.POST)
    return redirect('/admin')


def delete_monster(request):
    if request.method == "POST":
        Monsters.objects.add_monster(request.POST)
    return redirect('/admin')


def room_monster(request):
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'monsters': Monsters.objects.all(),
        }
    return render(request, 'game/add_monster.html', context)


def assign_monster(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        monsterin = Monsters.objects.get(id=request.POST['monster'])
        room.monster.add(monsterin)

    return redirect('/admin')

def room_killer(request):
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'traps': Traps.objects.all(),
        }
    return render(request, 'game/room_traps.html', context)

def room_trap(request):
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'traps': Traps.objects.all(),
        }
    return render(request, 'game/room_traps.html', context)


def assign_trap(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        trap = Traps.objects.get(id=request.POST['trap'])
        room.trap.add(trap)
    return redirect('/admin')


def room_treasure(request):
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'treasures': Treasures.objects.all(),
        }
    return render(request, 'game/room_treasure.html', context)


def assign_treasure(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        treasure = Treasures.objects.get(id=request.POST['treasure'])
        room.treasure.add(treasure)
    return redirect('/admin')


def room_visitor(request):
    print request.POST
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'characters': Characters.objects.all(),
        }
    return render(request, 'game/currently_in.html', context)


def assign_visitor(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        character = Characters.objects.get(id=request.POST['character'])
        room.currently_in.add(character)
    return redirect('/admin')


def room_explorer(request):
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'characters': Characters.objects.all(),
        }
    return render(request, 'game/explored_by.html', context)


def assign_explorer(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        character = Characters.objects.get(id=request.POST['character'])
        room.explored_by.add(character)
    return redirect('/admin')


def add_item(request):
    if request.method == "POST":
        Items.objects.add_item(request.POST)
    return redirect('/admin')


def delete_item(request):
    if request.method == "POST":
        Items.objects.add_item(request.POST)
    return redirect('/admin')


def add_treasure(request):
    if request.method == "POST":
        Treasures.objects.add_treasure(request.POST)
    return redirect('/admin')


def delete_treasure(request):
    if request.method == "POST":
        Treasures.objects.add_treasure(request.POST)
    return redirect('/admin')


def add_room(request):
    if request.method == "POST":
        Rooms.objects.add_room(request.POST)
    return redirect('/admin')


def delete_room(request):
    if request.method == "POST":
        Rooms.objects.add_room(request.POST)
    return redirect('/admin')


def add_trap(request):
    if request.method == "POST":
        Traps.objects.add_trap(request.POST)
    return redirect('/admin')


def delete_trap(request):
    if request.method == "POST":
        Traps.objects.add_trap(request.POST)
    return redirect('/admin')
