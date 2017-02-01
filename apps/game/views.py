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

def add_item(request):
    if request.method=="POST":
        print request.POST['consumeable']
        Items.objects.add_item(request.POST)
    return redirect('/game')

def add_treasure(request):
    if request.method=="POST":
        Treasures.objects.add_treasure(request.POST)
    return redirect('/')

def add_room(request):
    if request.method=="POST":
        Rooms.objects.add_room(request.POST)
    return redirect('/')

def add_trap(request):
    if request.method=="POST":
        Traps.objects.add_trap(request.POST)
    return redirect('/')
