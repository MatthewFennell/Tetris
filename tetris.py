from tkinter import *
import time

################################################################################################################################
# Moves the block slowly down the screen
counter = 0
def move_blocks(label, shape):
    global box
    def count():
        location = get_coords()
        row = int(location[0])
        column = int(location[1])
        if grid[row][column] != 1:
            #canv.move(shape, 0, grid_size)
            move_down()
        else:
            move_down()
        label.config(text=str(counter))
        label.after(300,count)
    count()
################################################################################################################################

def move_down():
    global box
    location = get_coords()
    row = int(location[0])
    column = int(location[1])
    if grid[row][column] != 1:
        canv.move(box, 0, grid_size)
    else:
        box = canv.create_rectangle((left_line_location+right_line_location)/2, 0, (left_line_location+right_line_location)/2+grid_size,grid_size, fill = "green")

def get_coords():                                                                                                              # returns column / row
    global box
    x_one, y_one, x_two, y_two = canv.coords(box)
    x_coord = (x_one - left_line_location)/grid_size
    y_coord = y_one / grid_size
    return [y_coord, x_coord]

def move_left():
    global box
    location = get_coords()
    row = int(location[0])
    column = int(location[1])
    if canv.coords(box)[0] > left_line_location:
        canv.move(box,-grid_size,0)

def move_right():
    global box
    location = get_coords()
    row = int(location[0])
    column = int(location[1])
    if canv.coords(box)[0] < right_line_location - cell_size*2:
        canv.move(box,grid_size,0)


def callback(event):
    if event.keysym == 'a':
        move_left()
    if event.keysym == 'd':
        move_right()

grid_size = 25                                                                                                                      # how big the grid is (N x N)
left_line_location = 100                                                                                                            # how big the middle area is (left side)
right_line_location = 600                                                                                                           # how big the middle area is (right side)
cell_size = int((right_line_location - left_line_location)/grid_size)                                                                    # how big each cell is
canvas_height = 500                                                                                                                 # how far down the screen
canvas_width = 700                                                                                                                  # how far across the screen
grid = [[0]*grid_size for i in range(0,cell_size-1)] + [[1]*cell_size for i in range(0, 3)]

square_array = [[0]*grid_size for i in range(0, cell_size-1)]



root = Tk()
canv = Canvas(root, width = canvas_width, height = canvas_height, highlightthickness=0)
canv.pack(fill='both', expand=True)                                                                            # the screen layout
##################################################################################################################################  
top = canv.create_line(left_line_location, 0, right_line_location, 0, fill='green', tags=('top'))                                   # the top line 
left = canv.create_line(left_line_location, 0, left_line_location, canvas_height, fill='green', tags=('left'))                      # the left line 

right = canv.create_line(right_line_location, 0, right_line_location, canvas_height, fill='green', tags=('right'))                  # the right line

bottom = canv.create_line(left_line_location, canvas_height, right_line_location, canvas_height, fill='red', tags=('bottom'))       # the bottom line

left = canv.create_rectangle(0,0, left_line_location, canvas_height, fill = "#000080")                                              # the left square area

right = canv.create_rectangle(right_line_location, 0, canvas_width, canvas_height, fill = "#000080")                                # the right square area

middle = canv.create_rectangle(left_line_location, 0, right_line_location, canvas_height, fill = "#2f2f2f")                         # the center area 
#####################################################################################################################################

global box
box = canv.create_rectangle((left_line_location+right_line_location)/2, 0, (left_line_location+right_line_location)/2+grid_size,grid_size, fill = "yellow")
label = Label(root, text="hi")
move_blocks(label,box)
root.title("counting seconds")
canv.bind("<1>", lambda event: canv.focus_set())
canv.bind("<Key>", callback)
canv.pack()

root.mainloop()

