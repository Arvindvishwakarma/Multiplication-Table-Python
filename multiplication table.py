from tkinter import *

def MulTable():
    print("\n")
    print("Table")
    for x in range(1,11):
        m = int(EnterTable.get())
        print((x), 'once the', (m), '=', (x*m))


win = Tk()
win.geometry('200x200')
win.title('Multiplication Table')

EnterTable = StringVar()



label = Label(win, text='Table', font=30, fg='Black')
label.grid(row=1,column=6)

label = Label(win, text='                          ')
label.grid(row=2,column=6)

entry = Entry(win, textvariable=EnterTable, justify='center')
entry.grid(row=2,column=6)

button = Button(win, text='Table', command=MulTable)
button.grid(row=5,column=6)

label = Label(win, text='                          ')
label.grid(row=4,column=6)


QUIT=Button(win, text='Exit', command=win.destroy)
QUIT.grid(row=6,column=6)


win.mainloop()

