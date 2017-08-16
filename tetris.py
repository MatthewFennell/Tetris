from tkinter import *
import time
import random
from random import randint

################################################################################################################################
global score 
global text_value
score = 0
grid_size = 25                                                                                                                      # how big each square is pixels
left_line_location = 200                                                                                                            # how big the middle area is (left side)
right_line_location = 700                                                                                                           # how big the middle area is (right side)
cell_size = int((right_line_location - left_line_location)/grid_size)                                                               # the number of cells
canvas_height = 500                                                                                                                 # how far down the screen
canvas_width = 900                                                                                                                  # how far across the screen
grid = [[0]*cell_size for i in range(0,cell_size)] + [[1]*cell_size for i in range(0, 1)]
square_array = [[0]*grid_size for i in range(0, cell_size)]
next_shapes = [0,0,0]
next_colours = [0,0,0]

side_shape_one = [[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]


side_shape_two = [[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]


side_shape_three = [[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]







################################################################################################################################

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

shape_eight = [[1,0,0,1],
               [0,1,1,0],
               [0,1,1,0],
               [1,0,0,1]]

possible_shapes = [shape_one, shape_two, shape_three, shape_four, shape_five, shape_six, shape_seven]
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
for x in range(0, 3):
    next_shapes[x] = randint(0, len(possible_shapes)-1)
    next_colours[x] = randint(0, len(colors)-1)
################################################################################################################################


def draw_next_shapes():

    for row in range(0, 4):
        for column in range(0, 4):
            canv.delete(side_shape_one[row][column])
            canv.delete(side_shape_two[row][column])
            canv.delete(side_shape_three[row][column])

    for shape_number in range(0, 3):

        shape = possible_shapes[next_shapes[shape_number]]

        
        
        x = (canvas_width + right_line_location) / 2 - grid_size
        y = 100 + 130 * shape_number

        for row in range(0, len(shape)):
            for column in range(0, 4):
                if shape[row][column] == 1:
                    side_shape = canv.create_rectangle(x+grid_size*column,y+grid_size*row,x+grid_size+grid_size*column,y+grid_size+grid_size*row,fill=colors[next_colours[shape_number]])
                    
                    if shape_number == 0:
                        side_shape_one[row][column] = side_shape
                    if shape_number == 1:
                        side_shape_two[row][column] = side_shape
                    if shape_number == 2:
                        side_shape_three[row][column] = side_shape




def text(increase):
    global score
    global text_value
    canv.delete(text_value)
    score = score + increase
    text_value = canv.create_text((canvas_width+right_line_location)/2,30,fill="white",font="Times 20 italic bold",text="Score = " + str(score))
    canv.update

def select_random_shape():
    chosen_shape = possible_shapes[randint(0,len(possible_shapes)-1)]
    return chosen_shape

# draws a chosen shape at the top of the screen
def draw_chosen_shape(shape, x_coord, y_coord, color):

    x_location = x_coord * grid_size + left_line_location
    y_location = y_coord * grid_size

    for row in range(0, 4):
        for column in range(0, 4):
            if shape[row][column] == 1:
                 box = canv.create_rectangle(x_location+grid_size*column,y_location+grid_size*row,x_location+grid_size+grid_size*column,y_location+grid_size+grid_size*row,fill=color)
                 co_ords = get_coordinates(box)
                 square_array[co_ords[0]][co_ords[1]] = box
                 grid[co_ords[0]][co_ords[1]] = 2


################################################################################################################################
# Moves the block slowly down the screen

def move_blocks(label):
    def count():
        move_shape_down()
        label.after(300,count)
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

    # if it can move, store new values into temporary array
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

    # reassign the values
        for row in range(0, cell_size):
            for column in range(0, cell_size):
                if dummy_grid[row][column] == 2:
                   grid[row][column] = 2
                   square_array[row][column] = dummy_square_array[row][column]

    else:
        # if it can't move, set the active shape values (2) to non active (1)
        for row in range(0, cell_size):
            for column in range(0, cell_size):
                if grid[row][column] == 2:
                    grid[row][column] = 1
        # check for complete rows (4 times as max number is 4)
        a = 0 # number of rows deleted at once
        for y in range(0, 4):
            for x in range(cell_size-1,-1,-1):
                a += check_row_complete(x)
        if a > 0:
            text(10 + (20*(a-1)))
        # since it can't move down anymore, must spawn another shape
        draw_chosen_shape(possible_shapes[next_shapes[0]], (right_line_location-left_line_location)/(2*grid_size)-1 , 0, colors[next_colours[0]])
        text(1)
        next_shapes.pop(0)
        next_shapes.append(randint(0, len(possible_shapes)-1))
        next_colours.pop(0)
        next_colours.append(randint(0, len(colors)-1))
        draw_next_shapes()

################################################################################################################################
# checks if a horizontal row is full and deletes it if it's full

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
            return 1
    return 0

# deletes a row

def delete_row(row):
    # set all values to 0
    # then move everything above it down 1
    for x in range(0, cell_size):
        grid[row][x] = 0
        current_square = square_array[row][x]
        canv.delete(current_square)
    move_everything_down(row)

# moves everything above row_limit down 1
def move_everything_down(row_limit):
    # create temporary arrays to store in
    dummy_square_array = [[0]*grid_size for i in range(0, cell_size)]
    dummy_grid = [[0]*cell_size for i in range(0,cell_size)] + [[1]*cell_size for i in range(0, 1)]
    
    # up to row_limit, move all peices down 1 -> store in temporary array
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

    # reassign the temporary array
    # avoids overwriting data
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


################################################################################################################################
# moves the square 1 left

def move_shape_left():

    # create temporary arrays to store grid data in
    dummy_square_array = [[0]*grid_size for i in range(0, cell_size)]
    dummy_grid = [[0]*cell_size for i in range(0,cell_size)] + [[1]*cell_size for i in range(0, 1)]

    # check if it's possible to move each part of the shape
    can_move = True
    for row in range(0, cell_size):
        for column in range(0, cell_size):
            if grid[row][column] == 2:
                if grid[row][column-1] == 1 or column == 0:
                    can_move = False 

    # if it can be moved, move it into a temporary array (both the grid and square)
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

    # transfer the temporary values back
        for row in range(0, cell_size):
            for column in range(0, cell_size):
                if dummy_grid[row][column] == 2:
                   grid[row][column] = 2
                   square_array[row][column] = dummy_square_array[row][column]

# same as move left, but right
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
################################################################################################################################
# tracks keyboard input

def callback(event):
    if event.keysym == 'a':
        move_shape_left()
    if event.keysym == 'd':
        move_shape_right()
    if event.keysym == 's':
        move_shape_down()
    if event.keysym == 'w':
        rotate_left()

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

# finds the matrix that matches the current shape
def find_matrix():

    # find the smallest and largest x/y values
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

    # initialise the shape matrix
    shape_matrix =[[0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]

    # search only the small region where the active shape could possibly be
    # maximum 4x4 size
    # set shape_matrix value to equal those of the active shape where it = 2
    for row in range(smallest_y, smallest_y+4):
        for column in range(smallest_x, smallest_x+4):
            if row < cell_size and column < cell_size:
                if grid[row][column] == 2:
                    shape_matrix[row - smallest_y][column - smallest_x] = 1

    # chop off the end bits of the shape matrix if unnecessary
    # as they affect the rotation
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

    # make it 2x2 if it's the square shape
    if shape_matrix[0][0] == 1 and shape_matrix[0][1] == 1 and shape_matrix[1][0] == 1 and shape_matrix[1][1] == 1:
        shape_matrix.pop(-1)
        shape_matrix[0].pop(-1)
        shape_matrix[1].pop(-1)

    return shape_matrix
 ################################################################################################################################
   
def rotate_left():

    # get an array of the active shape
    shape = find_matrix()
    dummy = find_matrix()

    # rotate it (magic)
    new_shape = list(zip(*shape[::-1]))

    # reassign it back
    for x in range(0, len(shape[0])):
        for y in range(0, len(shape[0])):
            shape[x][y] = new_shape[x][y]

    # check to see if the left most column is all 0 
    # this section stops rotation to move it sideways
    for z in range(0,3):
        first_column_all_zero = True
        for x in range(0, len(shape[0])):
            if shape[x][0] != 0:
                first_column_all_zero = False

        # if it is all 0, then shift everything in the shape to the left one
        # loops through this 3 times as that's the most anything could be shifted left
        if first_column_all_zero:
            for row in range(0, len(shape[0])):
                for column in range(1, len(shape[0])):
                    dummy[row][column-1] = shape[row][column]
                dummy[row][len(shape[0])-1] = 0
    
            # reassign shape back
            for row in range(0, len(shape[0])):
                for column in range(0, len(shape[0])):
                    shape[row][column] = dummy[row][column]

    # temporary arrays to store the new rotated values in
    dummy_square_array = [[0]*grid_size for i in range(0, cell_size)]
    dummy_grid = [[0]*cell_size for i in range(0,cell_size)] + [[1]*cell_size for i in range(0, 1)]

    # find the smallest x and y value (top left corner) of active shape
    smallest_x = cell_size
    smallest_y = cell_size

    for row in range(0, cell_size):
        for column in range(0, cell_size):
            if grid[row][column] == 2:
                if column < smallest_x:
                    smallest_x = column

                if row < smallest_y:
                    smallest_y = row

    # search the small square region where the active shape is
    # if it is a block, set the dummy grid value at that location = 2
    for row in range(smallest_y, smallest_y + len(shape[0])):
        for column in range(smallest_x, smallest_x + len(shape[0])):
            if shape[row-smallest_y][column-smallest_x] == 1:
                dummy_grid[row][column] = 2
    
    # pair up the old co-ordinates with the new ones
    # 1 ) find part of the original shape
    # 2 ) find a part of the new rotated shape (stored in the dummy arrays)
    # 3 ) find the difference in co-ordinates between them
    # 4 ) move the original shape to the new location
    # 5 ) update the values so that these are not paired again and the remaining squares are selected
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
                    
    # reassigns the dummy arrays back to the true arrays
    for row in range(0, cell_size):
        for column in range(0, cell_size):
            if dummy_grid[row][column] == 3:
                grid[row][column] = 2
                square_array[row][column] = dummy_square_array[row][column]

    
    

    return shape
################################################################################################################################
# draws the grid lines

def draw_lines():
    for column in range(0, cell_size):
        canv.create_line(left_line_location + column * grid_size, 0, left_line_location + column * grid_size, canvas_height, fill = "black", width = 1)
        canv.create_line(left_line_location, column * grid_size, right_line_location, column * grid_size, fill = "black", width = 1)
################################################################################################################################
# starts the game

def start_game():
    global canv
    global text_value
    root = Tk()
    canv = Canvas(root, width = canvas_width, height = canvas_height, highlightthickness=0)
    canv.pack(fill='both', expand=True)                                                                            # the screen layout
    create_board()
    text_value = canv.create_text((canvas_width+right_line_location)/2,30,fill="white",font="Times 20 italic bold",text="Score = " + str(score))
    draw_lines()
    draw_next_shapes()
    starter = select_random_shape()
    draw_chosen_shape(starter, (right_line_location-left_line_location)/(2*grid_size)-1 ,0, colors[randint(0, len(colors)-1)])
    label = Label(root, text="Tetris")
    move_blocks(label)
    root.title("Tetris!")
    canv.bind("<1>", lambda event: canv.focus_set())
    canv.bind("<Key>", callback)
    canv.pack()
    root.mainloop()
################################################################################################################################

start_game()


