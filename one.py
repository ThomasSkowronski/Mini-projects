def app():
    print ('What would you like to do?')

    ins = input('''
0: exit
1: calculate the seconds in a number of days
2: reverse a string

''')
    if ins=='1':
        secondsDays()
    elif ins=='0':
        return
    elif ins=='2':
        strReverse()
    else:
        app()

def secondsDays():
    days = input('how many days? ')
    seconds = int(days)*24*60*60

    print (str(seconds)+(' seconds in ')+days+(' days.'))
    app()

def strReverse():
    st=input ('string to reverse: ')
    out=st[::-1]
    print (out)
    app()

app()
