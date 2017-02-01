from __future__ import unicode_literals
from django.db import models
from ..login.models import Users



class CharacaterManager(models.Manager):
    def add_char(self, postData):
        pass


class Characters(models.Model):
    FIGHTER = 'FI'
    ROGUE = 'RO'
    WIZARD = 'WI'
    name = models.CharField(max_length=60)
    cclass = models.CharField(max_length=2, choices=((WIZARD, 'Wizard'),(ROGUE, 'Rogue'),(WIZARD, 'Wizard')), default=FIGHTER)
    strength = models.PositiveSmallIntegerField(default=1)
    dexterity = models.PositiveSmallIntegerField(default=1)
    intelligence = models.PositiveSmallIntegerField(default=1)
    health = models.PositiveSmallIntegerField(default=1)
    gold = models.PositiveSmallIntegerField(default=0)
    level = models.PositiveSmallIntegerField(max_length=3, default=1)
    owned_by = models.ForeignKey(Users)
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CharacaterManager()
