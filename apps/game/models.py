from __future__ import unicode_literals
from django.db import models
from ..mainmenu.models import Characters, Users



class RoomManager(models.Manager):
    def add_room(self, postData):
        pass

class MonsterManager(models.Manager):
    def add_monster(self, postData):
        pass

class TrapManager(models.Manager):
    def add_trap(self, postData):
        pass

class TreasureManager(models.Manager):
    def add_treasure(self, postData):
        pass

class ExitManager(models.Manager):
    def add_exit(self, postData):
        pass

class ItemManager(models.Manager):
    def add_item(self, postData):
        pass


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
    last_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ItemManager()


class Treasure(models.Model):
    name = models.CharField(max_length=60, unique=True)
    gold = models.PositiveSmallIntegerField(default=0)
    item = models.ForeignKey(Items)
    last_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ItemManager()


class Traps(models.Model):
    PUZZLE = 'PZ'
    POISON = 'PS'
    REFLEX = 'RF'
    COLLAPSE = 'CL'
    name = models.CharField(max_length=60, unique=True)
    Tclass = models.CharField(max_length=2, choices=((PUZZLE, 'Puzzle'),(POISON, 'Poison'),(REFLEX, 'Reflex'), (COLLAPSE, 'Collapse')), default=POISON)
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
    treasure = models.ManyToManyField(Treasure)
    explored_by = models.ManyToManyField(Characters, related_name='explored')
    currently_in = models.ManyToManyField(Characters, related_name='populating')
    terrain_type = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MonsterManager()


class Exits(models.Model):
    exitdirection = models.CharField(max_length=30)
    leads_to = models.ManyToManyField(Rooms, related_name='exits')
    comes_from = models.ManyToManyField(Rooms, related_name='entrances')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ExitManager()
