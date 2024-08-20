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

frame = tk.Frame (interface, bg="#000000")
frame.pack(pady=10)

add_tarefa = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30)
add_tarefa.pack(side=tk.LEFT, padx=10)

botao_adicionar = tk.Button(frame, text = "Adiconar Tarefa", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)

#Criar um frame para as tarefas serem adicionadas
frame_lista = tk.Frame(interface, bg="white")
frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_lista, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

barra_scroll = ttk.Scrollbar(frame_lista, orient="vertical", command=canvas.yview)
barra_scroll.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=barra_scroll.set)
canvas_interior = tk.Frame(canvas,bg="white")
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")
canvas_interior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))




interface.mainloop()
