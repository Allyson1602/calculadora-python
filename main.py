from tkinter import *
from tkinter import ttk

# cores
preto = "#1e1f1e"
branco = "#feffff"
azul = "#38576b"
cinza = "#eceff1"
laranja = "#ffab40"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=preto)

frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)

janela.mainloop()
