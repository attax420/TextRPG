from random import choice 
from termcolor import colored
from time import sleep
import os
from platform import system

if system().lower() == 'windows':
    os.system('color')


# ######### MAP ######### #
class GameMap:
    def __init__(self):        
        self.map = []
        self.map_x = 10
        self.map_y = 10
        self.player_pos_x = int(choice(range(self.map_x -1)))
        self.player_pos_y = int(choice(range(self.map_y -1)))        
        self.boss_x = int(choice(range(self.map_x -1)))
        self.boss_y = int(choice(range(self.map_y -1)))        
        for i in range(self.map_y):
            self.map.append([])
            for j in range(self.map_x):
                self.map[i].append(-1)

    def position_update(self):
        run = True        
        while run == True:
            if self.boss_x != self.player_pos_x or self.boss_y != self.player_pos_y:                
                       self.map[self.player_pos_y][self.player_pos_x] = colored(' ','green','on_white')
                       run = False
            else:
                self.player_pos_x = int(choice(range(self.map_x -1)))
                self.player_pos_y = int(choice(range(self.map_y -1)))  
                continue
    
    def print_map(self):
        for i in range(self.map_y):
            for j in range(self.map_x):
                print(self.map[i][j], ' | ', end=' ')
            print()
        print()

    def randomize_map(self):
        for i in range(self.map_y):
            for j in range(self.map_x):
                if self.map[j][i] == -1:
                    self.map[j][i] = choice([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                                             colored('E', 'green'), colored('E', 'yellow'), colored('E', 'red'), colored('+', 'red'), colored('e', 'yellow')])
        self.map[self.boss_y][self.boss_x] = colored('B', 'magenta')
        
        

    def check_field(self):
        if self.map[self.player_pos_y][self.player_pos_x] == colored('X', 'blue'):
            return 'visited'

        if self.map[self.player_pos_y][self.player_pos_x] == colored('+', 'red'):
            return 'heal'

        if self.map[self.player_pos_y][self.player_pos_x] == ' ':
            return 'empty'

        if self.map[self.player_pos_y][self.player_pos_x] == colored('E', 'green'):
            return 'goblin'

        if self.map[self.player_pos_y][self.player_pos_x] == colored('e', 'yellow'):
            return 'dwarf'

        if self.map[self.player_pos_y][self.player_pos_x] == colored('E', 'yellow'):
            return 'troll'

        if self.map[self.player_pos_y][self.player_pos_x] == colored('E', 'red'):
            return 'ork'

        if self.map[self.player_pos_y][self.player_pos_x] == colored('B', 'magenta'):
            return 'dragon'

    def move_north(self):
        if self.player_pos_y != 0:
            self.map[int(self.player_pos_y)][int(self.player_pos_x)] = colored('X', 'blue')
            self.player_pos_y -= 1
            return True
        else:
            return False


    def move_south(self):
        if self.player_pos_y != self.map_y-1:
            self.map[int(self.player_pos_y)][int(self.player_pos_x)] = colored('X', 'blue')
            self.player_pos_y += 1
            return True
        else:
            return False

    def move_west(self):
        if self.player_pos_x != 0:
            self.map[int(self.player_pos_y)][int(self.player_pos_x)] = colored('X', 'blue')
            self.player_pos_x -= 1
            return True
        else:
            return False

    def move_east(self):
        if self.player_pos_x != self.map_y-1:
            self.map[int(self.player_pos_y)][int(self.player_pos_x)] = colored('X', 'blue')
            self.player_pos_x += 1
            return True
        else:
            return False
# end MAP #

enemies = ['Goblin','Troll','Ork','Dwarf']

# ######### CHARACTERS ######### #
class Character(GameMap):
    def __init__(self):
        GameMap.__init__(self)                             
        self.max_hp = None
        self.hp = None
        self.mana = None
        self.attack_damage = None
        self.name = None
        self.spells = None
        self.inventory = None
        self.lvl = None
        self.xp = None
        self.action = None
        self.active_effect = None

    def attack(self, attacker, target):    
        self.action = 'attack'
        if target.hp > 0 and target.action != 'defend':
            target.hp -= int(attacker.attack_damage)
        if target.hp > 0 and target.action == 'defend':
            target.hp -= int(attacker.attack_damage)/2

    def defend(self):
        self.action = 'defend'       

    def drop_item(self):
        pass



class Player(Character, GameMap):

    def __init__(self):        
        Character.__init__(self)        
        self.name = 'Player'
        self.lvl = 1
        self.attack_damage = 15
        self.max_hp = 100
        self.max_mp = 50
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.xp = 0
        self.spells = ['fireball']
        self.inventory = []
        self.weapon = None
        self.gear = {'Head': 'none',
                    'Torso': 'none',
                    'Legs': 'none',
                    'Feet': 'none'}
        self.dmg_bonus = 0
        
    def equip(self, item):        
        if item in weaponlist and item in self.inventory and self.weapon == None:
            self.weapon = item
            self.inventory.remove(item)
            self.dmg_bonus = item.dmg_bonus
            return True
        return False

    def unequip(self, item):
        if self.weapon != None and item == self.weapon:
            self.dmg_bonus = 0            
            self.inventory.append(item)            
            self.weapon = None
            return True
        else:
            return False

    def showspells(self):
        return self.spells

    def showxp(self):
        return self.xp, self.lvl

    def pickup_item(self):
        pass

    def equip_item(self):
        pass

    def use_world(self):
        pass

    def use_item(self, item):
        if not item.interactive:
                return False, 'not usable'
        if item not in self.inventory:
            return False, 'not available'
        if item in self.inventory:
            item.use(self)
            for i, v in enumerate(self.inventory):
                if v == item:
                    self.inventory.pop(i)
                    return True, 'success'



    def lvl_up(self):
        lvlup = False 
        if self.lvl == 8:
            self.xp = 0       
        if self.xp >= 100 and self.lvl < 2:
            self.lvl = 2            
            self.max_hp += 20
            self.mp += 30
            self.mp = self.max_mp
            self.hp = self.max_hp
            if self.xp >= 100:
                self.xp -= 100
            else:
                self.xp = 0
            self.attack_damage = self.attack_damage * 1.1      
            lvlup = True      
        if self.xp >= 200 and self.lvl < 3:
            self.lvl = 3
            self.max_hp += 40
            self.hp = self.max_hp
            self.mp += 60
            self.mp = self.max_mp
            if self.xp >= 200:
                self.xp -= 200
            else:
                self.xp = 0
            self.attack_damage = self.attack_damage * 1.3 
            lvlup = True              
        if self.xp >= 400 and self.lvl < 4:
            self.lvl = 4            
            self.max_hp += 60
            self.mp += 80
            self.mp = self.max_mp
            self.hp = self.max_hp
            if self.xp >= 400:
                self.xp -= 400
            else:
                self.xp = 0
            self.attack_damage = self.attack_damage * 1.6 
            lvlup = True              
        if self.xp >= 700 and self.lvl < 5:
            self.lvl = 5            
            self.max_hp += 100
            self.hp = self.max_hp
            self.mp += 150
            self.mp = self.max_mp
            if self.xp >= 800:
                self.xp -= 800
            else:
                self.xp = 0
            self.attack_damage = self.attack_damage * 2    
            lvlup = True           
        if self.xp >= 1300 and self.lvl < 6:
            self.lvl = 6            
            self.max_hp += 130
            self.hp = self.max_hp
            self.mp += 200
            self.mp = self.max_mp
            if self.xp >= 1600:
                self.xp -= 1600
            else:
                self.xp = 0
            self.attack_damage = self.attack_damage * 2.5       
            lvlup = True        
        if self.xp >= 2000 and self.lvl < 7:
            self.lvl = 7            
            self.max_hp += 180
            self.mp += 250
            self.mp = self.max_mp
            self.hp = self.max_hp
            if self.xp >= 2400:
                self.xp -= 2400       
            else:
                self.xp = 0
            self.attack_damage = self.attack_damage * 2.7    
            lvlup = True      
        if self.xp >= 2800 and self.lvl < 8:
            self.lvl = 8            
            self.max_hp += 200
            self.hp = self.max_hp
            self.mp += 300
            self.mp = self.max_mp
            self.xp = 0
            self.attack_damage = self.attack_damage * 3 + self.dmg_bonus
            lvlup = True 

        
        if lvlup:
            if self.lvl == 8:
                return('LVL up!!! You are now on LVL 8 which is the maximum LVL!')
            else:
                return ('LVL up!!! You are now LVL ' + str(self.lvl) + '!')            
        else:
            return False

    @staticmethod
    def suicide():
        sleep(2)
        exit('exit by suicide...')

    @staticmethod
    def death():
        sleep(2)
        exit('exit by death...')

    @staticmethod
    def run_away(e):
        mode_choices = ('explore', 'fight')
        mode = choice(mode_choices)
        if mode == 'fight':
            return False
        if mode == 'explore':
            return True


class Enemy(Character):
    def __init__(self):
        Character.__init__(self)
        self.action = None        
        self.xp_bonus = 0

    def showhp(self):
        return self.name, self.hp

class EnemyGoblin(Enemy):
    def __init__(self, p):
        Enemy.__init__(self)        
        self.xp_bonus = 10
        self.name = 'Goblin'
        self.hp = int(p.max_hp)/2
        self.hp = self.hp.__round__(2)        
        self.attack_damage = int(p.attack_damage)/4
        choices = [healthpotion,manapotion,xppotion]
        self.inventory = [choice(choices)]

class EnemyDwarf(Enemy):
    def __init__(self, p):
        Enemy.__init__(self)
        self.xp_bonus = 35
        self.name = 'Dwarf'
        self.hp = int(p.max_hp)/1.5
        self.hp = self.hp.__round__(2)
        self.attack_damage = int(p.attack_damage)/1.8
        choices = (healthpotion, manapotion, xppotion, healthpotion, manapotion, xppotion, healthpotion, manapotion, xppotion, sword_bronze)
        self.inventory = [choice(choices)]

class EnemyTroll(Enemy):
    def __init__(self, p):
        Enemy.__init__(self)        
        self.xp_bonus = 25
        self.name = 'Troll'
        self.hp = int(p.max_hp)/1.5
        self.hp = self.hp.__round__(2)
        self.attack_damage = int(p.attack_damage)/2
        choices = (healthpotion, manapotion, xppotion, healthpotion, manapotion, xppotion, healthpotion, manapotion, xppotion, sword_bronze)
        self.inventory = [choice(choices)]

class EnemyOrk(Enemy):            
    def __init__(self, p):
        Enemy.__init__(self)        
        self.xp_bonus = 50
        self.name = 'Ork'
        self.hp = int(p.max_hp)/1
        self.hp = self.hp.__round__(2)
        self.attack_damage = int(p.attack_damage)/1.5
        choices = (healthpotion, manapotion, xppotion, healthpotion, manapotion, xppotion, sword_bronze, sword_bronze, sword_bronze, sword_steel)
        self.inventory = [choice(choices)]

class EnemyDragon(Enemy):
    def __init__(self, p):
        Enemy.__init__(self)
        self.mp = 999999
        self.xp_bonus = 800
        self.name = 'Dragon'
        self.hp = 2000
        self.inventory = [sword_diamond, manapotion, manapotion, healthpotion]
        self.attack_damage = 30
        self.spells = ['fireball']
   

# end CHARACTERS #

# ######### ITEMS ######### #
class Item:
    def __init__(self):
        self.name = None
        self.worth = 0
        self.interactive = True
        self.can_use_in_fight = True
        self.consumable = True
        self.weight = 0


class Potion(Item):
    def __init__(self):
        Item.__init__(self)
        self.weight = 0.5


class PotionHP(Potion):
    def __init__(self):
        Potion.__init__(self)
        self.name = 'HP Potion'
        self.hp_bonus = 50

    def use(self, p):
        p.hp = p.hp + self.hp_bonus
        if p.hp >= p.max_hp:
            p.hp = p.max_hp
        return self.hp_bonus


class PotionXP(Potion):
    def __init__(self):
        Potion.__init__(self)
        self.name = 'XP Potion'
        self.xp_bonus = 150


    def use(self, p):
        p.xp = p.xp + self.xp_bonus
        p.lvl_up
        return self.xp_bonus


class PotionMP(Potion):
    def __init__(self):
        Potion.__init__(self)
        self.name = 'MP Potion'
        self.mp_bonus = 50

    def use(self, p):
        p.mp = p.mp + self.mp_bonus
        if p.mp >= p.max_mp:
            p.mp = p.max_mp
        return self.mp_bonus


class Weapon(Item):
    dmg_bonus = None
    pass

class WeaponBronzeSword(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Bronze Sword'
        self.dmg_bonus = 10

class WeaponSteelSword():
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Steel Sword'
        self.dmg_bonus = 40

class WeaponDiamondSword():
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Diamond Sword'
        self.dmg_bonus = 160

class Armor(Item):
    pass
# end ITEMS #


# ######### SPELLS ######### #
class Spell():
    def __init__(self): 
        self.name = None       
        self.effect = None
        self.dmg = None
        self.mana_usage = None
        self.effect_dmg = None

    def cast(self, attacker, target):
        target.hp -= self.dmg
        attacker.mp -= self.mana_usage
        target.active_effect = self.effect
        return self.dmg, self.mana_usage, self.effect


class SpellFireball(Spell):
    def __init__(self):        
        Spell.__init__(self)
        self.name = 'Fireball'
        self.dmg = 50
        self.mana_usage = 20
        self.effect_dmg = 5
        self.effect = 'fire'

         
class SpellBlizzard(Spell):
    def __init__(self):
        Spell.__init__(self)
        self.name = 'Blizzard'
        self.dmg = 50
        self.mana_usage = 30
        self.effect_dmg = 0
        self.effect = 'ice'
# end SPELLS #


# ######### Objects ######### #
healthpotion = PotionHP()
manapotion = PotionMP()
xppotion = PotionXP()
spellfireball = SpellFireball()
spellblizzard = SpellBlizzard()
sword_bronze = WeaponBronzeSword()
sword_steel = WeaponSteelSword()
sword_diamond = WeaponDiamondSword()

# ######### ITEMLISTS + SPELLLIST ######### #
weaponlist = [sword_bronze, sword_steel, sword_diamond]
potionlist = [healthpotion, manapotion, xppotion]
spelllist = [spellfireball, spellblizzard]
# end ITEMLISTS + SPELLLIST #
# end OBJECTS #