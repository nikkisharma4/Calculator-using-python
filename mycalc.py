from tkinter import *

screen = Tk()
# it is for title
screen.configure(bg='blue')
screen.title('MY CALC')
# to give width and height we use geometry fuction
# screen.geometry('360x460')
screen.maxsize(width='360', height='500')
screen.minsize(width='360', height='460')

# click function for all button
def click(number):
    global operator
    operator+= str(number)
    txt.set(operator)


def clear(): 
    global operator
    operator=''
    txt.set(operator)   

def equal():
    global operator
    # eval fuction used evaluate expression in string it will perform add mul devide etc
    result = eval(operator)
    operator = str(result)
    txt.set(result)
    
    
# The Tkinter StringVar helps you manage the value of a widget such as a Label or Entry more effectivel
txt = StringVar()
operator=''

# to enter text area button inside the screen we use Entry() function
# bd is border size and bg is background color. justify will give you permission to write from right to left
# Some widgets (like text entry widgets, radio buttons and so on) can be connected directly to application variables by using
enter = Entry(screen, bg='gray', font=('arial' ,20, 'italic bold'), bd='30', justify='right', textvariable=txt)
# to show entry fuction we need to give the row and coloumn size so we have to use grid funcion
#  we use column span so that we can adjust for button just below the text screen
enter.grid(row=0, columnspan=4)
#  for button we use button function and we have to give screen function because we want it inside the screen
#and also text function for text on the button
btn7 = Button(screen, text='7', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('7'), 
              activebackground='red', activeforegroun='white')
# to show button we have to use grid we used row =1 because we want button just below to the text screen
btn7.grid(row=1, column=0)
btn8 = Button(screen, text='8', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('8'),
              activebackground='red', activeforegroun='white')
btn8.grid(row=1, column=1)
btn9 = Button(screen, text='9', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('9'),
              activebackground='red', activeforegroun='white')
btn9.grid(row=1, column=2)
btnmul = Button(screen, text='*', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('*'),
                activebackground='red', activeforegroun='white')
btnmul.grid(row=1, column=3)

btn4 = Button(screen, text='4', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('4'), 
              activebackground='red', activeforegroun='white')
btn4.grid(row=2, column=0)
btn5 = Button(screen, text='5', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('5'),
              activebackground='red', activeforegroun='white')
btn5.grid(row=2, column=1)
btn6 = Button(screen, text='6', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('6'),
              activebackground='red', activeforegroun='white')
btn6.grid(row=2, column=2)
btnsub = Button(screen, text='-', bg='pink', font=('arial', 20, 'italic bold'), bd='25' , command=lambda:click('-'),
                activebackground='red', activeforegroun='white')
btnsub.grid(row=2, column=3)


btn3 = Button(screen, text='3', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('3'),
              activebackground='red', activeforegroun='white')
btn3.grid(row=3, column=0)
btn2 = Button(screen, text='2', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('2'),
              activebackground='red', activeforegroun='white')
btn2.grid(row=3, column=1)
btn1 = Button(screen, text='1', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('1'),
              activebackground='red', activeforegroun='white')
btn1.grid(row=3, column=2)
btnadd = Button(screen, text='+', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('+'),
                activebackground='red', activeforegroun='white')
btnadd.grid(row=3, column=3)


btndot = Button(screen, text='C', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:clear(),
                activebackground='red', activeforegroun='white')
btndot.grid(row=4, column=0)
btnzero = Button(screen, text='0', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('0'),
                 activebackground='red', activeforegroun='white')
btnzero.grid(row=4, column=1)
btnequl = Button(screen, text='=', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:equal(),
                 activebackground='red', activeforegroun='white')
btnequl.grid(row=4, column=2)
btndiv = Button(screen, text='/', bg='pink', font=('arial', 20, 'italic bold'), bd='25', command=lambda:click('/'),
                activebackground='red', activeforegroun='white')
btndiv.grid(row=4, column=3)


# it will show the screen
screen.mainloop()