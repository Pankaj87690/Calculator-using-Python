from tkinter import *
import tkinter.messagebox
import random
string=""
r=Tk()
left=Frame(r,width=600,height=650,relief=SUNKEN)
left.pack(side=LEFT)
input_num=StringVar()
txt=Entry(left,font="arial 20 bold",text=input_num,bd=30,width=45,bg="#00BFFF")
txt.grid(columnspan=4)

def press(num):
    global string
    string=string+str(num)
    input_num.set(string)

def evaluate():
    global string
    try:
            total=eval(string)
    except Exception as e:
            tkinter.messagebox.showinfo("Error","Incorrect Input")
            total=0
            clear()
    input_num.set(total)
    string=""

def clear():
    global string
    string=""
    input_num.set(string)

def delete():
    global string
    string=string[:-1]
    input_num.set(string)
    
b1=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="7",bg="green",command=lambda: press(7))
b1.grid(row=3,column=0)    
b2=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="8",bg="green",command=lambda: press(8))
b2.grid(row=3,column=1)    
b3=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="9",bg="green",command=lambda: press(9))
b3.grid(row=3,column=2) 
b4=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="4",bg="green",command=lambda: press(4))
b4.grid(row=4,column=0)
b5=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="5",bg="green",command=lambda: press(5))
b5.grid(row=4,column=1)
b6=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="6",bg="green",command=lambda: press(6))
b6.grid(row=4,column=2)
b7=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="1",bg="green",command=lambda: press(1))
b7.grid(row=5,column=0)
b8=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="2",bg="green",command=lambda: press(2))
b8.grid(row=5,column=1)
b9=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="3",bg="green",command=lambda: press(3))
b9.grid(row=5,column=2)

plus=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="+",bg="yellow",command=lambda: press("+"))
plus.grid(row=4,column=3)

minus=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="-",bg="yellow",command=lambda: press("-"))
minus.grid(row=3,column=3)

into=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="*",bg="yellow",command=lambda: press("*"))
into.grid(row=2,column=3)

b0=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="0",bg="green",command=lambda: press(0))
b0.grid(row=6,column=1)

clear=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="C",bg="red",command=clear)
clear.grid(row=2,column=0)

equal=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,height=4,text="=",bg="blue",command=evaluate)
equal.grid(row=5,column=3,rowspan=2)

percent=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="Mode",bg="blue",command=lambda: press("%"))
percent.grid(row=6,column=0)

divide=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="/",bg="yellow",command=lambda: press("/"))
divide.grid(row=2,column=2)

dot=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text=".",bg="green",command=lambda: press("."))
dot.grid(row=6,column=2)

delete=Button(left,padx=16,pady=8,bd=8,fg="black",font="arial 16 bold",width=10,text="delete",bg="#E03C31",command=delete)
delete.grid(row=2,column=1)

r.mainloop()
