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
    'exits': Exits.objects.all().order_by('entrances'),
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


def assign_monster(request):
    if request.method=="POST":
        room=Room.objects.get(id=request.post['room'])
        monster=Monsters.objects.get(id=request.post['monster'])
        room.objects.create(monster=monster)
    return redirect('/game')


def assign_trap(request):
    if request.method=="POST":
        room=Room.objects.get(id=request.post['room'])
        trap=Traps.objects.get(id=request.post['trap'])
        room.objects.create(trap=trap)
    return redirect('/game')


def assign_treasure(request):
    if request.method=="POST":
        room=Room.objects.get(id=request.post['room'])
        treasure=Treasures.objects.get(id=request.post['treasure'])
        room.objects.create(treasure=treasure)
    return redirect('/game')

def assign_visitor(request):
    if request.method=="POST":
        room=Room.objects.get(id=request.post['room'])
        character=Characters.objects.get(id=request.post['character'])
        room.objects.create(currently_in=character)
    return redirect('/game')

def assign_explorer(request):
    if request.method=="POST":
        room=Room.objects.get(id=request.post['room'])
        character=Characters.objects.get(id=request.post['character'])
        room.objects.create(explored_by=character)
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
        Treasure.objects.add_treasure(request.POST)
    return redirect('/game')


def delete_treasure(request):
    if request.method=="POST":
        Treasure.objects.add_treasure(request.POST)
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

<<<<<<< HEAD
=======

def delete_trap(request):
    if request.method=="POST":
        Traps.objects.add_trap(request.POST)
    return redirect('/game')
>>>>>>> a5f15dad8d6562825ba5434e696c13e209993415
