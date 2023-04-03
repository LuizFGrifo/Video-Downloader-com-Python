import os
from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from tkinter import messagebox
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


def downloadAudio(link_):
    if link_:
        try:
            pasta = filedialog.askdirectory()
            mp3 = YouTube(link_).streams.filter(only_audio=True).first()
            download_file = mp3.download(pasta)
            base, ext = os.path.splitext(download_file)
            new_file = base + '.mp3'
            os.rename(download_file, new_file)
            aviso()
        except RegexMatchError:
            erro()
    else:
        erro()


def aviso():
    messagebox.showinfo("Sucesso!", "Download Concluido!")


def erro():
    messagebox.showerror("Erro!", "Erro insira um link válido!")

quadro = Frame(janela)
quadro.pack()

Label(quadro, text='Insira o Link do YouTube: ', font='arial 12 bold').pack(side='left')
link = Entry(quadro, font='arial 20', width=50)
link.pack(side='left')

Button(quadro, bg='green', text='MP4', bd=1, fg='white', width=9, height=2, command=lambda: download(link.get())).pack()
Button(quadro, bg='green', text='MP3', bd=1, fg='white', width=9, height=2, command=lambda: downloadAudio(link.get())).pack(side='bottom')
janela.mainloop()
