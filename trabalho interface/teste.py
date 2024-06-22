import tkinter as tk
from tkinter import messagebox

# Função para exibir uma mensagem quando uma opção do menu é selecionada
def show_message(option):
    messagebox.showinfo("Selecionado", f"Você selecionou: {option}")

# Criação da janela principal
window = tk.Tk()
window.title("Exemplo de MenuButton")
window.geometry("300x200")  # Largura x Altura

# Criação de um Menubutton
menubutton = tk.Menubutton(window, text="Opções", relief=tk.RAISED)
menubutton.grid(pady=20)

# Criação do Menu
menu = tk.Menu(menubutton, tearoff=0)
menubutton.config(menu=menu)

# Adicionando opções ao menu
menu.add_command(label="Opção 1", command=lambda: show_message("Opção 1"))
menu.add_command(label="Opção 2", command=lambda: show_message("Opção 2"))
menu.add_command(label="Opção 3", command=lambda: show_message("Opção 3"))

# Iniciar o loop principal da interface
window.mainloop()
