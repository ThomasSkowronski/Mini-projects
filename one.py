import os

def app():
    print ('What would you like to do?')

    ins = input('''
0: exit
1: calculate the seconds in a number of days
2: reverse a string
3: ping google and append a log file

''')
    if ins=='1':
        secondsDays()
    elif ins=='0':
        return
    elif ins=='2':
        strReverse()
    elif ins=='3':
        pingGoogle()
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

def pingGoogle():
    os.system('ping google.com -c 5 > log.txt')
    app()

app()
