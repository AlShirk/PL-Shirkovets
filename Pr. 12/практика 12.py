import tkinter as tk 
import requests 
import json

win=tk.Tk()

win.title("Ширковец Александр Степанович")
win.geometry("160x130+640+300")
win.resizable(False, False)

def user_name():
    UserName=ent1.get()
    url=f"https://api.github.com/users/{UserName}"
    UserData=requests.get(url).json()
    NeedData=("company", "created_at", "email", "id", "name", "url")

    ReData=dict()
    for i in NeedData:
        ReData[i]=UserData.get(i)

    with open(r"D:\PL-Shirkovets\Pr. 12\result.json", "w") as file:
        file.write(json.dumps(ReData, indent=4))


lbl1=tk.Label(win, text="введите имя пользователя")
ent1=tk.Entry(win)
btn1=tk.Button(win,text="Получить JSON\nинформацию", command=user_name)

lbl1.grid(column=0, row=0, padx=5, pady=5)
ent1.grid(column=0, row=1, padx=5, pady=5)
btn1.grid(column=0, row=2, padx=5, pady=5)

win.mainloop()