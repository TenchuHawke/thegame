from __future__ import unicode_literals
from django.db import models
from mainmenu import Char, Users


class CharManager(models.Manager):
    def add_char(self, postData):
        pass
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

class Char(models.Model):
    FIGHTER = 'FI'
    ROGUE = 'RO'
    WIZARD = 'WI'
    name = models.CharField(max_length=60)
    cclass = models.CharField(max_length=2, choices=((WIZARD, 'Wizard'),(ROGUE, 'Rogue'),(WIZARD, 'Wizard')), default=FIGHTER)
    strength = SmallIntegerField(default=1)
    dexterity = SmallIntegerField(default=1)
    intelligence = SmallIntegerField(default=1)
    health = SmallIntegerField(default=1)
    items = ManyToManyField(game.Items)
    gold = SmallIntegerField(default=0)
    level = SmallIntegerField(default=1)
    current_room = ForeignKey(game.Rooms)
    owned_by = ForeignKey(login.users)
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MonsterManager()

class Rooms(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    monster = ManyToManyField(Monsters)
    trap = ManyToManyField(Traps)
    treasure = ManyToManyField(Treasure)
    exits = ManyToManyField(Exits)
    explored_by = ManyToManyField(mainmenu.Char)
    terrain_type = CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MonsterManager()

class Monsters(models.Model):
    BRUTE = 'BR'
    ASSASSIN = 'AS'
    MAGE = 'MA'
    ELITE = 'EL'
    name = models.CharField(max_length=60, unique=True)
    mclass = models.CharField(max_length=2, choices=((BRUTE, 'Brute'), (ASSASSIN, 'Assassin'), (MAGE, 'Mage'), (ELITE, 'Elite')), default=BRUTE)
    strength = models.SmallIntegerField(default=1)
    dexterity = models.SmallIntegerField(default=1)
    intelligence = models.SmallIntegerField(default=1)
    health = models.SmallIntegerField(default=1)
    alive = models.BooleanField(default=True)
    image = models.CharField()
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MonsterManager()

class Traps(models.Model):
    PUZZLE = 'PZ'
    POISON = 'PS'
    REFLEX = 'RF'
    COLLAPSE = 'CL'
    name = models.CharField(max_length=60, unique=True)
    Tclass = models.CharField(max_length=2, choices=((PUZZLE, 'Puzzle'),(POISON, 'Poison'),(REFLEX, 'Reflex'), (COLLAPSE, 'Collapse')), default=POISON)
    strength = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}

    objects = TrapManager()

class Treasure(models.Model):
    name = models.CharField(max_length=60, unique=True)
    gold = models.SmallIntegerField(default=0)
    item = models.ManyToManyField(Items)
    last_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}

    objects = TreasureManager()

class Exits(models.Model):
    exitdirection = models.CharField(max_length=30)
    leadsTo = ForeignKey(Rooms)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ExitManager()

class Items(models.Model):
    name = models.CharField(max_length=60, unique=True)
    gold = models.SmallIntegerField(default=0)
    item = models.CharField(max_length=80)
    strbonus = models.SmallIntegerField()
    dexbonus = models.SmallIntegerField()
    intbonus = models.SmallIntegerField()
    hthbonus = models.SmallIntegerField()
    consumeable = models.BooleanField(default=False)
    last_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ItemManager()
