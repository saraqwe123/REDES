from tkinter import *
from tkinter import messagebox

class Interface():
    def __init__(self, root):
        self.root = root
        self.options = []
        self.red = "#A6243C"
        self.white = "#F2F2F2"
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
        self.label1 = Label(self.root, text = "Endereço IP", bg = self.red, fg = self.white, font = ("Arial", 10, "bold"))
        self.label1.place(relx = 0.25, rely = 0.05, relwidth = 0.5, relheight = 0.05)
        
        self.entry1 = Entry(self.root, textvariable = self.textEntry1)
        self.entry1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.05)
        
        self.menubutton = Menubutton(self.root, text = "Máscara", relief = "ridge", cursor = "hand1")
        self.menubutton.place(relx = 0.25, rely = 0.25, relwidth = 0.5, relheight = 0.05)
        
        self.menu = Menu(self.menubutton, tearoff = 0)
        self.menubutton.config(menu = self.menu)
        
        self.label2 = Label(self.root, text = "Quantidade de hosts", bg = self.red, fg = self.white, font = ("Arial", 10, "bold"))
        self.label2.place(relx = 0.25, rely = 0.35, relwidth = 0.5, relheight = 0.05)
        
        self.entry2 = Entry(self.root, textvariable = self.textEntry2)
        self.entry2.place(relx = 0.25, rely = 0.4, relwidth = 0.5, relheight = 0.05) 
        
        self.button = Button(self.root, text = "Enviar", cursor = "hand1", command = self.open_new)
        self.button.place(relx = 0.375, rely = 0.5, relwidth = 0.25, relheight = 0.05)
        
        
    def config_menubutton(self):
        i = 0
        while i < 33:
            self.options.append(i)
            i += 1 
        for self.option in self.options:
            self.menu.add_command(label = self.option, command = lambda op = self.option: self.show_message(op))
        
    def open_new(self):
        texto1 = self.textEntry1.get()
        texto2 = self.textEntry2.get()
        select = self.op
        if texto1 != "" and texto2 != "":
            if len(texto1) <= 12 and len(texto2) <= 12 and select != "":
                root2 = Tk()
                root2.mainloop()
            else:
                messagebox.showinfo("Erro", "Uma das opções não foi selecionada")
        else:
            messagebox.showinfo("Erro", "Uma das opções está vázia")

    
    
    def show_message(self, op):
        self.op = op
        messagebox.showinfo("Selecionado", f"Você selecionou: {self.op}")       

    
class SegundaInterface():
    def __init__(self, root2, interface):
        self.interface = interface
        self.root2 = root2
        
if __name__ == "__main__":
    root = Tk()
    app = Interface(root)
    root.mainloop()
    
"""
no open new, fazer verificação de:
- números, ele não poderá funcionar com letras
- validação de pontos, ele terá que funcionar 111.111.111.111
- validação dos números até 255  
"""