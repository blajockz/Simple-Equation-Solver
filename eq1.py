from math import pow
import tkinter 
import tkinter.messagebox
print("Write an equation in this from : ax + b = 0")
print("________________")
print("Write a specific value for a")
a = float(input())
print("Write a specific value for b")
b = float(input())
if a == 0:
    tkinter.messagebox.showerror(title="Error Equationel", message="a couldn't apply the value 0")
elif a!=0:
    print("The solution of this equation is :")
