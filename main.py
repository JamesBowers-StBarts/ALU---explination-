from tkinter import *

def move_frame(direction_number):
    global current_frame
    current_frame = current_frame + direction_number
    if current_frame == 3:
        current_frame =0
    elif current_frame == -1:
        current_frame =2
    selected_frame = frames_list[current_frame]
    selected_frame.tkraise()

root =Tk()

top_frame = Frame(root, bg = "Grey")
top_frame.grid(row=0,column=0,sticky=E+W+S+N)
menu_label = Label(top_frame,text="MAIN MENU", bg = "Grey")
menu_label.config(font=(40))
menu_label.grid(row=0,column=1)


content_frame3 = Frame(root, bg = "white")
content_frame3.grid(row=1,column=0,sticky=E+W+S+N)
title1=Label(text="Arithmetic operations")
title1.grid(content_frame3,row=0,column=0)

content_frame2 = Frame(root, bg = "blue")
content_frame2.grid(row=1,column=0,sticky=E+W+S+N)

content_frame1 = Frame(root, bg = "black")
content_frame1.grid(row=1,column=0,sticky=E+W+S+N)


forward_button = Button(top_frame, text="<---",bg = "Grey",command = lambda: move_frame(1))
forward_button.grid(row=1,column=0,pady=(10,10),sticky="ESNW")
back_button = Button(top_frame, text="--->",bg = "Grey",command = lambda: move_frame(-1))
back_button.grid(row=1,column=2,pady=(10,10),sticky="ESNW")

current_frame = 0
frames_list = [content_frame1,content_frame2,content_frame3]

root.rowconfigure(0,minsize = 100,weight=0)
root.rowconfigure(1,minsize = 400,weight=1)
root.columnconfigure(0,minsize = 500,weight=1)


content_frame1.columnconfigure(0,minsize = 200,weight=1)
content_frame1.rowconfigure(0,minsize = 200)
top_frame.columnconfigure(1,minsize = 700,weight=1)
top_frame.columnconfigure(0,minsize = 75)
top_frame.columnconfigure(2,minsize = 75)


root.mainloop()





