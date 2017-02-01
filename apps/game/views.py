from django.shortcuts import render
from django.contrib import messages
from models import Users, Characters, Monsters, Rooms, Items, Traps, Treasure, Exits
from django.template import Context
from random import randint


def index(request):
    context = {
    'users': Users.objects.all(),
    'chars': Characters.objects.all(),
    'monsters': Monsters.objects.all(),
    'rooms': Rooms.objects.all(),
    'items': Items.objects.all(),
    'traps': Traps.objects.all(),
    'treasure': Treasure.objects.all(),
    'exits': Exits.objects.all(),
    }

    return render(request, 'game/megaadd.html', context)
