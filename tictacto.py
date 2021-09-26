import tkinter as tk

xTurn = True
btns = [0,0,0,0,0,0,0,0,0]
"""
positions in the btns array on the game.
0 1 2
3 4 5
6 7 8
"""

def btnEnter(event):
    if (btns[btnPos(event)]==0):
        if (xTurn):
            event.widget.configure(text='X')
        else:
            event.widget.configure(text='O')

def btnLeave(event):
    if (btns[btnPos(event)]==0):
        event.widget.configure(text='')

def btnClick(event):
    if (btns[btnPos(event)]==0):
        global xTurn
        if (xTurn):
            btns[btnPos(event)] = 1
        else:
            btns[btnPos(event)] = 2
        xTurn = not xTurn
    print (btns)

def btnPos(event):
    row = event.widget.grid_info()['row']
    col = event.widget.grid_info()['column']
    index = (row*3)+col
    return index

def checkWin():
    if btns[0]

window = tk.Tk()
window.title('Tic Tac Toe')

window.columnconfigure(0, weight=1, minsize=300)
window.rowconfigure(0, weight=0, minsize=75)
window.rowconfigure(1, weight=1, minsize=300)

controlFrame = tk.Frame(window, background='white')
controlFrame.columnconfigure(0, weight=1, minsize=80)
controlFrame.rowconfigure(0, weight=1, minsize=80)
controlFrame.grid(row=0, column=0, sticky='new')

label = tk.Label(controlFrame, text='label', relief=tk.RAISED)
label.grid(row=0, column=0, sticky='nesw')

gameFrame = tk.Frame(window, background='white')
gameFrame.grid(row=1, column=0, sticky='nesw')

for i in range(3):
    gameFrame.columnconfigure(i, weight=1, minsize=50)
    gameFrame.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        button = tk.Button(gameFrame, relief=tk.RAISED)
        button.grid(row=i, column=j, sticky='nesw')
        button.bind("<Enter>", btnEnter)
        button.bind("<Leave>", btnLeave)
        button.bind("<Button-1>", btnClick)

window.mainloop()
