import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def generate():
    ()

root = Tk()


#frames
slotframe = LabelFrame(root, text="Slot ID")
nameframe = LabelFrame(root, text="Name")
typeframe = LabelFrame(root, text="Type")
hdbidframe = LabelFrame(root, text="HDBID")
priceframe = LabelFrame(root, text="Price (Lore)")
costframe = LabelFrame(root, text="Cost")
giveidframe = LabelFrame(root, text="Give ID")


#Entrys
slot = Entry(slotframe, width=30, justify=CENTER)
name = Entry(nameframe, width=30, justify=CENTER)
loretype = Entry(typeframe, width=30, justify=CENTER)
lorehdbid = Entry(hdbidframe, width=30, justify=CENTER)
loreprice = Entry(priceframe, width=30, justify=CENTER)
cost = Entry(costframe, width=30, justify=CENTER)
commandgiveid = Entry(giveidframe, width=30, justify=CENTER)


#Buttons
generateb = Button(text="Сгенерировать", command='generate')
#b3 = Button(text="Очистить", command='')





#####grid hui znaet

slotframe.pack()
slot.pack()

nameframe.pack()
name.pack()

typeframe.pack()
loretype.pack()

hdbidframe.pack()
lorehdbid.pack()

priceframe.pack()
loreprice.pack()

costframe.pack()
cost.pack()

giveidframe.pack()
commandgiveid.pack()


generateb.pack(side=BOTTOM, padx=5, pady=5)

root.mainloop()



#Unused

#Texts
# slotlabel = Label(slotframe, width=10, text="Slot")
# slotname = Label(nameframe, width=10, text="Name")
# slottype = Label(width=10, text="Type")
# slothdbid = Label(width=10, text="HDBID")
# slotprice = Label(width=10, text="LorePrice")
# slotcost = Label(width=10, text="Cost")
# slotgiveid = Label(width=10, text="GiveID")