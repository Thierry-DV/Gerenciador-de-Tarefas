import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage


#Criar Interface do APP
interface = tk.Tk()
interface.title("Meu Gerenciador de Tarefas")
interface.configure(bg="#000000")
interface.geometry("550x650")

fonte_cabecalho = font.Font(family="Garamond", size=24, weight="bold")
rotulo_cabecalho = tk.Label(interface, text="Meu Gerenciador de Tarefas", font=fonte_cabecalho, bg="#000000", fg="#F0F0F0").pack(pady=20) 

frame = tk.Frame (interface, bg="#000000").pack(pady=10)

add_tarefa = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30)
add_tarefa.pack(side=tk.LEFT, padx=10)

botao_adicionar = tk.Button(frame, text = "Adiconar Tarefa", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)

interface.mainloop()
