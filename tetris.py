from tkinter import *
import time


left_line_location = 100        # how big the middle area is (left side)
right_line_location = 700       # how big the middle area is (right side)
canvas_height = 600             # how far down the screen
canvas_width = 800              # how far across the screen

root = Tk()
canv = Canvas(root, width = canvas_width, height = canvas_height, highlightthickness=0)
canv.pack(fill='both', expand=True)
################################################################################################################################
# the screen layout

# the top line
top = canv.create_line(left_line_location, 0, right_line_location, 0, fill='green', tags=('top'))

#the left line
left = canv.create_line(left_line_location, 0, left_line_location, canvas_height, fill='green', tags=('left'))

# the right line
right = canv.create_line(right_line_location, 0, right_line_location, canvas_height, fill='green', tags=('right'))

# the bottom line
bottom = canv.create_line(left_line_location, canvas_height, right_line_location, canvas_height, fill='red', tags=('bottom'))

# the left hand side
left = canv.create_rectangle(0,0, left_line_location, canvas_height, fill = "#000080")

# the right hand side
right = canv.create_rectangle(right_line_location, 0, canvas_width, canvas_height, fill = "#000080")

# the center area
middle = canv.create_rectangle(left_line_location, 0, right_line_location, canvas_height, fill = "#2f2f2f")
################################################################################################################################

box = canv.create_rectangle((left_line_location+right_line_location)/2, 0, (left_line_location+right_line_location)/2+10,10, fill = "yellow")

counter = 0
def move_blocks(label):
    def count():
        canv.move(box,0,10)
        label.config(text=str(counter))
        label.after(300,count)
    count()

label = Label(root, fg="green")
label.pack()
move_blocks(label)
button = Button(root, text='Stop', width=25, command = root.destroy)
button.pack()
root.title("counting seconds")

root.mainloop()

