import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage


#Criar Interface do APP
interface = tk.Tk()
interface.title("Meu Gerenciador de Tarefas")
interface.configure(bg="#F0F0F0")
interface.geometry("475x550")

frame_edicao = None

#Funcao adicionar tarefa
def add_tarefa():
    global frame_edicao

    tarefa = campo_tarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_edicao = None
        else:   
            add_item_tarefa(tarefa)
            campo_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada invalida","Por favor insira uma tarefa!")

def add_item_tarefa(tarefa):
    frame_tarefa = tk.Frame(canvas_interior, bg="white", bd=1, relief=tk.SOLID)

    label_tarefa = tk.Label(frame_tarefa, text=tarefa, font=("Garamond", 16), bg="white", width=25, height=2, anchor="w")
    label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    botao_editar = tk.Button(frame_tarefa, image=icone_editar, command=lambda f=frame_tarefa, l=label_tarefa: preparar_edicao(f, l), bg="white", relief=tk.FLAT)
    botao_editar.pack(side=tk.RIGHT, padx=5)

    botao_excluir = tk.Button(frame_tarefa, image=icone_excluir, command=lambda f=frame_tarefa: deletar_tarefa(f), bg="white", relief=tk.FLAT)
    botao_excluir.pack(side=tk.RIGHT, padx=5)

    frame_tarefa.pack(fill=tk.X, padx=5, pady=5)

    checkbutton = ttk.Checkbutton(frame_tarefa, command=lambda label=label_tarefa: alterar_sublinhado(label))
    checkbutton.pack(side=tk.RIGHT, padx=5)

    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def preparar_edicao(frame_tarefa, label_tarefa):
    global frame_edicao
    frame_edicao = frame_tarefa
    campo_tarefa.delete(0, tk.END)
    campo_tarefa.insert(0, label_tarefa.cget("text"))

def atualizar_tarefa(nova_tarefa):
    global frame_edicao
    for widget in frame_edicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text=nova_tarefa)

def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def alterar_sublinhado(label):
    fonte_atual = label.cget("font")
    if "overstrike" in fonte_atual:
        nova_fonte = fonte_atual.replace(" overstrike", "")
    else:
        nova_fonte = fonte_atual + " overstrike"
    label.config(font=nova_fonte) 


icone_editar = PhotoImage(file="editar.png").subsample(3, 3)
icone_excluir = PhotoImage(file="excluir.png").subsample(3, 3)

fonte_cabecalho = font.Font(family="Garamond", size=24, weight="bold")
rotulo_cabecalho = tk.Label(interface, text="Meu Gerenciador de Tarefas", font=fonte_cabecalho, bg="#F0F0F0", fg="#333").pack(pady=20) 

frame = tk.Frame (interface, bg="#F0F0F0")
frame.pack(pady=10)

campo_tarefa = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30)
campo_tarefa.pack(side=tk.LEFT, padx=10)

botao_adicionar = tk.Button(frame, text="Adicionar Tarefa", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT, command=add_tarefa)
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
