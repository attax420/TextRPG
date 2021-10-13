from classes import *

debug = False
cheatmode = True
p = Player()
p.randomize_map()
p.position_update()
p.print_map()
if cheatmode:
    p.attack_damage = 1000
    p.hp = 999999
p_effectcounter = 0
e_effectcounter = 0

# ######### PLAYER CONTROL FUNCTIONS ######### #
def p_showmp(p):
    print('You have '+str(p.mp)+'MP left!')

def p_showxp(p):
    xp, lvl = p.showxp()
    print('You have ' + str(xp) + 'XP and are on LVL' + str(lvl)+'!')

def p_showhp(p):
    print('You have ' + str(p.hp) + 'HP left!')

def e_showhp(e):
    print('The ' + e.name + ' has ' + str(e.hp) + 'HP left!')

def show_inventory(p):
    for i in p.inventory:
        print(i.name)

def equip(p):
    print('What do you want to equip?')
    show_inventory(p)
    try:
        item_in = input('->')
        if item_in == 'Diamond Sword':
            item_out = sword_diamond
        elif item_in == 'Steel Sword':
            item_out = sword_steel
        elif item_in == 'Bronze Sword':
            item_out = sword_bronze      
        else:
            item_out = None
            raise ValueError          
        p.equip(item_out)
        print('You equipped the '+str(item_out.name)+'!')
        
    except ValueError:
        print('Enter an item from the list to equip!')

def unequip(p):
    print('What do you want to unequip?')
    print(p.weapon.name)
    try:
        item_in = input('->')
        if item_in == 'Diamond Sword':
            item_out = sword_diamond
        elif item_in == 'Steel Sword':
            item_out = sword_steel
        elif item_in == 'Bronze Sword':
            item_out = sword_bronze      
        else:        
            item_out = None
            raise ValueError

        p.unequip(item_out)
        print('You unequipped the '+str(item_out.name)+'!')        

    except ValueError:
        print('Enter an item from the list to unequip!')

def use_healthpotion(p):   
    exec, state = p.use_item(healthpotion)
    if not exec and state == 'not usable':
        print ('This item is not usable!')
    if not exec and state == 'not available':
        print ('You don\'t have this item!')
    if exec:
        print('You used a Health Potion and recieved '+str(healthpotion.hp_bonus)+'HP!')

def use_manapotion(p):
    exec, state = p.use_item(manapotion)
    if not exec and state == 'not usable':
        print ('This item is not usable!')
    if not exec and state == 'not available':
        print ('You don\'t have this item!')
    if exec:
        print('You used a Mana Potion and recieved '+str(manapotion.mp_bonus)+'MP!')

def use_xppotion(p):    
    exec, state = p.use_item(xppotion)
    if not exec and state == 'not usable':
        print ('This item is not usable!')
    if not exec and state == 'not available':
        print ('You don\'t have this item!')
    if exec:
        print('You used a XP Potion and recieved '+str(xppotion.xp_bonus)+'XP!')
    print(p.lvl_up())
    
def cast_spell(p, e): 
    print('Which spell do you want to cast?')
    print('Avalilable spells: ')
    for i in p.spells:
        print(i)
    spell_select = input('->')

    while spell_select not in p.spells:        
        print('You dont have this spell... Enter a spell that you actually have.\n Available spells:\n')
        for i in p.spells:
            print(i)
        spell_select = input('->')
        
    if spell_select == 'fireball' and p.mp >=20:
        spellfireball.cast(p, e)
        print('You casted a fireball! It did '+str(spellfireball.dmg)+'DMG and the '+e.name+' is burning now!')        
    else:
        print('You dont have enough MP!')
# end PLAYER CONTROL FUNCTIONS #

while True:
    
    lvlup = p.lvl_up()
    if lvlup:
        print(lvlup)
        
    mode = 'explore'      # explore, fight, riddle, itemcrate
    # ######### EXPLORE MODE ######### #
    while mode == 'explore':
        # ######### EXPLORE MODE PLAYER MOVES ######### #
        moves = ('go north', 'go east', 'go south', 'go west',
                 'quit', 'show xp', 'show mp', 'show inventory', 'show hp',
                 'use healthpotion', 'use manapotion', 'use xppotion'
                 'equip', 'unequip')

        move = str(input('\n What do you want to do? \n'
                            'go north, go east, go south, go west,\n'
                            'show xp, show hp, show mp, show inventory,\n'
                            'use healthpotion, use manapotion, use xppotion,\n'
                            'equip, unequip, quit\n->'))
        
        if move == 'go north':
            exec = p.move_north()
            if exec:
                pass
            if not exec:
                print('There are huge Mountains that you cannot pass!')
        if move == 'go east':
            exec = p.move_east()
            if exec:
                pass
            if not exec:
                print('You see a huge cliff. Jumping of it is no option!')
        if move == 'go south':
            exec = p.move_south()
            if exec:
                pass
            if not exec:
                print('You see a big ocean. There is certainly no way past this!')
        if move == 'go west':
            exec = p.move_west()
            if exec:
                pass
            if not exec:
                print('There is a thick jungle full of dangerous animals. Walking through there would certainly kill you!')
        if move == 'quit':
            print('You commit suicide!')
            p.suicide()
        if move == 'show xp':
            p_showxp(p)
        if move == 'show hp':
            p_showhp(p)
        if move == 'show mp':
            p_showmp(p)
        if move == 'use healthpotion':
            use_healthpotion(p)
        if move == 'use manapotion':
            use_manapotion(p)      
        if move == 'use xppotion':
            use_xppotion(p)                   
        if move == 'show inventory':
            show_inventory(p)
        if move == 'equip':
            equip(p)
            move = None
        if move == 'unequip':
            unequip(p)
        if move not in moves and move != None:
            print('You have no idea what you are doing...')
        # end EXPLORE MODE PLAYER MOVES  #

        # ######### MAP FIELD CHECK AND EVENT ######### #
        field = str(p.check_field())
        if debug:
            print('\n\n\n# ######### DEBUG BEGIN ######### #')
            print('DEBUG field selection: '+str(field))
            print('# ######### DEBUG END ######### #\n\n\n')
        if field == 'empty':
            print('There is nothing special here...')
            p.position_update()
            p.print_map()
            break
        if field == 'visited':
            print('This place seems familiar...')
            p.position_update()
            p.print_map()
            break
        if field == 'heal':
            print('You feel much better now and also recieved a hp potion...')
            p.hp = p.max_hp
            p.inventory.append(healthpotion)
            p.position_update()
            p.print_map()
            break
        if field == 'goblin':
            print('You see a Goblin crawling out of a hole on the ground. '
                    'It watches you for a few seconds and then starts to attack you!')
            e = EnemyGoblin(p)
            mode = 'fight'
            break
        if field == 'ork':
            print('You see a Ork agressively walking towards you... It immediately attacks you!')
            e = EnemyOrk(p)
            mode = 'fight'
            break
        if field == 'troll':
            print('You see a Troll stomping on the ground... It spotted you and looks like it wants to fight!')
            e = EnemyTroll(p)
            mode = 'fight'
            break        
        if field == 'dragon':
            print('A huge Dragon appears in front of you! This will be a hard fight!')
            e = EnemyDragon(p)
            mode = 'fight'
        else:
            mode = 'explore'

        if debug:
            print('\n\n\n# ######### DEBUG BEGIN ######### #')
            print('DEBUG check_field function: '+str(p.check_field()))
            print('DEBUG player coordinates x:y: '+str(p.player_pos_x)+' : '+str(p.player_pos_y))            
            print('DEBUG state of player coordinates: '+str(p.map[p.player_pos_y][p.player_pos_x]))
            print('DEBUG mode variable: '+str(mode))
            print('# ######### DEBUG END ######### #\n\n\n')
        
        p.position_update()
        p.print_map()
        # end MAP FIELD CHECK AND EVENT #
    # end EXPLORE MODE #

    # ######### FIGHT MODE ######### # 
    if mode == 'fight':
        print('\n############ the fight starts! ############\n')
    while mode == 'fight':
        p_showhp(p)
        p_showmp(p)
        e_showhp(e)        
                    
        # ######### EFFECTS AND MOVE SELECTION ######### #
        e_move_choices = ['attack', 'defend']
        if e.name == 'Dragon':
            e_move_choices = ['attack','defend','fireball']                    
            text_choices = ('The Dragon screams: YOU WILL DIE!', 'Dragon screams: I WILL BURN YOU ALIVE!', 'Dragon screams: I WILL EAT YOUR FLESH!')
            text = choice(text_choices)        
            print(text)   
        
        if p.active_effect == 'fire':            #for bossfight
            dmg = 10
            p.hp -= dmg
            print('You are burning and recieved '+str(dmg)+' additional DMG!')
            p_effectcounter += 1
            if p_effectcounter == 3:
                p.active_effect == None
                p_effectcounter = 0

        if e.active_effect == 'fire':            
            print('The ' + e.name + ' is burning and recieved ' + str(spellfireball.effect_dmg) + ' additional DMG!')
            e.hp -= spellfireball.effect_dmg
            e_effectcounter += 1
            if p_effectcounter == 3:
                e.active_effect == None
                e_effectcounter = 0

        elif e.active_effect == 'ice':
            e_choice = 0
            print('The '+e.name+' is frozen and can\'t do anything')
        else:          
            e_choice = choice(e_move_choices)                        
        # end ENEMY EFFECTS AND MOVE SELECTION #

        # ######### BOSS SPECIFIC STUFF ######### #
                 
        # end BOSS SPECIFIC STUFF #

        # ######### PLAYER MOVE SELECTION ######### #
        moves = ('attack', 'defend', 'cast spell', 'use manapotion', 'use healthpotion', 'run away')

        move = input('\nWhat do you want to do? \nattack, defend, cast spell,\n'
                     'use manapotion, use healthpotion, run away:\n->')

        while move not in moves:  # Input validation
            move = input('Invalid Move! Try: \nattack, defend, cast spell,\n'
                     'use manapotion, use healthpotion, run away:\n->')
        
        if move == 'use manapotion':
            use_manapotion(p)
        if move == 'use healthpotion':
            use_healthpotion(p)          
        if move == 'cast spell':
            if e_choice == 'defend':
                e.defend()
                print('The '+e.name+' is defending!')
            cast_spell(p, e)
            e.attack(e, p)
            if e_choice == 1:
                print('The '+e.name+' attacks you for '+str(e.attack_damage)+' DMG!')            
        if move == 'run away':
            success = p.run_away(e)
            if success:
                print('You successfully escaped the '+e.name+'!')
                mode = 'explore'
                p.position_update()
                p.print_map()
                break
            if not success:
                print('You tried to run away, but the '+e.name+' is faster than you. The fight continues')
                mode = 'fight'
                e.attack(e, p)                   
        if move == 'attack':
            if e_choice == 'defend':
                e.defend()
                print('The '+e.name+' is defending!')
            p.attack(p, e)
            print('You attack the '+str(e.name)+' for '+str(p.attack_damage)+' DMG!')
        # end PLAYER MOVE SELECTION #

        # ######### ENEMY DEATH ######### #
        if e.hp <= 0:
            print('You killed the '+str(e.name)+' and got '+str(e.xp_bonus)+'XP!')            
            print('Loot recieved: ')
            for i in e.inventory:
                print(i.name)     
            if e.name == 'Dragon':
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                      'Congratulations!!!\n'
                      'You finished the game!!!\n'
                      'You are free to explore the rest of the world!\n'
                      'TextRPG created by: Alexander \'aTTaX\' Müller\n\n\n')
                p.map[p.boss_y][p.boss_x] = colored('X', 'blue')
                sleep(5)
                 
            for i in e.inventory:
                p.inventory.append(i)
            p.xp = p.xp + e.xp_bonus            
            p.position_update()
            p.print_map()
            mode = 'explore'
            break
        # end ENEMY DEATH #

        if debug:
            print('\n\n\n# ######### DEBUG BEGIN ######### #')
            print('DEBUG player action: '+p.action)
            print('# ######### DEBUG END ######### #\n\n\n')
        # ######### ENEMY ATTACK ######### #
        if e_choice == 'attack':
            if move == 'defend':
                p.defend()
                print('You are defending!')
            e.attack(e, p)
            print('The '+e.name+' attacks you for '+str(e.attack_damage)+' DMG!')
            
        if e_choice == 'fireball':
            if move == 'defend':
                p.defend()
                print('You are defending!')
            spellfireball.cast(e,p)
            print('The '+e.name+' casts a fireball on you for '+str(spellfireball.dmg)+' DMG!')
        # end ENEMY ATTACK #

        # ######### PLAYER DEATH ######### #        
        if p.hp <= 0:
            print('You were killed by the '+e.name+'! Rest in peace...')
            p.death()
        # end PLAYER DEATH #
    # end FIGHT MODE #  

