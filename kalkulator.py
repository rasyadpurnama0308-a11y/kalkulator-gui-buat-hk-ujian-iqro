import tkinter as tk

def klik(t):
    if t=="C": e.delete(0,"end")
    elif t=="=":
        try:
            h=eval(e.get())
            e.delete(0,"end")
            e.insert(0,h)
        except:
            e.delete(0,"end")
            e.insert(0,"Error")
    else: e.insert("end",t)

r=tk.Tk()
r.title("𝕶𝖆𝖑𝖐𝖚𝖑𝖆𝖙𝖔𝖗")
r.geometry("350x450")
e=tk.Entry(r,font=("Old English Text MT",24),justify="right")
e.grid(row=0,column=0,columnspan=4,sticky="nsew")

for i,t in enumerate("789/456*123-C0=+"):
    tk.Button(r,text=t,font=("Old English Text MT",18),command=lambda x=t:klik(x)).grid(row=i//4+1,column=i%4,sticky="nsew",padx=3,pady=3)

for i in range(5): r.grid_rowconfigure(i,weight=1)
for i in range(4): r.grid_columnconfigure(i,weight=1)

r.mainloop()