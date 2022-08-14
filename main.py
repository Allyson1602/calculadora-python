from tkinter import *
from tkinter import ttk

# cores
preto = "#1e1f1e"
branco = "#feffff"
azul = "#38576b"
cinza = "#eceff1"
laranja = "#ffab40"

# janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=preto)

# output
frame_tela = Frame(janela, width=235, height=50, bg=azul)
frame_tela.grid(row=0, column=0)

# corpo
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# botões
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

botao_sete = Button(
    frame_corpo,
    text="7",
    width=5,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_sete.place(x=0, y=52)

botao_oito = Button(
    frame_corpo,
    text="8",
    width=5,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_oito.place(x=59, y=52)

botao_nove = Button(
    frame_corpo,
    text="9",
    width=5,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_nove.place(x=118, y=52)

botao_asterisco = Button(
    frame_corpo,
    text="*",
    width=5,
    height=2,
    bg=laranja,
    fg=branco,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_asterisco.place(x=177, y=52)

botao_quatro = Button(
    frame_corpo,
    text="4",
    width=5,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_quatro.place(x=0, y=104)

botao_cinco = Button(
    frame_corpo,
    text="5",
    width=5,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_cinco.place(x=59, y=104)

botao_seis = Button(
    frame_corpo,
    text="6",
    width=5,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_seis.place(x=118, y=104)

botao_subtracao = Button(
    frame_corpo,
    text="-",
    width=5,
    height=2,
    bg=laranja,
    fg=branco,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_subtracao.place(x=177, y=104)

botao_um = Button(
    frame_corpo,
    text="1",
    width=5,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_um.place(x=0, y=156)

botao_dois = Button(
    frame_corpo,
    text="2",
    width=5,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_dois.place(x=59, y=156)

botao_tres = Button(
    frame_corpo,
    text="3",
    width=5,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_tres.place(x=118, y=156)

botao_adicao = Button(
    frame_corpo,
    text="+",
    width=5,
    height=2,
    bg=laranja,
    fg=branco,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_adicao.place(x=177, y=156)

botao_zero = Button(
    frame_corpo,
    text="0",
    width=11,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_zero.place(x=0, y=208)

botao_ponto = Button(
    frame_corpo,
    text=".",
    width=5,
    height=2,
    bg=cinza,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_ponto.place(x=118, y=208)

botao_igual = Button(
    frame_corpo,
    text="=",
    width=5,
    height=2,
    bg=laranja,
    fg=branco,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE
)
botao_igual.place(x=177, y=208)

janela.mainloop()
