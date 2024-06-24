from tkinter import *
from tkinter import messagebox

class Interface():
    def __init__(self, root):
        self.root = root
        self.options = []
        self.red = "#A6243C"
        self.textEntry1 = StringVar()
        self.textEntry2 = StringVar()
        self.config()
        self.entradas()
        self.config_menubutton()
        
    def config(self):
        self.root.title("Sara linda")
        self.root.configure(background = self.red)
        self.root.resizable(False, False)
        self.root.geometry("290x300")
        
    def entradas(self):
        self.label1 = Label(self.root, text = "Endereço IP")
        self.label1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.05)
        
        self.entry1 = Entry(self.root, textvariable = self.textEntry1)
        self.entry1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.05)
        
        self.menubutton = Menubutton(self.root, text = "Máscara", relief = "ridge", cursor = "hand1")
        self.menubutton.place(relx = 0.25, rely = 0.2, relwidth = 0.5, relheight = 0.05)
        
        self.menu = Menu(self.menubutton, tearoff = 0)
        self.menubutton.config(menu = self.menu)
        
        self.entry2 = Entry(self.root, textvariable = self.textEntry2)
        self.entry2.place(relx = 0.25, rely = 0.3, relwidth = 0.5, relheight = 0.05) 
        
        self.button = Button(self.root, text = "Enviar")
        self.button.place(relx = 0.375, rely = 0.4, relwidth = 0.25, relheight = 0.05)
        
        
    def config_menubutton(self):
        i = 0
        while i < 33:
            self.options.append(i)
            i += 1 
        for self.option in self.options:
            self.menu.add_command(label = self.option, command = lambda option = self.option: self.show_message )
        
    def show_message(option):
        messagebox.showinfo("Selecionado", f"Você selecionou: {option}")       

if __name__ == "__main__":
    root = Tk()
    app = Interface(root)
    root.mainloop()