from tkinter import *
import time
import random
from random import randint
import numpy as np

################################################################################################################################

grid_size = 25                                                                                                                      # how big each square is pixels
left_line_location = 100                                                                                                            # how big the middle area is (left side)
right_line_location = 600                                                                                                           # how big the middle area is (right side)
cell_size = int((right_line_location - left_line_location)/grid_size)                                                               # the number of cells
canvas_height = 500                                                                                                                 # how far down the screen
canvas_width = 700                                                                                                                  # how far across the screen
grid = [[0]*cell_size for i in range(0,cell_size)] + [[1]*cell_size for i in range(0, 1)]
square_array = [[0]*grid_size for i in range(0, cell_size)]

# straight line length 4
shape_one =   [[1,0,0,0],
               [1,0,0,0],
               [1,0,0,0],
               [1,0,0,0]]

shape_two =   [[1,0,0,0],
               [1,0,0,0],
               [1,1,0,0],
               [0,0,0,0]]

shape_three = [[0,1,0,0],
               [0,1,0,0],
               [1,1,0,0],
               [0,0,0,0]]

shape_four =  [[1,1,0,0],
               [1,1,0,0],
               [0,0,0,0],
               [0,0,0,0]]

shape_five =  [[1,1,0,0],
               [0,1,1,0],
               [0,0,0,0],
               [0,0,0,0]]

shape_six   = [[0,1,1,0],
               [1,1,0,0],
               [0,0,0,0],
               [0,0,0,0]]

shape_seven = [[1,1,1,0],
               [0,1,0,0],
               [0,0,0,0],
               [0,0,0,0]]
possible_shapes = [shape_one, shape_two, shape_three, shape_four, shape_five, shape_six, shape_seven]

def select_random_shape():
    chosen_shape = possible_shapes[randint(0,6)]
    return chosen_shape

# draws a chosen shape at the top of the screen
def draw_chosen_shape(shape, x_coord, y_coord):
    colors = ["red", "orange", "yellow", "green", "blue", "violet"]
    choice = colors[randint(0, 5)]

    x_location = x_coord * grid_size + left_line_location
    y_location = y_coord * grid_size

    for row in range(0, 4):
        for column in range(0, 4):
            if shape[row][column] == 1:
                 box = canv.create_rectangle(x_location+grid_size*column,y_location+grid_size*row,x_location+grid_size+grid_size*column,y_location+grid_size+grid_size*row,fill=choice)
                 co_ords = get_coordinates(box)
                 square_array[co_ords[0]][co_ords[1]] = box
                 grid[co_ords[0]][co_ords[1]] = 2


################################################################################################################################
# Moves the block slowly down the screen

def move_blocks(label):
    global box
    def count():
    #    location = get_coords()
     #   row = int(location[0])
      #  column = int(location[1])
       # move_down()
       # move_shape_down()
       # for x in range(cell_size-1,-1,-1):
        #    check_row_complete(x)
        move_shape_down()
        label.after(600,count)
        find_matrix()
    count()

################################################################################################################################
# moves the square 1 down


def move_shape_down():
    can_move = True
    # check if all parts of shape are able to be moved down
    for row in range(0, cell_size):
        for column in range(0, cell_size):
            if grid[row][column] == 2:
                if grid[row+1][column] == 1:
                    can_move = False

    dummy_square_array = [[0]*grid_size for i in range(0, cell_size)]
    dummy_grid = [[0]*cell_size for i in range(0,cell_size)] + [[1]*cell_size for i in range(0, 1)]


    if can_move:
        for row in range(0, cell_size):
            for column in range(0, cell_size):
                if grid[row][column] == 2:
                    current_square = square_array[row][column]
                    canv.move(current_square, 0, grid_size)
                    dummy_square_array[row+1][column] = current_square
                    dummy_grid[row+1][column] = 2
                    grid[row][column] = 0
                    square_array[row][column] = 0

        for row in range(0, cell_size):
            for column in range(0, cell_size):
                if dummy_grid[row][column] == 2:
                   grid[row][column] = 2
                   square_array[row][column] = dummy_square_array[row][column]

    else:
        for row in range(0, cell_size):
            for column in range(0, cell_size):
                if grid[row][column] == 2:
                    grid[row][column] = 1
        
        for y in range(0, 4):
            for x in range(cell_size-1,-1,-1):
                check_row_complete(x)

        test = select_random_shape()
        draw_chosen_shape(test, 4, 0)

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
        #create_shape(10,0)
################################################################################################################################
# checks if a horizontal row is full

def check_row_complete(row):
    if row == 0:
        pass
    else:
        row_filled = True
        for x in range(0, cell_size):
            if grid[row][x] == 0:
                row_filled = False
        if row_filled:
            delete_row(row)

# deletes a row

def delete_row(row):
    for x in range(0, cell_size):
        grid[row][x] = 0
        current_square = square_array[row][x]
        canv.delete(current_square)
    move_everything_down(row)

def move_everything_down(row_limit):
    dummy_square_array = [[0]*grid_size for i in range(0, cell_size)]
    dummy_grid = [[0]*cell_size for i in range(0,cell_size)] + [[1]*cell_size for i in range(0, 1)]
    
    for row in range(0, row_limit):
        for column in range(0, cell_size):
            if grid[row][column] == 1:
                dummy_square_array[row+1][column] = square_array[row][column]
                dummy_grid[row+1][column] = grid[row][column]
            if grid[row][column] == 2:
                dummy_grid[row][column] = 2
            if grid[row][column] == 1:
                current_square = square_array[row][column]
                canv.move(current_square, 0, grid_size)

    for row in range(0, row_limit+1):
        for column in range(0, cell_size):
            if dummy_grid[row][column] == 1 or dummy_grid[row][column] == 0:
                grid[row][column] = dummy_grid[row][column]
                square_array[row][column] = dummy_square_array[row][column]
   
################################################################################################################################
# return column / row co-ords of square

def get_coordinates(shape):                                                                                                             
    x_one, y_one, x_two, y_two = canv.coords(shape)
    x_coord = int((x_one - left_line_location)/grid_size)
    y_coord = int(y_one / grid_size)
    return [y_coord, x_coord]


def get_coords():                                                                                                             
    global box
    x_one, y_one, x_two, y_two = canv.coords(box)
    x_coord = (x_one - left_line_location)/grid_size
    y_coord = y_one / grid_size
    return [y_coord, x_coord]

################################################################################################################################
# moves the square 1 left

def move_shape_left():
    dummy_square_array = [[0]*grid_size for i in range(0, cell_size)]
    dummy_grid = [[0]*cell_size for i in range(0,cell_size)] + [[1]*cell_size for i in range(0, 1)]

    can_move = True
    for row in range(0, cell_size):
        for column in range(0, cell_size):
            if grid[row][column] == 2:
                if grid[row][column-1] == 1 or column == 0:
                    can_move = False 


    if can_move:
        for row in range(0, cell_size):
            for column in range(0, cell_size):
                if grid[row][column] == 2:
                    current_square = square_array[row][column]
                    canv.move(current_square, -grid_size, 0)
                    dummy_square_array[row][column-1] = current_square
                    dummy_grid[row][column-1] = 2
                    grid[row][column] = 0
                    square_array[row][column] = 0

        for row in range(0, cell_size):
            for column in range(0, cell_size):
                if dummy_grid[row][column] == 2:
                   grid[row][column] = 2
                   square_array[row][column] = dummy_square_array[row][column]

def move_shape_right():
    dummy_square_array = [[0]*grid_size for i in range(0, cell_size)]
    dummy_grid = [[0]*cell_size for i in range(0,cell_size)] + [[1]*cell_size for i in range(0, 1)]

    can_move = True
    for row in range(0, cell_size):
        for column in range(0, cell_size):
            if grid[row][column] == 2:
                if column == cell_size-1:
                    can_move = False
                elif grid[row][column+1] == 1 or column == cell_size:
                    can_move = False 


    if can_move:
        for row in range(0, cell_size):
            for column in range(0, cell_size):
                if grid[row][column] == 2:
                    current_square = square_array[row][column]
                    canv.move(current_square, grid_size, 0)
                    dummy_square_array[row][column+1] = current_square
                    dummy_grid[row][column+1] = 2
                    grid[row][column] = 0
                    square_array[row][column] = 0

        for row in range(0, cell_size):
            for column in range(0, cell_size):
                if dummy_grid[row][column] == 2:
                   grid[row][column] = 2
                   square_array[row][column] = dummy_square_array[row][column]



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
    #    move_left()
        move_shape_left()
    if event.keysym == 'd':
     #   move_right()
        move_shape_right()
    if event.keysym == 's':
      #  move_down()
        move_shape_down()
    if event.keysym == 'w':
        rotate_shape_left()

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

# finds the matrix that matches the current shape
def find_matrix():

    smallest_x = cell_size
    largest_x = 0

    smallest_y = cell_size
    largest_y = 0

    for row in range(0, cell_size):
        for column in range(0, cell_size):
            if grid[row][column] == 2:
                if column < smallest_x:
                    smallest_x = column
                if column > largest_x:
                    largest_x = column

                if row < smallest_y:
                    smallest_y = row
                if row > largest_y:
                    largest_y = row

    shape_matrix =[[0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]


    for row in range(smallest_y, smallest_y+4):
        for column in range(smallest_x, smallest_x+4):
            if row < cell_size and column < cell_size:
                if grid[row][column] == 2:
                    shape_matrix[row - smallest_y][column - smallest_x] = 1

    
    all_zero = True
    
    for x in range(0, 4):
        if shape_matrix[3][x] != 0:
            all_zero = False
        if shape_matrix[x][3] != 0:
            all_zero = False

    if all_zero:
        shape_matrix.pop(-1)
        for row in range(0, 3):
            shape_matrix[row].pop(-1)


    if shape_matrix[0][0] == 1 and shape_matrix[0][1] == 1 and shape_matrix[1][0] == 1 and shape_matrix[1][1] == 1:
        shape_matrix.pop(-1)
        shape_matrix[0].pop(-1)
        shape_matrix[1].pop(-1)

    return shape_matrix
    
def rotate_shape_left():

    original_shape = find_matrix()
    shape = find_matrix()

    new_shape = list(zip(*shape[::-1]))

    for x in range(0, len(shape[0])):
        for y in range(0, len(shape[0])):
            shape[x][y] = new_shape[x][y]

    dummy_square_array = [[0]*grid_size for i in range(0, cell_size)]
    dummy_grid = [[0]*cell_size for i in range(0,cell_size)] + [[1]*cell_size for i in range(0, 1)]

    smallest_x = cell_size
    smallest_y = cell_size

    for row in range(0, cell_size):
        for column in range(0, cell_size):
            if grid[row][column] == 2:
                if column < smallest_x:
                    smallest_x = column

                if row < smallest_y:
                    smallest_y = row

    for row in range(smallest_y, smallest_y + len(shape[0])):
        for column in range(smallest_x, smallest_x + len(shape[0])):
            if shape[row-smallest_y][column-smallest_x] == 1:
                dummy_grid[row][column] = 2


    for row in range(smallest_y, smallest_y + len(shape[0])):
        for column in range(smallest_x, smallest_x + len(shape[0])):
            if grid[row][column] == 2:
                replaced = False
                for row_dummy in range(smallest_y, smallest_y + len(shape[0])):
                    for column_dummy in range(smallest_x, smallest_x + len(shape[0])):
                        if replaced == False:
                            if dummy_grid[row_dummy][column_dummy] == 2:
                                x_difference = row_dummy - row
                                y_difference = column_dummy - column
                                #print ("The difference in x = " + str(x_difference) + " and in y is " + str(y_difference))
                                #print ("The value at (" + str(row) + "," + str(column) + ") maps to (" + str(row_dummy) + "," + str(column_dummy) + ")")
                                dummy_grid[row_dummy][column_dummy] = 3
                                grid[row][column] = 0
                                replaced = True
                                canv.move(square_array[row][column], grid_size * y_difference, grid_size * x_difference)
                                #print ("Moving the shape at (" + str(row) + ", " + str(column) + ") " + str(x_difference) + " cells right and " + str(y_difference) + " cells down")
                                #print ("")
                                dummy_square_array[row_dummy][column_dummy] = square_array[row][column]
                                square_array[row][column] = 0
                    

    for row in range(0, cell_size):
        for column in range(0, cell_size):
            if dummy_grid[row][column] == 3:
                grid[row][column] = 2
                square_array[row][column] = dummy_square_array[row][column]

    return shape


def start_game():
    global box
    global canv
    root = Tk()
    canv = Canvas(root, width = canvas_width, height = canvas_height, highlightthickness=0)
    canv.pack(fill='both', expand=True)                                                                            # the screen layout
    create_board()

    test = select_random_shape()
    draw_chosen_shape(test, 10,0)

    #create_shape(1,5)
    label = Label(root, text="Tetris")
    move_blocks(label)
    root.title("Tetris!")
    canv.bind("<1>", lambda event: canv.focus_set())
    canv.bind("<Key>", callback)
    canv.pack()
    root.mainloop()

#rotate_shape()
start_game()


