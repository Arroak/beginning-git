from   tkinter import *
from math import sqrt as sq
from math import pow 



root = Tk()
root.title('Standard Calculator')


e = Entry(root, width = 50, borderwidth = 3)
e.grid(row=0,column=0,padx=10,pady=5, columnspan=3)

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0,str(current) + str(number))

def button_neg():
	first_num = e.get()
	global f_num
	global math
	math = 'neg'
	f_num = first_num * -1
	
	e.insert(0, first_num * -1)

def button_del():
	e.delete(0)
	
def button_clear():
	e.delete(0, END)



def button_equal():
	second_number = float(e.get())
	e.delete(0, END)
	if math == "addition":
		e.insert(0, f_num + second_number)

	elif math == "subtraction":
		e.insert(0, f_num - int(second_number))

	elif math == "division":
		e.insert(0, round(f_num / int(second_number),4)) 

	elif math == "multiplication":
		e.insert(0, f_num * int(second_number))

	elif math == "exponent":
		e.insert(0, f_num ** int(second_number))

	elif math == "modulus":
		e.insert(0, f_num % int(second_number))

	elif math == "square_root":
		e.insert(sq(0, f_num))

	elif math == "floor_division":
		e.insert(0, f_num // int(second_number))


	elif math == "inverse":
		e.insert(0, pow(f_num,-1))

	elif math == "dot":
		e.insert(0, float(f_num))

	else: 
		e.insert(0,float(f_num))


def button_add(): 
	first_number = e.get()
	global f_num
	global math 
	math = "addition"
	f_num = float(first_number)
	e.delete(0, END)


def button_sub():
	first_number = e.get()
	global f_num
	global math 
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def button_mut():
	first_number = e.get()
	global f_num
	global math 
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)


def button_div():
	first_number = e.get()
	global f_num
	global math 
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)

def button_inv(): 
	first_number = e.get()
	global f_num
	global math 
	math = "inverse"
	f_num = int(first_number)
	e.delete(0, END)

def button_mod(): 
	first_number = e.get()
	global f_num
	global math 
	math = "modulus"
	f_num = int(first_number)
	e.delete(0, END)

def button_exp(): 
	first_number = e.get()
	global f_num
	global math 
	math = "exponent"
	f_num = int(first_number)
	e.delete(0, END)

def button_flr(): 
	first_number = e.get()
	global f_num
	global math 
	math = "floor_division"
	f_num = int(first_number)
	e.delete(0, END)

def button_sqrt(): 
	first_number = e.get()
	global f_num
	global math 
	math = "square_root"
	f_num = int(first_number)
	e.delete(0, END)

def button_dot():
	first_number = e.get()
	global f_num
	global math 
	math = "dot"
	f_num = str(first_number) + "." 
	e.insert(END, '.')





#defining the buttons

#define buttons
button_mod = Button(root, text="%", padx=40,pady=20, bg='grey',fg='black',command =button_mod).grid(row=6, column =0)
button_sqrt = Button(root, text="sqrt", padx=40,pady=20, bg='grey',fg='black',command =button_sqrt).grid(row=6, column =1)
button_exp = Button(root, text="**", padx=40,pady=20, bg='grey',fg='black',command =button_exp).grid(row=6, column =2)
button_inv = Button(root, text="1/x", padx=40,pady=20, bg='grey',fg='black',command =button_inv).grid(row=6, column =3)


button_clear = Button(root, text="clear", padx=40,pady=20,bg='#000fff777',fg='black',command=button_clear).grid(row=2, column =0)
button_div = Button(root, text="/", padx=40,pady=20, bg='grey',fg='black',command =button_div).grid(row=2, column =1)
button_flr = Button(root, text="//", padx=40,pady=20, bg='grey',fg='black',command =button_flr).grid(row=2, column =2)
button_del = Button(root, text="del", padx=40,pady=20, bg='grey',fg='black',command =button_del).grid(row=2, column =3)

button_7 = Button(root, text="7", padx=40,pady=20,bg='green', fg='black',command = lambda: button_click(7)).grid(row=3, column =0)
button_8 = Button(root, text="8", padx=40,pady=20, bg='green',fg='black',command = lambda: button_click(8)).grid(row=3, column =1)
button_9 = Button(root, text="9", padx=40,pady=20, bg='green',fg='black',command = lambda: button_click(9)).grid(row=3, column =2)
button_mut = Button(root, text="*", padx=40,pady=20,bg='grey', fg='black',command =button_mut).grid(row=3, column =3)

button_4 = Button(root, text="4", padx=40,pady=20,bg='green',fg='black', command = lambda: button_click(4)).grid(row=4, column =0)
button_5 = Button(root, text="5", padx=40,pady=20,bg='green',fg='black', command = lambda: button_click(5)).grid(row=4, column =1)
button_6 = Button(root, text="6", padx=40,pady=20,bg='green',fg='black', command = lambda: button_click(6)).grid(row=4, column =2)
button_sub = Button(root, text="-", padx=40,pady=20,bg='grey', fg='black',command =button_sub).grid(row=4, column =3)

button_1 = Button(root, text="1", padx=40,pady=20,bg='green',fg='black', command = lambda: button_click(1)).grid(row=5, column =0)
button_2 = Button(root, text="2", padx=40,pady=20,bg='green',fg='black', command = lambda: button_click(2)).grid(row=5, column =1)
button_3 = Button(root, text="3", padx=40,pady=20,bg='green',fg='black', command = lambda: button_click(3)).grid(row=5, column =2)
button_add = Button(root, text="+", padx=40,pady=20,bg='grey',fg='black', command =button_add).grid(row=5, column =3)


button_neg = Button(root, text="-1", padx=40,pady=20, bg='grey',fg='black',command = button_neg).grid(row=6, column =0)
button_0 = Button(root, text="0", padx=40,pady=20,bg='green',fg='black', command = lambda: button_click(0)).grid(row=6, column =1)
button_dot = Button(root, text=".", padx=40,pady=20,bg='green',fg='black', command = button_dot).grid(row=6, column =2)
button_equal = Button(root, text="=", padx=40,pady=20,bg='grey', fg='black',command =button_equal).grid(row=6, column =3)






root.mainloop()