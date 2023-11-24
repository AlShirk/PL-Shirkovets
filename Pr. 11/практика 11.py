import tkinter as tk 
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import scrolledtext as st

win=tk.Tk()

win.title("Ширковец Александр Степанович")
win.geometry("500x600+800+100")
win.resizable(True, False)
#////////////////////////////////////////////////////
#--------------------Вкладки-------------------------

tab_control = ttk.Notebook(win)  
tab1 = ttk.Frame(tab_control) 
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)  

tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Файл') 

tab_control.pack(expand=1,fill="both")
#/////////////////////////////////////////////////////
#------------------Калькулятор-------------------------

def CALC():
    a=int(calc1.get())
    b=int(calc2.get())
    znak=spn.get()
    if znak == "+":
        o=a+b
    elif znak == "-":
        o=a-b
    elif znak == "*":
        o=a*b
    elif znak == "/":
        o=a/b
    lbl["text"]=f"{o}"

calc1=tk.Entry(tab1)
spn=Combobox(tab1, values=("+", "-", "*", "/"), width=1)
calc2=tk.Entry(tab1)
btn=tk.Button(tab1, text="Получить ответ", command=CALC)
lbl =tk.Label(tab1,text="")

calc1.grid(column=0, row=0)
spn.grid(column=1, row=0)
calc2.grid(column=2, row=0)
btn.grid(column=0, row=1)
lbl.grid(column=2, row=1)
#/////////////////////////////////////////////////////
#---------------------Чекбоксы------------------------

def show():
    a,b,c=c_bt1_value.get(), c_bt2_value.get(), c_bt3_value.get()
    if a == b == c == "":
            mb.showinfo("Предупреждение", "Вы не выбрали Вариант")
            return
    mb.showinfo("Подтверждение", f"Вы выбрали {a} {b} {c} Вариант")

c_bt1_value = StringVar()
c_bt2_value = StringVar() 
c_bt3_value = StringVar()  

c_bt1=tk.Checkbutton(tab2, text="Первый", variable=c_bt1_value, onvalue="Первый", offvalue="")
c_bt2=tk.Checkbutton(tab2, text="Второй", variable=c_bt2_value, onvalue="Второй", offvalue="")
c_bt3=tk.Checkbutton(tab2, text="Третий", variable=c_bt3_value, onvalue="Третий", offvalue="")
c_btn=tk.Button(tab2, text="Подтвердить выбор", command=show)

c_bt1.grid(column=0, row=0)
c_bt2.grid(column=0, row=1)
c_bt3.grid(column=0, row=2)
c_btn.grid(column=0, row=3)
#/////////////////////////////////////////////////////
#----------------------Файл---------------------------

def download():
    file_name = fd.askopenfilename(filetypes=(("All", "*"), ("Text", "*.txt")))
    with open(file_name, "r", encoding="utf-8") as f:
        txt.insert(INSERT, f.read())
txt=st.ScrolledText(tab3)
menu3 = Menu(win)
win.config(menu=menu3)
file_menu=Menu(menu3,tearoff=0)
file_menu.add_command(label="Загрузить", command=download)
menu3.add_cascade(label='Файл', menu=file_menu) 

txt.pack(expand=1, fill="both")


win.mainloop()