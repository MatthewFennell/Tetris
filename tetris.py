from tkinter import *
import time
import random

################################################################################################################################

grid_size = 25                                                                                                                      # how big each square is pixels
left_line_location = 100                                                                                                            # how big the middle area is (left side)
right_line_location = 600                                                                                                           # how big the middle area is (right side)
cell_size = int((right_line_location - left_line_location)/grid_size)                                                               # the number of cells
canvas_height = 500                                                                                                                 # how far down the screen
canvas_width = 700                                                                                                                  # how far across the screen
grid = [[0]*cell_size for i in range(0,cell_size)] + [[1]*cell_size for i in range(0, 1)]
square_array = [[0]*grid_size for i in range(0, cell_size)]

################################################################################################################################
# Moves the block slowly down the screen

def move_blocks(label, shape):
    global box
    def count():
        location = get_coords()
        row = int(location[0])
        column = int(location[1])
        move_down()
        check_row_complete(cell_size-1)
        label.after(300,count)
    count()

################################################################################################################################
# moves the square 1 down

def move_down():
    global box
    location = get_coords()
    row = int(location[0])
    column = int(location[1])
    if grid[row+1][column] != 1:
        grid[row][column] = 0
        canv.move(box, 0, grid_size)
        grid[row+1][column] = 1
    else:
        square_array[row][column] = box
        create_shape(10,0)
################################################################################################################################
# checks if a horizontal row is full

def check_row_complete(row):
    if row == 0:
        print ("Finished")
    else:
        row_filled = True
        for x in range(0, cell_size):
            if grid[row][x] == 0:
                row_filled = False
        if row_filled:
            delete_row(row)


def delete_row(row):
    for x in range(0, cell_size):
        grid[row][x] = 0
        current_square = square_array[row][x]
        canv.delete(current_square)
    
    # lets the squares fall (only fall down 1 row currently)
    for x in range(0, cell_size):
        if grid[row-1][x] == 1:
            current_square = square_array[row-1][x]
            canv.move(current_square,0, grid_size)
            grid[row-1][x] = 0
            grid[row][x] = 1

################################################################################################################################
# return column / row co-ords of square

def get_coords():                                                                                                             
    global box
    x_one, y_one, x_two, y_two = canv.coords(box)
    x_coord = (x_one - left_line_location)/grid_size
    y_coord = y_one / grid_size
    return [y_coord, x_coord]

################################################################################################################################
# moves the square 1 left

def move_left():
    global box
    location = get_coords()
    row = int(location[0])
    column = int(location[1])
    if canv.coords(box)[0] > left_line_location and grid[row][column-1] == 0:
        grid[row][column] = 0
        canv.move(box,-grid_size,0)
        grid[row][column-1] = 1

################################################################################################################################
# moves the square 1 right

def move_right():
    global box
    location = get_coords()
    row = int(location[0])
    column = int(location[1])
    if canv.coords(box)[0] < right_line_location - cell_size*2 and grid[row][column+1] == 0:
        grid[row][column] = 0
        canv.move(box,grid_size,0)
        grid[row][column+1] = 1

################################################################################################################################
# tracks keyboard input

def callback(event):
    if event.keysym == 'a':
        move_left()
    if event.keysym == 'd':
        move_right()
    if event.keysym == 's':
        move_down()

#####################################################################################################################################
# creates the board structure

def create_board():
    top = canv.create_line(left_line_location, 0, right_line_location, 0, fill='green', tags=('top'))                                   # the top line 
    left = canv.create_line(left_line_location, 0, left_line_location, canvas_height, fill='green', tags=('left'))                      # the left line 
    right = canv.create_line(right_line_location, 0, right_line_location, canvas_height, fill='green', tags=('right'))                  # the right line
    bottom = canv.create_line(left_line_location, canvas_height, right_line_location, canvas_height, fill='red', tags=('bottom'))       # the bottom line
    left = canv.create_rectangle(0,0, left_line_location, canvas_height, fill = "#000080")                                              # the left square area
    right = canv.create_rectangle(right_line_location, 0, canvas_width, canvas_height, fill = "#000080")                                # the right square area
    middle = canv.create_rectangle(left_line_location, 0, right_line_location, canvas_height, fill = "#2f2f2f")                         # the center area 

################################################################################################################################
# creates a square shape at x,y of random color

def create_shape(x_coord, y_coord):
    global box
    x_location = x_coord * grid_size + left_line_location
    y_location = y_coord * grid_size
    colors = ["red", "orange", "yellow", "green", "blue", "violet"]
    box = canv.create_rectangle(x_location, y_location, x_location + grid_size, y_location + grid_size, fill = random.choice(colors))
    
################################################################################################################################
# starts the game

def start_game():
    global box
    global canv
    root = Tk()
    canv = Canvas(root, width = canvas_width, height = canvas_height, highlightthickness=0)
    canv.pack(fill='both', expand=True)                                                                            # the screen layout
    create_board()
    create_shape(10,0)
    label = Label(root, text="Tetris")
    move_blocks(label,box)
    root.title("Tetris!")
    canv.bind("<1>", lambda event: canv.focus_set())
    canv.bind("<Key>", callback)
    canv.pack()
    root.mainloop()

start_game()


