from tkinter import *
from classes import *

p = Player()
p.randomize_map()
p.position_update()
p.print_map()
a=10
  
window = Tk()

        # code for creating table
for i in range(10):
    print(i)
    for j in range(10): 
        
        symbol = ' '
        e = Entry(window,bg='black', width=2,
                            font=('Arial',15,'bold'))
        
        if p.map[j][i] == ' ':
            symbol = ' '
            e = Entry(window,bg='black', width=2,
                            font=('Arial',15,'bold'))

        elif p.map[j][i] == colored(' ','green','on_white'):
            symbol = ' '
            e = Entry(window,bg='white', width=2,
                            font=('Arial',15,'bold'))

        elif p.map[j][i] == colored('X', 'blue'):
            symbol = 'X'
            e = Entry(window,bg='black',fg='blue', width=2,
                            font=('Arial',15,'bold'))

        elif p.map[j][i] == colored('+', 'red'):
            symbol = '+'
            e = Entry(window,bg='black',fg='red', width=2,
                            font=('Arial',15,'bold'))

        elif p.map[j][i] == colored('E', 'green'):
            symbol = 'E'
            e = Entry(window,bg='black',fg='green', width=2,
                            font=('Arial',15,'bold'))
    

        elif p.map[j][i] == colored('e', 'yellow'):
            symbol = 'e'
            e = Entry(window,bg='black',fg='yellow', width=2,
                            font=('Arial',15,'bold'))
    
        elif p.map[j][i] == colored('E', 'yellow'):
            symbol = 'E'
            e = Entry(window,bg='black',fg='yellow', width=2,
                            font=('Arial',15,'bold'))

        elif p.map[j][i] == colored('E', 'red'):
            symbol = 'E'
            e = Entry(window,bg='black',fg='red', width=2,
                            font=('Arial',15,'bold'))

        elif p.map[j][i] == colored('B', 'magenta'):
            symbol = 'B'
            e = Entry(window,bg='black',fg='magenta', width=2,
                            font=('Arial',15,'bold'))                

        e.grid(row=i, column=j)
        e.insert(END, symbol)



 
# find total number of rows and
# columns in list

 
# create window window S

 
##window.attributes("-fullscreen",True)
window.configure(bg='black')
 
window.mainloop()