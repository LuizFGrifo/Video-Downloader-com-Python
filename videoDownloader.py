from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from pytube.exceptions import RegexMatchError

janela = Tk()
janela.title('Baixe seus videos do YouTube!!!')


def download(link_):
    if link_:
        try:
            pasta = filedialog.askdirectory()
            YouTube(link_).streams.get_highest_resolution().download(pasta)
            aviso()
        except RegexMatchError:
            erro()
    else:
        erro()


def aviso():
    janela_msg = Toplevel()
    janela_msg.title('Video baixado com sucesso!')
    janela_msg.geometry('300x200')

    Label(janela_msg, text='Download concluido!', font='arial 12 bold', pady=30).pack()

    Button(janela_msg, text='Fechar', command=janela_msg.destroy).pack()


def erro():
    janela_msg = Toplevel()
    janela_msg.title('Erro!!!')
    janela_msg.geometry('300x200')

    Label(janela_msg, text='Erro, insira um link válido', font='arial 12 bold', pady=30).pack()

    Button(janela_msg, text='Fechar', command=janela_msg.destroy).pack()

quadro = Frame(janela)
quadro.pack()

Label(quadro, text='Insira o Link do YouTube: ', font='arial 12 bold').pack(side='left')
link = Entry(quadro, font='arial 20', width=50)
link.pack(side='left')

Button(quadro, bg='green', text='Download', bd=1, fg='white', width=9, height=2, command=lambda: download(link.get())).pack()
janela.mainloop()

