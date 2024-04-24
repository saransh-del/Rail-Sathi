from tkinter import*
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0,END)
    textget = change(text = msg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)







root = Tk()
root.title("Translator")
root.geometry("500x700")  #box_sizing 
root.config(bg='lightblue')     #backgroud_color

lab_txt=Label(root,text="Translator",font=("Time New Roman",40,"bold"))#heading_decoratives
lab_txt.place(x=100,y=40,height=50,width=300)#place_of_placing_heading

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="black",bg='lightblue')#heading_decoratives
lab_txt.place(x=100,y=100,height=20,width=300)#place_of_placing_heading


Sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=200,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=340,height=40,width=150)
comb_sor.set("English")

button_change = Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=340,height=40,width=150)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=340,height=40,width=150)
comb_dest.set("English")

lab_txt=Label(root,text="Destination Text",font=("Time New Roman",20,"bold"),fg="black",bg='lightblue')#heading_decoratives
lab_txt.place(x=100,y=390,height=20,width=300)#place_of_placing_heading


dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=420,height=200,width=480)






root.mainloop()
