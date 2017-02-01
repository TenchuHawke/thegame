from django.shortcuts import render
from ..game.models import Users, Characters, Monsters, Rooms, Items, Traps, Treasure, Exits

def index(request):
    return render(request, 'login/base.html')
