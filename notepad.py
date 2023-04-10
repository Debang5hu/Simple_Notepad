import tkinter 
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import ttk

mode="light"

def save_file():
    file_name=asksaveasfilename()
    if file_name is not None:
        with open(file_name,"w") as file:
            file.write(code.get(1.0,tkinter.END))


def open_file():
    file_name=askopenfilename()
    if file_name is not None:
        with open(file_name,"r") as file:
            code.delete(1.0,tkinter.END)
            code.insert(1.0,file.read())


def new_file():
    code.delete(1.0,tkinter.END)


def theme_file():
    global mode
    if mode=="light":
        ##36454F
        code.config(background="#555555",fg="black")
        mode="dark"


    else:
        code.config(background="white",fg="black")
        mode="light"
        


#screen
if  __name__ == "__main__":
    screen=tkinter.Tk()
    screen.title("Notepad")

 


#text box
    code=tkinter.Text(screen)
    code.pack(expand=True,fill="both")




#button
    save_btn =tkinter.Button(screen,text ='Save',command = lambda:save_file())
    save_btn.pack(side=tkinter.LEFT,padx=3,anchor=tkinter.N)


    open_btn =tkinter.Button(screen,text ='Open',command = lambda:open_file())
    open_btn.pack(side=tkinter.LEFT,padx=3,anchor=tkinter.N)
    

    new_btn =tkinter.Button(screen,text ='New',command = lambda:new_file())
    new_btn.pack(side=tkinter.LEFT,padx=3,anchor=tkinter.N)

    theme_btn =tkinter.Button(screen,text ='Theme',command = lambda:theme_file())
    theme_btn.pack(side=tkinter.LEFT,padx=3,anchor=tkinter.N)

    





#to run the application
    screen.mainloop()