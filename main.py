#python2 library Tkinter 2
from cProfile import label
from cgitb import text
from turtle import width
from Tkinter import Frame, Label, CENTER

import logics as l
import constants as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid() #using grid manager
        self.master.title('2048') #title of frame is 2048
        self.master.bind("<Key>", self.key_down) #if anykey pressed in this frame
        self.commands = {c.KEY_UP: l.move_up(), c.KEY_DOWN: l.move_down(),
                        c.KEY_LEFT: l.move_left(), c.KEY_RIGHT: l.move_right()}

        self.grid_cells = []
        self.init_grid() #add the grid cells
        self.init_matrix() #initialise matrix 
        self.update_grid_matrix() #update matrix grid

        self.mainloop() #runs the game


    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                            width =c.SIZE, height=c.size)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row =[]
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY, width=c.SIZE/c.GRID_LEN, height = c.SIZE/c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING, pady=c.GRID_PADDING)
                t =label(master = cell, text="", bg =c.BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font =c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = l.start_game() #start game or create matrix
        #add two 2s to begin with
        l.add_new_2(self.matrix)
        l.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg=c.BACKGROUND_COLOR_DICT[new_number], fg=c.CELL_COLOR_DICT[new_number],fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks() #wait until all colors change
    
    def key_down(self, event):
        key =repr(event.char) #'w' -> "'w'"
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                l.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if l.get_current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if l.get_current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][2].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)


gamegrid = Game2048()