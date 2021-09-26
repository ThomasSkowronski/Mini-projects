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
    checkWin()
    print (btns)

def btnPos(event):
    row = event.widget.grid_info()['row']
    col = event.widget.grid_info()['column']
    index = (row*3)+col
    return index

def checkWin():
    row1 = btns[0]*btns[1]*btns[2]
    row2 = btns[3]*btns[4]*btns[5]
    row3 = btns[6]*btns[7]*btns[8]

    col1 = btns[0]*btns[3]*btns[6]
    col2 = btns[1]*btns[4]*btns[7]
    col3 = btns[2]*btns[5]*btns[8]

    dia1= btns[0]*btns[4]*btns[8]
    dia2 = btns[2]*btns[4]*btns[6]

    if 1 in {row1,row2,row3,col1,col2,col3,dia1,dia2}:
        print('X wins')
        resetGame()
    elif 8 in {row1,row2,row3,col1,col2,col3,dia1,dia2}:
        print('O wins')
        resetGame()

def resetGame():
    for k in range(9):
        btns[k] = 0
    global xTurn
    xTurn = True

    global gameFrame
    gameFrame.destroy()

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
