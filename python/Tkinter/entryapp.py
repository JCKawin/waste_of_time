import tkinter as tk
import csv

def entry():
    text = txt.get()
    if text:
        reg_csv.writerow(text)
        txt.delete(first= 0)
    
reg = open("Tkinter\\register.csv" , 'w')
reg_csv = csv.writer(reg)

root  = tk.Tk()
root.columnconfigure(0 , weight=1)
root.rowconfigure(0 , weight= 1)
root.title("JCKawin")
root.config(background="black")
root.geometry('300x400')

txt = tk.Entry()
txt.grid(column=0 , row= 0  , sticky="new")
frame = tk.Frame(root)
frame.grid(row=1 , column=0 , sticky="news")


btn = tk.Button(root , text= "enter" , command= entry)
btn.grid(row=2 ,columnspan=3)

root.mainloop()

