from tkinter import*

def fun():

    print("you clicked the button")
    
root = Tk()
label_1 = Label(root, text = "Name")
label_1.grid(row = 0, column = 0)

entry_1 = Entry(root)
entry_1.grid(row = 0,column = 1)

label_2 = Label(root, text = "Email")
label_2.grid(row = 1, column = 0)

entry_2 = Entry(root)
entry_2.grid(row = 1,column = 1)

button_1 = Button(root, text = "Click",command = fun)
button_1.grid(row = 2, columnspan = 2, column = 0)
