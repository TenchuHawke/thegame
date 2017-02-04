from __future__ import unicode_literals
from django.db import models
from ..login.models import Users



class RoomManager(models.Manager):
    def add_room(self, postData):
        Rooms.objects.create(
        name = postData['name'],
        description = postData['description'],
        peek_description = postData['peek_description'],
        terrain_type = postData['terrain_type'],
        )

    def update_room(self, postData):
        errors = []
        room = Rooms.objects.filter(name=postData['name']).exclude(id=postData['id'])
        print postData
        if room:
            errors.append('Trap already exists')

        modelResponse={}
        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        else:
            room = Rooms.objects.get(id=postData['id'])
            room.name = postData['name']
            room.description = postData['description']
            room.peek_description = postData['peek_description']
            room.terrain_type = postData['terrain_type']
            room.save()
            modelResponse['status'] = True
        return modelResponse


    def fill_room(self, room, hero):
        pass


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
        image = postData['image'],
        )

    def update_monster(request, postData):
        errors = []
        monster = Monsters.objects.filter(name=postData['name']).exclude(id=postData['id'])
        if monster:
            errors.append('Monster Name already exists')

        modelResponse={}

        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        else:
            monster = Monsters.objects.get(id=postData['id'])
            monster.name = postData['name']
            monster.mclass = postData['mclass']
            monster.killed_by = postData['killed_by']
            monster.strength = postData['strength']
            monster.dexterity = postData['dexterity']
            monster.intelligence = postData['intelligence']
            monster.health = postData['health']
            monster.image = postData['image']
            monster.save()
            modelResponse['status'] = True
        return modelResponse


class TrapManager(models.Manager):
    def add_trap(self, postData):
        Traps.objects.create(
        name = postData['name'],
        tclass = postData['tclass'],
        strength = postData['strength'],
        )

    def update_trap(self, postData):
        errors = []
        trap = Treasures.objects.filter(name=postData['name']).exclude(id=postData['id'])
        print postData
        if trap:
            errors.append('Trap already exists')

        modelResponse={}

        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        else:
            trap = Traps.objects.get(id=postData['id'])
            trap.name = postData['name']
            trap.tclass = postData['class']
            trap.strength = postData['strength']
            trap.save()
            modelResponse['status'] = True
        return modelResponse

class TreasureManager(models.Manager):
    def add_treasure(self, postData):
        item=Items.objects.get(id=postData['item'])
        Treasures.objects.create(
        name = postData['name'],
        gold = postData['gold'],
        item = item,
        )

    def update_treasure(self, postData):
        errors = []
        treasure = Treasures.objects.filter(name=postData['name']).exclude(id=postData['id'])
        teaitem = Items.objects.get(id=postData['item'])
        print postData
        if treasure:
            errors.append('Treasure already exists')

        modelResponse={}

        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        else:
            treasure = Treasures.objects.get(id=postData['id'])
            treasure.name = postData['name']
            treasure.gold = postData['gold']
            treasure.item = teaitem
            treasure.save()
            modelResponse['status'] = True
        return modelResponse


class ExitManager(models.Manager):
    def add_exit(self, room, exit, direction, direction2):
        Exits.objects.create(
        exitdirection = direction,
        leads_to = room,
        comes_from = exit,
        )
        if not direction2 == "None":
            Exits.objects.create(
            exitdirection = direction2,
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
        consumable = postData['consumable'],
        )

    def update_item(self, postData):
        errors = []
        item = Items.objects.filter(name=postData['item']).exclude(id=postData['id'])
        print postData
        if item:
            errors.append('Item already exists')

        modelResponse={}

        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        else:
            item = Items.objects.get(id=postData['id'])
            item.name = postData['item']
            item.strbonus = postData['strbonus']
            item.dexbonus = postData['dexbonus']
            item.intbonus = postData['intbonus']
            item.hthbonus = postData['hthbonus']
            item.consumable = postData['consumable']
            item.save()
            modelResponse['status'] = True
        return modelResponse

class CombatManager(models.Manager):
    def add_combat(self, room, hero, monsters):
        combat=self.objects.create(room=room, hero=hero)
        for monster in monsters.all():
            combat.monsters.add(monster)
        combat.save()
        print combat


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


    def update_character(self, postData):
        errors = []
        character = Characters.objects.filter(name=postData['name']).exclude(id=postData['id'])
        if character:
            errors.append('Character Name already exists')

        modelResponse={}

        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        else:
            character = Characters.objects.get(id=postData['id'])
            character.name = postData['name']
            character.cclass = postData['cclass']
            character.strength = postData['strength']
            character.dexterity = postData['dext']
            character.intelligence = postData['intel']
            character.health = postData['health']
            character.current_health = postData['current_health']
            character.gold = postData['gold']
            character.killed_by = postData['killed_by']
            character.level = postData['level']
            character.save()
            modelResponse['status'] = True
        return modelResponse



    def calculate_stats(self, character):
        strength = character.strength
        dexterity = character.dexterity
        intelligence = character.intelligence
        health = character.health
        for item in character.owner.all():
            if not item.consumable:
                strength+=int(item.strbonus)
                dexterity+=int(item.dexbonus)
                intelligence+=int(item.intbonus)
                health+=int(item.hthbonus)
        strdiff= int(strength)-int(character.strength)
        strdiff= '{:+}'.format(strdiff)
        dexdiff= int(dexterity)-int(character.dexterity)
        dexdiff= '{:+}'.format(dexdiff)
        intdiff= int(intelligence)-int(character.intelligence)
        intdiff= '{:+}'.format(intdiff)
        hthdiff= int(health)-int(character.health)
        hthdiff= '{:+}'.format(hthdiff)

        return_to_view = {
        'strength': strength,
        'dexterity': dexterity,
        'intelligence': intelligence,
        'health': health,
        'strdiff': strdiff,
        'dexdiff': dexdiff,
        'intdiff': intdiff,
        'hthdiff': hthdiff,
        }
        return (return_to_view)

    def move(self, hero, room, destination):
        errors=[]
        modelResponse={}
        count=0
        # TODO monster blocking
        alive_monsters=[]
        print room.monster.all()
        if room.monster.all():
            print "room has monster"
            for monster in room.monster.all():
                if monster.killed_by.all():
                    print monster.name
                    for monster_kb in monster.killed_by.all():
                        print monster_kb
                        print monster_kb.id
                        if monster_kb.id == hero.id:
                            count = count + 1
                        if count == 0:
                            alive_monsters.append(monster)
                    if alive_monsters:
                        errors.append(monster.name+" blocks your way")
                else:
                    errors.append(monster.name+" blocks your way")
        if errors:
            modelResponse['status']=False
            modelResponse['errors']=errors
        else:
            modelResponse['status']=True
            room.explored_by.add(hero)
            room.currently_in.remove(hero)
            destination.currently_in.add(hero)
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
    current_health = models.SmallIntegerField(default=1)
    gold = models.PositiveSmallIntegerField(default=0)
    level = models.PositiveSmallIntegerField(default=1)
    owned_by = models.ForeignKey(Users)
    killed_by = models.CharField(max_length=255, default='')
    slug = models.SlugField()
    prepopulated_fields = {
        "slug": ("name",),
        "current_health": ("health",)
        }
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CharacaterManager()


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
    killed_by = models.ManyToManyField(Characters, related_name="killed")
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
    owned_by = models.ManyToManyField(Characters, related_name='owner')
    consumable = models.BooleanField(default=False)
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
    peek_description = models.TextField()
    monster = models.ManyToManyField(Monsters, related_name='denizen')
    trap = models.ManyToManyField(Traps, related_name='dangers')
    treasure = models.ManyToManyField(Treasures, related_name='reward')
    explored_by = models.ManyToManyField(Characters, related_name='explored')
    currently_in = models.ManyToManyField(Characters, related_name='populating')
    terrain_type = models.CharField(max_length=50)
    slug = models.SlugField()
    prepopulated_fields = {"slug": ("name",)}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RoomManager()


class Exits(models.Model):
    exitdirection = models.CharField(max_length=30)
    leads_to = models.ForeignKey(Rooms, related_name='exits')
    comes_from = models.ForeignKey(Rooms, related_name='entrances')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ExitManager()

class Combats(models.Model):
    room = models.ForeignKey(Rooms, related_name="combat_location"),
    hero = models.ForeignKey(Characters, related_name="combat_hero"),
    monsters = models.ManyToManyField(Monsters, related_name="combat_villians"),

    objects = CombatManager()
