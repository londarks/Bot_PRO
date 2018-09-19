from tkinter import *
import tkinter as tk
import os
import time
import random
import threading
from functools import partial
import cave_pewter

def bot_cave():
	time.sleep(2)
	t_cave_hut = threading.Thread(target= cave_pewter.bot)
	t_cave_hut.start()

def terminal_th():
	lb = Listbox(root,bg="black",font="18",fg="#07FB00",width=18, height=0)
	lb.pack(side=LEFT,expand=False,fill="both")
	sb = Scrollbar(root)
	sb.pack(side=LEFT,fill="y")
	sb.configure(command=lb.yview)
	lb.configure(yscrollcommand=sb.set)
	while True:
		terminal_txt=open("terminal.txt","r")
		for x in terminal_txt.readlines():
			time.sleep(0.4)
			lb.insert(END,x)
			terminal_txt.close()
			terminal_txt=open("terminal.txt","w")
			terminal_txt.write("")
			terminal_txt.close()




global root
root=tk.Tk()

#imagens#
logo_client = tk.PhotoImage(file="img/logo1.png")
start = tk.PhotoImage(file="img/start.png")
#======================#
#janelas dem cima do programa
principal=Menu(root,fg='white',bg='#202020')
Porteiro_bot=Menu(principal)
#coisas dentro de Porteiro_bot
Porteiro_bot.add_command(label="Informações")
Porteiro_bot.add_command(label="Help")
Porteiro_bot.add_command(label="O")
#logs menu
Logs_bot=Menu(principal)
#coisas dentro de logs
Logs_bot.add_command(label="View logs")
Logs_bot.add_command(label="Clear logs")
#menu em cima da janela V V V
principal.add_cascade(label="Siren-Bot")
principal.add_command(label="Credits")
principal.add_command(label="Help")
principal.add_command(label="Exit")
root.configure(menu=principal)

root.title('Siren-Bot')

root.resizable(width=False, height=False)
#Canvas(root, width=700, height=600, bg='#202020').pack()
root.geometry("500x300+300+20")
#============================#
icon = PhotoImage(file='img/icon.png')
root.tk.call('wm', 'iconphoto', root._w, icon)
#================================#

#======lock img=============#
logo_l = Label(root,width=198, height=111, image=logo_client)
logo_l.place(x=250, y=40)
#=========================#


t_cave_hut = threading.Thread(target= terminal_th)
t_cave_hut.start()

#terminal_txt = open('terminal.txt','r')
#lb = Listbox(root,bg="black",font="18",fg="#07FB00",width=18, height=0)
#lb.pack(side=LEFT,expand=False,fill="both")
#sb = Scrollbar(root)
#sb.pack(side=LEFT,fill="y")
#sb.configure(command=lb.yview)
#lb.configure(yscrollcommand=sb.set)
#while True:
# terminal_txt=open('terminal.txt','r')
# for i in terminal_txt.readlines():
#  lb.insert(END,i)
#  terminal_txt=open("terminal.txt","w")
#  terminal_txt.write("")
#  terminal_txt.close()
#  time.sleep(2)



button_start = Button(root, width=90, height=30,image=start,command=bot_cave)
button_start.place(x=300, y=250)


root["bg"] = "#202020"



root.mainloop()
