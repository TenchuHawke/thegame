from __future__ import unicode_literals
from django.db import models
from ..login.models import Users


class CharacaterManager(models.Manager):
    def add_char(self, postData, user):
        errors = []
        if not postData['char_name']:
            errors.append('Character name must have more then 4 characters.')
        charname = Characters.objects.filter(name=postData['char_name'])
        if charname:
            errors.append('Character name already exist!')
        modelResponse = {}
        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        else:
            strength=int(postData['strength'])
            dexterity=int(postData['dext'])
            intelligence=int(postData['intel'])
            if postData['add_class'] == "FI":
                strength+=5
            elif postData['add_class']=="RO":
                dexterity+=5
            else:
                intelligence+=5
            try:
                user=Users.objects.get(username=postData['owned_by'])
            except:
                pass
            Characters.objects.create(name=postData['char_name'],   cclass=postData['add_class'], strength=strength, dexterity=dexterity, intelligence=intelligence, health=postData['health'], owned_by=user)
            char = Characters.objects.get(name=postData['char_name'])
            modelResponse['status']=True
            modelResponse['character']=char
        return modelResponse


class Characters(models.Model):
    FIGHTER = 'FI'
    ROGUE = 'RO'
    WIZARD = 'WI'
    name = models.CharField(max_length=60)
    cclass = models.CharField(max_length=2, choices=((FIGHTER, 'Fighter'), (ROGUE, 'Rogue'), (WIZARD, 'Wizard')), default=FIGHTER)
    strength = models.PositiveSmallIntegerField(default=1)
    dexterity = models.PositiveSmallIntegerField(default=1)
    intelligence = models.PositiveSmallIntegerField(default=1)
    health = models.PositiveSmallIntegerField(default=1)
    gold = models.PositiveSmallIntegerField(default=0)
    level = models.PositiveSmallIntegerField(default=1)
    owned_by = models.ForeignKey(Users)
    killed_by = models.CharField(max_length=255, default='')
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CharacaterManager()
