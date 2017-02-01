from __future__ import unicode_literals
from django.db import models
from ..login.models import Users



class CharacaterManager(models.Manager):
    def add_char(self, postData):
        errors = []
        if len(postData['char_name'])<4:
            errors.append('Character name must have more then 4 characters.')
        charname = Characters.objects.filter(name=postData['char_name'])
        if charname:
            errors.append('Character name already exist!')
        modelResponse = {}
        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        else:
            Characters.objets.create(name=postData['char_name'], cclas=postData['add_class'], strength=postData['strength'], dexterity=postData['dext'], intelligence=postData['intel'], health=postData['health'])

        return modelResponse



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
