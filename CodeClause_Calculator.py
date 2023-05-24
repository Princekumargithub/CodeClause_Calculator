from tkinter import *


def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = float(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    elif text == "⌫":
        value = scvalue.get()
        n=len(scvalue.get())
        value1 = value[0:n-1:1]
        scvalue.set(value1)
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


prince_cal = Tk()
prince_cal.title('Prince Calculator')
prince_cal.geometry('500x300')

scvalue = StringVar()
scvalue.set("")

screen = Entry(prince_cal, textvar=scvalue, font=("lucida 20 bold"))
screen.pack(fill='x', ipadx=10, padx=20, pady=20)

f1 = Frame(prince_cal, bg='#FAEBD7')
b = Button(f1, text="C", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="%", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="⌫",fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="/", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

f1.pack()

f1 = Frame(prince_cal, bg='#FAEBD7')
b = Button(f1, text="7", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="8", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="9", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="*", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

f1.pack()

f1 = Frame(prince_cal, bg='#FAEBD7')
b = Button(f1, text="4", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="5", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="6", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="-", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

f1.pack()

f1 = Frame(prince_cal, bg='#FAEBD7')
b = Button(f1, text="1", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="2", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="3", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="+", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

f1.pack()

f1 = Frame(prince_cal, bg='#FAEBD7')
b = Button(f1, text="0", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="00", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text=".", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f1, text="=", fg='black', bg='yellow', height=1, width=7, font=("lucida 13 bold"))
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

f1.pack()
prince_cal.mainloop()