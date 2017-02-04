from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
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
    return render(request, 'gameadmin/megaadd.html', context)



# first half of assigning objects display all options for X_Y
# TODO add filters for all room_ rooms
def room_exit(request):
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'exits': Exits.objects.all(),
        'rooms': Rooms.objects.all(),
        }
    return render(request, 'gameadmin/add_entrance_exit.html', context)


def room_monster(request):
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'monsters': Monsters.objects.all(),
        }
    return render(request, 'gameadmin/add_monster.html', context)


def room_killer(request):
    context = {
        'monster': Monsters.objects.get(id=request.POST['monster_id']),
        'characters': Characters.objects.all(),
        }
    return render(request, 'gameadmin/room_killedby.html', context)

def room_trap(request):
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'traps': Traps.objects.all(),
        }
    return render(request, 'gameadmin/room_traps.html', context)

def room_treasure(request):
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'treasures': Treasures.objects.all(),
        }
    return render(request, 'gameadmin/room_treasure.html', context)

def room_visitor(request):
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'characters': Characters.objects.all(),
        }
    return render(request, 'gameadmin/currently_in.html', context)

def room_explorer(request):
    context = {
        'room': Rooms.objects.get(id=request.POST['room_id']),
        'characters': Characters.objects.all(),
        }
    return render(request, 'gameadmin/explored_by.html', context)

def character_item(request):
    context = {
        'item': Items.objects.get(id=request.POST['item_id']),
        'characters': Characters.objects.all(),
        }
    return render(request, 'gameadmin/character_item.html', context)

# ASSIGN
def assign_monster(request):
    print request.POST
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        monsterin = Monsters.objects.get(id=request.POST['monster'])
        room.monster.add(monsterin)

    return redirect(reverse ('Admin:admin_monsters'))

def assign_killer(request):
    if request.method == "POST":
        monster = Monsters.objects.get(id=request.POST['monster'])
        character = Characters.objects.get(id=request.POST['character'])
        monster.killed_by.add(character)
    return redirect(reverse ('Admin:admin_monsters'))

def assign_trap(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        trap = Traps.objects.get(id=request.POST['trap'])
        room.trap.add(trap)
    return redirect(reverse ('Admin:admin_rooms'))

def assign_explorer(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        character = Characters.objects.get(id=request.POST['character'])
        room.explored_by.add(character)
    return redirect(reverse ('Admin:admin_rooms'))


def assign_visitor(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        character = Characters.objects.get(id=request.POST['character'])
        room.currently_in.add(character)
    return redirect(reverse ('Admin:admin_rooms'))

def assign_treasure(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        treasure = Treasures.objects.get(id=request.POST['treasure'])
        room.treasure.add(treasure)
    return redirect(reverse ('Admin:admin_rooms'))

def assign_item(request):
    if request.method == "POST":
        character = Characters.objects.get(id=request.POST['character'])
        item = Items.objects.get(id=request.POST['item'])
        item.owned_by.add(character)
    context = {
        'item': Items.objects.get(id=request.POST['item']),
        'characters': Characters.objects.all(),
        }
    return render(request, 'gameadmin/character_item.html', context)

# DELETE

def delete_monster(request):
    if request.method == "POST":
        Monsters.objects.filter(id=request.POST['monster']).delete()
    return redirect('/admin/admin_monsters')

def delete_item(request):
    if request.method == "POST":
        Items.objects.filter(id=request.POST['item']).delete()
    return redirect('/admin/admin_items')


def delete_treasure(request):
    if request.method == "POST":
        Treasures.objects.filter(id=request.POST['treasure']).delete()
    return redirect('/admin/admin_treasure')

def delete_user(request):
    if request.method == "POST":
        Users.objects.filter(id=request.POST['user']).delete()
    return redirect('/admin/admin_users')

def delete_character(request):
    if request.method == "POST":
        Characters.objects.filter(id=request.POST['character']).delete()
    return redirect('/admin/admin_characters')

def delete_trap(request):
    if request.method == "POST":
        Traps.objects.filter(id=request.POST['trap']).delete()
    return redirect('/admin/admin_traps')

def delete_room(request):
    if request.method == "POST":
        Rooms.objects.filter(id=request.POST['room']).delete()
    return redirect('/admin/admin_rooms')

# ADD
def add_exit(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['source'])
        exit = Rooms.objects.get(id=request.POST['destination'])
        direction = (request.POST['direction'])
        if request.POST['direction2']:
            direction2 = (request.POST['direction2'])
        else:
            direction2 = "None"
        Exits.objects.add_exit(room, exit, direction, direction2)

    return redirect('/admin')

def add_monster(request):
    if request.method == "POST":
        Monsters.objects.add_monster(request.POST)
    return redirect('/admin/admin_monsters')

def add_treasure(request):
    if request.method == "POST":
        Treasures.objects.add_treasure(request.POST)
    return redirect('/admin/admin_treasure')

def add_trap(request):
    if request.method == "POST":
        Traps.objects.add_trap(request.POST)
    return redirect('/admin/admin_traps')

def add_room(request):
    if request.method == "POST":
        Rooms.objects.add_room(request.POST)
    return redirect('/admin/admin_rooms')

def add_item(request):
    if request.method == "POST":
        Items.objects.add_item(request.POST)
    return redirect('/admin/admin_items')


# REMOVE

def remove_killer(request):
    if request.method == "POST":
        monster = Monsters.objects.get(id=request.POST['monster'])
        character = Characters.objects.get(id=request.POST['character'])
        monster.killed_by.remove(character)
    return redirect('/admin')

def remove_treasure(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        treasure = Treasures.objects.get(id=request.POST['treasure'])
        room.treasure.remove(treasure)
    return redirect('/admin')

def remove_monster(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        monsterin = Monsters.objects.get(id=request.POST['monster'])
        room.monster.remove(monsterin)
    return redirect('/admin')

def remove_visitor(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        character = Characters.objects.get(id=request.POST['character'])
        room.currently_in.remove(character)
    return redirect(reverse ('Admin:admin_rooms'))

def remove_explorer(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        character = Characters.objects.get(id=request.POST['character'])
        room.explored_by.remove(character)
    return redirect(reverse ('Admin:admin_rooms'))

def remove_trap(request):
    if request.method == "POST":
        room = Rooms.objects.get(id=request.POST['room'])
        trap = Traps.objects.get(id=request.POST['trap'])
        room.trap.remove(trap)
    return redirect(reverse ('Admin:room_trap'))

def remove_character(request):
    if request.method == "POST":
        character = Characters.objects.get(id=request.POST['character'])
        item = Items.objects.get(id=request.POST['item'])
        character.owner.remove(item)
    context = {
        'item': Items.objects.get(id=request.POST['item']),
        'characters': Characters.objects.all(),
        }
    return render(request, 'gameadmin/character_item.html', context)
# ADMIN EDIT PAGES


def admin_characters(request):
    context = {
        'users': Users.objects.all().order_by('username'),
        'characters': Characters.objects.all().order_by('name'),
        'items': Items.objects.all().order_by('name'),
        }
    return render(request, 'gameadmin/admin_character.html', context)

def admin_items(request):
    context = {
        'items': Items.objects.all().order_by('name'),
        'characters':Characters.objects.all().order_by('name')
        }
    return render(request, 'gameadmin/admin_item.html', context)

def admin_monsters(request):
    context = {
        'characters': Characters.objects.all().order_by('name'),
        'monsters': Monsters.objects.all().order_by('name'),
        'rooms': Rooms.objects.all().order_by('id'),
        }
    return render(request, 'gameadmin/admin_monster.html', context)

def admin_rooms(request):
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
    return render(request, 'gameadmin/admin_room.html', context)

def admin_traps(request):
    context = {
        'rooms': Rooms.objects.all().order_by('id'),
        'traps': Traps.objects.all().order_by('name'),
        }
    return render(request, 'gameadmin/admin_trap.html', context)

def admin_treasure(request):
    context = {
        'rooms': Rooms.objects.all().order_by('id'),
        'items': Items.objects.all().order_by('name'),
        'treasures': Treasures.objects.all().order_by('name'),
        }
    return render(request, 'gameadmin/admin_treasure.html', context)

def admin_users(request):
    context = {
        'users': Users.objects.all().order_by('username'),
        'characters': Characters.objects.all().order_by('name'),
        }
    return render(request, 'gameadmin/admin_user.html', context)

# EDIT BUTTONS ON ADMIN SIDE


def edit_user(request, id):
    context = {
    'users': Users.objects.get(id=id)
    }
    return render(request, 'gameadmin/edit_user.html', context)

def edit_character(request, id):
    context = {
    'characters': Characters.objects.get(id=id),
    }
    return render(request, 'gameadmin/edit_character.html', context)

def edit_monster(request, id):
    context = {
    'monster': Monsters.objects.get(id=id),
    'characters': Characters.objects.all()
    }
    return render(request, 'gameadmin/edit_monster.html', context)

def edit_item(request, id):
    context = {
    'items': Items.objects.get(id=id),
    }
    return render(request, 'gameadmin/edit_items.html', context)

def edit_treasure(request, id):
    context = {
    'treasures': Treasures.objects.get(id=id),
    'items': Items.objects.all(),
    }
    return render(request, 'gameadmin/edit_treasure.html', context)

def edit_trap(request, id):
    context = {
    'traps': Traps.objects.get(id=id),
    }
    return render(request, 'gameadmin/edit_traps.html', context)

def edit_room(request, id):
    context = {
    'rooms': Rooms.objects.get(id=id),
    }
    return render(request, 'gameadmin/edit_room.html', context)

def update_user(request):
    if request.method == "POST":
        response_from_models = Users.objects.update_user(request.POST)
        if not response_from_models['status']:
            for error in response_from_models['errors']:
                messages.error(request, error)
    return redirect('edit_user/'+request.POST['id'])

def update_character(request):
    if request.method == "POST":
        response_from_models = Characters.objects.update_character(request.POST)
        if not response_from_models['status']:
            for error in response_from_models['errors']:
                messages.error(request, error)
    return redirect('edit_character/'+request.POST['id'])

def update_monster(request):
    if request.method == "POST":
        response_from_models = Monsters.objects.update_monster(request.POST)
        if not response_from_models['status']:
            for error in response_from_models['errors']:
                messages.error(request, error)
    return redirect('edit_monster/'+request.POST['id'])

def update_item(request):
    if request.method == "POST":
        response_from_models = Items.objects.update_item(request.POST)
        if not response_from_models['status']:
            for error in response_from_models['errors']:
                messages.error(request, error)
    return redirect('edit_item/'+request.POST['id'])

def update_treasure(request):
    if request.method == "POST":
        response_from_models = Treasures.objects.update_treasure(request.POST)
        if not response_from_models['status']:
            for error in response_from_models['errors']:
                messages.error(request, error)
    return redirect('edit_treasure/'+request.POST['id'])

def update_trap(request):
    if request.method == "POST":
        response_from_models = Traps.objects.update_trap(request.POST)
        if not response_from_models['status']:
            for error in response_from_models['errors']:
                messages.error(request, error)
    return redirect('edit_trap/'+request.POST['id'])

def update_room(request):
    if request.method == "POST":
        response_from_models = Rooms.objects.update_room(request.POST)
        if not response_from_models['status']:
            for error in response_from_models['errors']:
                messages.error(request, error)
    return redirect('edit_room/'+request.POST['id'])
