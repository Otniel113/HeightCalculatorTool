from tkinter import *

main = Tk()
main.title("Height Calculator Tool")
main.geometry("300x75")

def open_popup():
   height = ent.get()
   top= Toplevel(main)
   top.title("Result")
   top.geometry("200x60")
   Label(top, text= "Your height is " + height + " cm!").pack()

Label(main, text='Input your height: ').grid(row=0, column=0, padx=5, pady=5)

ent = Entry(main)
ent.grid(row=0, column=1, padx=5, pady=5)

Label(main, text='cm').grid(row=0, column=2, padx=5, pady=5)

btn = Button(main, text="Enter", command=open_popup).grid(row=1, column=1, padx=5, pady=5)

main.mainloop()