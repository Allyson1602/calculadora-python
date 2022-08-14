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

frame_tela = Frame(janela, width=235, height=50, bg=azul)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

botao_limpar = Button(
    frame_corpo,
    text="C",
    width=11,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_limpar.place(x=0, y=0)

botao_porceto = Button(
    frame_corpo,
    text="%",
    width=5,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_porceto.place(x=118, y=0)

botao_barra = Button(
    frame_corpo,
    text="/",
    width=5,
    height=2,
    bg=laranja,
    fg=branco,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_barra.place(x=177, y=0)

janela.mainloop()
