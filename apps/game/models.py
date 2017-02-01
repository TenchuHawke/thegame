from __future__ import unicode_literals
from django.db import models
from ..mainmenu.models import Characters, Users



class RoomManager(models.Manager):
    def add_room(self, postData):
        Rooms.objects.create(
        name = postData['name'],
        description = postData['description'],
        terrain_type = postData['terrain_type'],
        )
    def assign_exit(self, postdata):
        pass

    def assign_treasure(self, room, treasure):
        room.objects.create(treasure=treasure)

    def unassign_treasure(self, room, treasure):
        room.objects.delete(treasure=treasure)

class MonsterManager(models.Manager):
    def add_monster(self, postData):
        strength = int(postData['strength'])
        dexterity = int(postData['dexterity'])
        intelligence = int(postData['intelligence'])
        health = int(postData['health'])
        if postData['mclass']=="BR" or postData['mclass']=='EL':
            strength+=5
        elif postData['mclass']=="AS" or postData['mclass']=='EL':
            dexterity+=5
        elif postData['mclass']=="MA" or postData['mclass']=='EL':
            intelligence+=5
        else:
            health +=5
        Monsters.objects.create(
        name = postData['name'],
        mclass = postData['mclass'],
        strength = strength,
        dexterity = dexterity,
        intelligence = intelligence,
        health = postData['health'],
        alive = postData['alive'],
        image = postData['image'],
        )
    def assign_treasure(self, postData):
        pass

class TrapManager(models.Manager):
    def add_trap(self, postData):
        Traps.objects.create(
        name = postData['name'],
        tclass = postData['tclass'],
        strength = postData['strength'],
        )
    def assign_treasure(self, postData):
        pass

class TreasureManager(models.Manager):
    def add_treasure(self, postData):
        item=Items.objects.get(id=postData['item'])
        Treasures.objects.create(
        name = postData['name'],
        gold = postData['gold'],
        item = item,
        )

    def assign_item(self, treasure, item):
        treasure.objects.create(item=item)

    def unassign_item(self, treasure, item):
        treasure.objects.delete(item=item)

class ExitManager(models.Manager):
    def add_exit(self, room, exit, direction):
        Exits.objects.create(
        exitdirection = direction,
        leads_to = exit,
        comes_from = room,
        )
    def del_exit(self, room, exit):
        exit=Exits.objects.filter(leads_from=room).filter(comes_from=exit).get(exitdirection=direction)
        exit.objects.delete()


class ItemManager(models.Manager):
    def add_item(self, postData):
        Items.objects.create(
        name = postData['name'],
        strbonus = postData['strbonus'],
        dexbonus = postData['dexbonus'],
        intbonus = postData['intbonus'],
        hthbonus = postData['hthbonus'],
        consumeable = postData['consumeable'],
        )


class Monsters(models.Model):
    BRUTE = 'BR'
    ASSASSIN = 'AS'
    MAGE = 'MA'
    ELITE = 'EL'
    name = models.CharField(max_length=60, unique=True)
    mclass = models.CharField(max_length=2, choices=((BRUTE, 'Brute'), (ASSASSIN, 'Assassin'), (MAGE, 'Mage'), (ELITE, 'Elite')), default=BRUTE)
    strength = models.PositiveSmallIntegerField(default=1)
    dexterity = models.PositiveSmallIntegerField(default=1)
    intelligence = models.PositiveSmallIntegerField(default=1)
    health = models.PositiveSmallIntegerField(default=1)
    alive = models.BooleanField(default=True)
    image = models.CharField(max_length=10)
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MonsterManager()


class Items(models.Model):
    name = models.CharField(max_length=60, unique=True)
    strbonus = models.PositiveSmallIntegerField()
    dexbonus = models.PositiveSmallIntegerField()
    intbonus = models.PositiveSmallIntegerField()
    hthbonus = models.PositiveSmallIntegerField()
    owned_by = models.ManyToManyField(Characters)
    consumeable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ItemManager()


class Treasures(models.Model):
    name = models.CharField(max_length=60, unique=True)
    gold = models.PositiveSmallIntegerField(default=0)
    item = models.ForeignKey(Items)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TreasureManager()


class Traps(models.Model):
    PUZZLE = 'PZ'
    POISON = 'PS'
    REFLEX = 'RF'
    COLLAPSE = 'CL'
    name = models.CharField(max_length=60, unique=True)
    tclass = models.CharField(max_length=2, choices=((PUZZLE, 'Puzzle'),(POISON, 'Poison'),(REFLEX, 'Reflex'), (COLLAPSE, 'Collapse')), default=POISON)
    strength = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}

    objects = TrapManager()


class Rooms(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    monster = models.ManyToManyField(Monsters)
    trap = models.ManyToManyField(Traps)
    treasure = models.ManyToManyField(Treasures)
    explored_by = models.ManyToManyField(Characters, related_name='explored')
    currently_in = models.ManyToManyField(Characters, related_name='populating')
    terrain_type = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RoomManager()


class Exits(models.Model):
    exitdirection = models.CharField(max_length=30)
    leads_to = models.ManyToManyField(Rooms, related_name='exits')
    comes_from = models.ManyToManyField(Rooms, related_name='entrances')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ExitManager()
