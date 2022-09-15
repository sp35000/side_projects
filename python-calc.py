#!/usr/bin/python
# coding: utf-8
#import Tkinter as tk
from Tkinter import * 
from numbers import Number

# just as sample, try already validated a and b
def validator(func):
    def validator_nested(a, b):
        if not isinstance(a, Number) or not isinstance(b, Number):
            return 'Digit just numbers.'
        return func(a,b)
    return validator_nested

def calculates():
    which_button = selected_operation.get()
    result=0
    try:
        x = float(entry_field_1.get())
        y = float(entry_field_2.get())
    except ValueError:
	result='Digit just numbers.'
	result_field.delete(0, END)
        result_field.insert(0, result)	
        return False
    if which_button == 1:
        result = add(x,y)
    elif which_button == 2:
        result = subtract(x,y)
    elif which_button == 3:
        result = multiply(x,y)
    elif which_button == 4:
        result = divide(x,y)  
    result_field.delete(0, END)
    result_field.insert(0, result)

@validator
def add(x, y):
    return x + y

@validator
def subtract(x, y):
    return x - y

@validator
def multiply(x, y):
    return x * y

@validator
def divide(x, y):
	try:
		return x / y
	except ZeroDivisionError:
		return('float division by zero.')

root = Tk()
root.title('Python Calc')
window_title = Label(root, text='Python Calc', font=('Helvetica', 18)).grid(row=0, column=0, columnspan=2)
label_1 = Label(root, text='x:').grid(row=1, column=0)
entry_field_1 = Entry(root, text='x', width=10)
entry_field_1.grid(row=1, column=1)
label_2 = Label(root, text='y:').grid(row=2, column=0)
entry_field_2 = Entry(root, text='y', width=10)
entry_field_2.grid(row=2, column=1)
selected_operation = IntVar()
label_3 = Label(root, text='Operation:').grid(row=3, column=0, columnspan=2)
sum_button = Radiobutton(root, text='+', variable=selected_operation, value=1)
sum_button.grid(row=4, column=0)
subtraction_button = Radiobutton(root, text='-', variable=selected_operation, value=2)
subtraction_button.grid(row=4, column=1)
multiplication_button = Radiobutton(root, text='x', variable=selected_operation, value=3)
multiplication_button.grid(row=5, column=0)
division_button = Radiobutton(root, text='/', variable=selected_operation, value=4)
division_button.grid(row=5, column=1)
botao = Button(root, text='OK', command=calculates, width='30').grid(row=6, column=0, columnspan=2)
label_3 = Label(root, text='Result').grid(row=7, column=0)
result_field = Entry(root)
result_field.grid(row=7, column=1)

root.mainloop() 

