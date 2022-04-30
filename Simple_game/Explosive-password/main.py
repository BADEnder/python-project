from email import message
from tkinter import *
from PIL import Image, ImageTk
import random
import time 

def start():
    global left 
    global right 

    global min_input
    global max_input
    global result_frame
    global result_message
    global explosive_num
    global guess_num
    global enter_but

    if min_input.get() != "" and max_input.get() != "" :
        left = int(min_input.get())
        right =int(max_input.get())
        min_input = Entry(frame, width=15 ,borderwidth=2, state=DISABLED)
        max_input = Entry(frame, width=15 ,borderwidth=2, state=DISABLED)
        
        min_input.grid(row=1, column=1)
        max_input.grid(row=1, column=3)
        result_frame = LabelFrame(frame, width=350, height= 100)
        result_frame.grid(row=4, column=0, columnspan=4, rowspan=2, pady=10)
        result_message = Label(result_frame, text="Game start! \n The explosive number is between %d ~ %d"%(left,right)).pack()
        explosive_num = random.randint(left+1, right-1) 
        guess_num = Entry(frame, width=15, borderwidth=2, state=NORMAL)
        enter_but = Button(frame, text= "Enter", padx=5, pady= 5, command=guess, state=NORMAL)
        guess_num.grid(row=2, column=1,padx=10, pady= 10)
        enter_but.grid(row=2, column=2,padx=10, pady= 10)
        
    else :
        print("something is wrong")
        

def guess():
    
    global left
    global right
    global guess_num
    global result_frame
    global result_message

    renew_result_frame()

    print(explosive_num)
    try:
        num = int(guess_num.get())
    except: 
        result_message = Label(result_frame, text="The number is not int number.\n The explosive number is between %d ~ %d"%(left,right)).pack()

    if num >= right or num <= left:
        result_message = Label(result_frame, text="Guess-num out of the range.\n The explosive number is between %d ~ %d"%(left,right)).pack()
        # pass
    elif num > explosive_num:
        right = num
        result_message = Label(result_frame, text="Next one.\n The explosive number is between %d ~ %d"%(left,right)).pack()
    elif num < explosive_num: 
        left = num
        result_message = Label(result_frame, text="Next one.\n The explosive number is between %d ~ %d"%(left,right)).pack()
    elif num == explosive_num:
        result_message = Label(result_frame, text="!----------------------Boom----------------------!\n You lose!!!!!!!!!!!").pack()
        guess_num = Entry(frame, width=15, borderwidth=2, state=DISABLED)
        enter_but = Button(frame, text= "Enter", padx=5, pady= 5, command=guess, state=DISABLED)
        guess_num.grid(row=2, column=1,padx=10, pady= 10)
        enter_but.grid(row=2, column=2,padx=10, pady= 10)
def renew_result_frame():
    global result_frame

    result_frame = LabelFrame(frame, width=350, height= 100)
    result_frame.grid(row=4, column=0, columnspan=4, rowspan=2, pady=10)

def init_command():

    global min_input, max_input, result_frame, result_message
    min_input = Entry(frame, width=15 ,borderwidth=2, state=NORMAL)
    max_input = Entry(frame, width=15 ,borderwidth=2, state=NORMAL)
    min_input.grid(row=1, column=1)
    max_input.grid(row=1, column=3)
    renew_result_frame()


app = Tk()
app.title("Explosive Number")
app.geometry("600x600")
app.resizable(width=False, height=False)

frame = LabelFrame(app, padx= 5, pady= 5) 
head_img = ImageTk.PhotoImage(Image.open("lib/explosion.png"))

with open("lib/demo.txt", mode="r", encoding="utf-8") as file:
    data = file.read()


# --- Define elements
# First elems
demo_frame = LabelFrame(frame, pady = 30,width= 600, height=300 )
demo_frame.propagate(False)
demo_img = Label(demo_frame, image=head_img, width=100, height=100)
demo = Label(demo_frame, text=data)

# Second elems
min_label = Label(frame, text="Min-num", padx=5, pady=5)
min_input = Entry(frame, width=15 ,borderwidth=2)
max_label = Label(frame, text="Max-num", padx=5, pady=5)
max_input = Entry(frame, width=15, borderwidth=2)
start_but = Button(frame, text="Start", command=start, padx=5, pady=5)

# Third elems
guess_label = Label(frame, text="Guess-num", padx=5, pady=5)
guess_num = Entry(frame, width=15, borderwidth=2, state= DISABLED)
enter_but = Button(frame, text= "Enter", padx=5, pady= 5, state=DISABLED)

# Fourth elems
message_label = Label(frame, text="Message: ")
result_frame = LabelFrame(frame, width=350, height= 100)
result_frame.propagate(False)
init_but = Button(frame, text="Init", padx=10, pady= 10, command=init_command )


# --- Define Position
# First Position 
frame.pack(padx=10, pady=10)
demo_frame.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
demo_img.grid(row=0,column=0)
demo.grid(row=1, column=0)

# Second Position
min_label.grid(row=1, column=0,padx=10, pady= 10)
min_input.grid(row=1, column=1,padx=10, pady= 10)
max_label.grid(row=1, column=2,padx=10, pady= 10)
max_input.grid(row=1, column=3,padx=10, pady= 10)
start_but.grid(row=1, column=4,padx=10, pady= 10)

# Third Position
guess_label.grid(row=2, column=0, padx=10, pady=10)
guess_num.grid(row=2, column=1,padx=10, pady= 10)
enter_but.grid(row=2, column=2,padx=10, pady= 10)

# Fourth Position
message_label.grid(row=3, column=0)
result_frame.grid(row=4, column=0, columnspan=4, rowspan=2, pady=10)
init_but.grid(row=4, column=4)



# Playing
app.mainloop()


        