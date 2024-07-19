from tkinter import *
from tkinter import ttk

import binaryTree as bt

tree = bt.BinaryTree()

def addValue(nome,canvas):
    tree.add(nome)
    tree.render(canvas)

def printTree():
    tree.showValues()

def moveClosestTo(x,y):
    tree.moveClosestTo(x,y)
    tree.render(canvas)

if __name__ == '__main__':
    def drag(event):
        moveClosestTo(event.x,event.y)
    root = Tk()
    root.title("Arvores Binarias")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    inputes = ttk.Frame(frm)
    inputes.grid()
    ttk.Label(inputes, text="Nome:",padding=10).grid(column=0, row=0)
    nome_input = ttk.Entry(inputes, width=20)
    nome_input.grid(column=1,row=0)
    ttk.Button(inputes, text="Procurar", width=20, command=printTree).grid(column=1, row=1)
    canvas = Canvas(frm, width=600, height=400, background='gray75')
    canvas.grid(column=0,row=1)
    canvas.bind("<B1-Motion>", drag)
    ttk.Button(inputes, text="Adicionar", width=20, command=lambda: addValue(nome_input.get(),canvas)).grid(column=0, row=1)
    root.mainloop()