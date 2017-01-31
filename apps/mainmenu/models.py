from __future__ import unicode_literals
from django.db import models
from ..login.models import Users


class CharManager(models.Manager):
    def add_char(self, postData):
        pass


class Char(models.Model):
    FIGHTER = 'FI'
    ROGUE = 'RO'
    WIZARD = 'WI'
    name = models.CharField(max_length=60)
    cclass = models.CharField(max_length=2, choices=((WIZARD, 'Wizard'),(ROGUE, 'Rogue'),(WIZARD, 'Wizard')), default=FIGHTER)
    strength = IntegerField(default=1)
    dexterity = IntegerField(default=1)
    intelligence = IntegerField(default=1)
    health = IntegerField(default=1)
    items = ManyToManyField(game.Items)
    gold = IntegerField(default=0)
    level = IntegerField(default=1)
    current_room = ForeignKey(game.Rooms)
    owned_by = ForeignKey(login.users)
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MonsterManager()
