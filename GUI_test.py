import threading
from tkinter import *
from classes import *
from threading import *
debug = False

p = Player()
mode = 'explore'
p.randomize_map()

def gamelogic():  
    field = str(p.check_field())

    if debug:
        print('\n\n\n# ######### DEBUG BEGIN ######### #')
        print('DEBUG field selection: '+str(field))
        print('# ######### DEBUG END ######### #\n\n\n')
    
    if field == 'empty':        
        p.position_update()
        p.print_map()
        return('There is nothing special here...')
        
    if field == 'visited':        
        p.position_update()
        p.print_map()
        return('This place seems familiar...')
        
    if field == 'heal':        
        p.hp = p.max_hp
        p.inventory.append(healthpotion)
        p.position_update()
        p.print_map()
        return('You feel much better now and also recieved a hp potion...')

    if field == 'goblin':        
        e = EnemyGoblin(p)
        mode = 'fight'
        return('You see a Goblin crawling out of a hole on the ground. '
                'It watches you for a few seconds and then starts to attack you!')

    if field == 'dwarf':        
        e = EnemyDwarf(p)
        mode = 'fight'
        return('You see a Dwarf fetching his axe while walking towards you... He jumps towards you and attacks!')

    if field == 'ork':        
        e = EnemyOrk(p)
        mode = 'fight'
        return('You see a Ork agressively walking towards you... It immediately attacks you!')

    if field == 'troll':        
        e = EnemyTroll(p)
        mode = 'fight'
        return('You see a Troll stomping on the ground... It spotted you and looks like it wants to fight!')

    if field == 'dragon':        
        e = EnemyDragon(p)
        mode = 'fight'
        return('A huge Dragon appears in front of you! This will be a hard fight!')

    else:
        mode = 'explore'


printed_text = gamelogic()


window_map = Tk()
window_map_frame = Frame()
window_button_frame = Frame()
def map_update():
    p.position_update()
    p.print_map()
    for i in range(p.map_x):
        for j in range(p.map_y):       
            symbol = ' '
            entry = Entry(window_map_frame,bg='black', width=2,
                                font=('Arial',15,'bold'))
            
            if p.map[i][j] == ' ':
                symbol = ' '
                entry = Entry(window_map_frame,bg='black', width=2,
                                font=('Arial',15,'bold'))

            elif p.map[i][j] == colored(' ', 'green', 'on_white'):
                symbol = ' '
                entry = Entry(window_map_frame,bg='white', width=2,
                                font=('Arial',15,'bold'))

            elif p.map[i][j] == colored('X', 'blue'):
                symbol = 'X'
                entry = Entry(window_map_frame,bg='black',fg='blue', width=2,
                                font=('Arial',15,'bold'))

            elif p.map[i][j] == colored('+', 'red'):
                symbol = '+'
                entry = Entry(window_map_frame,bg='black',fg='red', width=2,
                                font=('Arial',15,'bold'))

            elif p.map[i][j] == colored('E', 'green'):
                symbol = 'E'
                entry = Entry(window_map_frame,bg='black',fg='green', width=2,
                                font=('Arial',15,'bold'))
        

            elif p.map[i][j] == colored('e', 'yellow'):
                symbol = 'e'
                entry = Entry(window_map_frame,bg='black',fg='yellow', width=2,
                                font=('Arial',15,'bold'))
        
            elif p.map[i][j] == colored('E', 'yellow'):
                symbol = 'E'
                entry = Entry(window_map_frame,bg='black',fg='yellow', width=2,
                                font=('Arial',15,'bold'))

            elif p.map[i][j] == colored('E', 'red'):
                symbol = 'E'
                entry = Entry(window_map_frame,bg='black',fg='red', width=2,
                                font=('Arial',15,'bold'))

            elif p.map[i][j] == colored('B', 'magenta'):
                symbol = 'B'
                entry = Entry(window_map_frame,bg='black',fg='magenta', width=2,
                                font=('Arial',15,'bold'))                

            entry.grid(row=i, column=j)
            entry.insert(END, symbol)
map_update()


sword_logo = PhotoImage(file='icon_small.png')

def move_north():
    p.move_north()
    gamelogic()        
    map_update()

def move_south():
    p.move_south()  
    gamelogic()      
    map_update()
    
def move_east():
    p.move_east()  
    gamelogic()      
    map_update()

def move_west():
    p.move_west()
    gamelogic()
    map_update()

button_go_north = Button(window_button_frame,
            text='go north',
            command=move_north,
            font=('Arial', 10,),
            fg='white',
            bg='#000000',
            relief=SUNKEN,
            #activeforeground='black',
            #activebackground='white',
            state=None,   # DISABLED
            image=sword_logo,
            compound='top'
            )
button_go_north.pack(side=LEFT)

button_go_south = Button(window_button_frame,
            text='go south',
            command=move_south,
            font=('Arial', 10,),
            fg='white',
            bg='#000000',
            relief=SUNKEN,
            #activeforeground='black',
            #activebackground='white',
            state=None,   # DISABLED
            image=sword_logo,
            compound='top'
            )
button_go_south.pack(side=LEFT)

button_go_east = Button(window_button_frame,
            text='go east',
            command=move_east,
            font=('Arial', 10,),
            fg='white',
            bg='#000000',
            relief=SUNKEN,
            #activeforeground='black',
            #activebackground='white',
            state=None,   # DISABLED
            image=sword_logo,
            compound='top'
            )
button_go_east.pack(side=LEFT)

button_go_west = Button(window_button_frame,
            text='go west',
            command=move_west,
            font=('Arial', 10,),
            fg='white',
            bg='#000000',
            relief=SUNKEN,
            #activeforeground='black',
            #activebackground='white',
            state=None,   # DISABLED
            image=sword_logo,
            compound='top'
            )
button_go_west.pack(side=LEFT)

window_map_frame.pack()
window_button_frame.pack()
window_map.configure(bg='black')
window_map.mainloop()
