from tkinter import *

def geti():
    value=Lb.curselection()
    stckname=Lb.get(value)


    va={'stckname':stckname}
    exec(open('da.py').read(),va)

m=Tk()

m.title('hello')
Label( text='Choose the option').grid(row=0)

Lb = Listbox(m,selectmode=SINGLE) 
Lb.insert(1, 'Facebook') 
Lb.insert(2, 'Instagram') 
Lb.insert(3, 'Whatsapp')
Lb.insert(4, 'twitter')
Lb.insert(5, 'WeChat')
Lb.insert(6, 'Snapchat')
Lb.insert(7, 'Tinder')
Lb.insert(8, 'Tik Tok')
Lb.insert(9, 'Vmate')
Lb.insert(10, 'Youtube')



w=Button(text='Submit',width=25,command=geti)
Lb.grid()
          
w.grid()
m.mainloop()
