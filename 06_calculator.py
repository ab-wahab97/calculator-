from tkinter import *

root=Tk()
root.title('CALCULATOR')
root.iconbitmap('images\\calc.ico')


e=Entry(root,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=20,pady=10)

def clickaction(number):
    current=e.get()
    e.delete(0,END)


    e.insert(0,current+str(number))
    
def clear_button():
    e.delete(0,END)

def add_button(a):
    
    global number1,sign
    sign=1
    number1=a
    e.delete(0,END)

def mul_button(b):
    
    global number1,sign
    sign=2
    number1=b
    e.delete(0,END)      

def div_button(c):
    
    global number1,sign
    sign=3
    number1=c
    e.delete(0,END)  

def sub_button(d):
    
    global number1,sign
    sign=4
    number1=d
    e.delete(0,END)  


def equal_button():
    if sign==1:
     number2=e.get()
     e.delete(0,END)
     answer=int(number1)+int(number2)
     e.insert(0,answer)

    elif sign==2:
     number2=e.get()
     e.delete(0,END)
     answer=int(number1)*int(number2)
     e.insert(0,answer)

    elif sign==3:
     number2=e.get()
     e.delete(0,END)
     answer=int(number1)/int(number2)
     e.insert(0,answer)

    elif sign==4:
     number2=e.get()
     e.delete(0,END)
     answer=int(number1)-int(number2)
     e.insert(0,answer)






button_1=Button(root,text='1',padx=40,pady=10,command=lambda:clickaction(1),borderwidth=5,bg='#c8f1d6')
button_2=Button(root,text='2',padx=40,pady=10,command=lambda:clickaction(2),borderwidth=5,bg='#c8f1d6')
button_3=Button(root,text='3',padx=40,pady=10,command=lambda:clickaction(3),borderwidth=5,bg='#c8f1d6')
button_4=Button(root,text='4',padx=40,pady=10,command=lambda:clickaction(4),borderwidth=5,bg='#c8f1d6')
button_5=Button(root,text='5',padx=40,pady=10,command=lambda:clickaction(5),borderwidth=5,bg='#c8f1d6')
button_6=Button(root,text='6',padx=40,pady=10,command=lambda:clickaction(6),borderwidth=5,bg='#c8f1d6')
button_7=Button(root,text='7',padx=40,pady=10,command=lambda:clickaction(7),borderwidth=5,bg='#c8f1d6')
button_8=Button(root,text='8',padx=40,pady=10,command=lambda:clickaction(8),borderwidth=5,bg='#c8f1d6')
button_9=Button(root,text='9',padx=40,pady=10,command=lambda:clickaction(9),borderwidth=5,bg='#c8f1d6')
button_0=Button(root,text='0',padx=40,pady=10,command=lambda:clickaction(0),borderwidth=5,bg='#c8f1d6')
button_add=Button(root,text='+',padx=90,pady=10,command=lambda:add_button(int(e.get())),borderwidth=8,bg='skyblue')
button_clear=Button(root,text='clear',padx=32,pady=10,command=clear_button,borderwidth=8,bg='red')
button_equal=Button(root,text='=',padx=90,pady=10,command=equal_button,borderwidth=8,bg='yellow')
button_multiply=Button(root,text='x',padx=40,pady=10,command=lambda:mul_button(int(e.get())),borderwidth=8,bg='skyblue')
button_divide=Button(root,text='/',padx=40,pady=10,command=lambda:div_button(int(e.get())),borderwidth=8,bg='skyblue')
button_subtract=Button(root,text='-',padx=40,pady=10,command=lambda:sub_button(int(e.get())),borderwidth=8,bg='skyblue')




button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1,columnspan=2)
button_clear.grid(row=6,column=0,columnspan=1)
button_equal.grid(row=6,column=1,columnspan=2)
button_multiply.grid(row=5,column=0)
button_divide.grid(row=5,column=1)
button_subtract.grid(row=5,column=2)



root.mainloop()