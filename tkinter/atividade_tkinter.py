import tkinter as tk
from tkinter import messagebox

def classificar():
    nota = float(entry_nota.get())
    if nota == 10:
        resultado.config(text="Parabéns, nota máxima!")
    elif nota >= 9:
        resultado.config(text="Quase perfeito!")
    elif nota <= 4.9:
        resultado.config(text="Reprovado com baixa nota.")
    else:
        resultado.config(text="Nota dentro da média.")

#Janela principal
root = tk.Tk()
root.title("verificador de Nota")
root.geometry("300x200")
root.configure(bg= "#8CEDF0") 

# Widgets
tk.Label(root, text="Digite a nota do aluno", bg="#8CEDF0", fg="black", font=("Arial", 11, "bold")).pack(pady=10)

entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)

botao = tk.Button(root, text="Verificar Nota", command=classificar)
botao.pack(pady=10)

resultado = tk.Label(root, text="", bg="#8CEDF0", font=("Arial", 10, "bold"))
resultado.pack(pady=10)

# Executar a janela
root.mainloop()