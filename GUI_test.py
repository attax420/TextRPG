import threading
from tkinter import *
from classes import *
from threading import *


p = Player()


def gamelogic():
    p.randomize_map()

# GameMap to Grid   
def thread_window_map():
    window_map = Tk()
    window_map_frame = Frame()
    window_button_frame = Frame()
    def map_update():
        p.position_update()
        p.print_map()
        for i in range(10):
            for j in range(10):       
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
        map_update()

    def move_south():
        p.move_south()        
        map_update()
        
    def move_east():
        p.move_east()        
        map_update()

    def move_west():
        p.move_west()
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


while True:

    thread_gamelogic = threading.Thread(target=gamelogic())
    thread_map = threading.Thread(target=thread_window_map())
    

    thread_gamelogic.start
    thread_map.start
    