#!/usr/bin/python3

from sys import platform
from tkinter import *
from tkinter import messagebox, ttk, scrolledtext
import nmap

root = Tk()
root.title("nmap-for")
root.minsize(900,800)


#################################################################################################################

#detection os
if platform == "linux" or platform == "linux2":
    os = "shell"

elif platform == "darwin":
    os = "shell"

elif platform == "win32":
    os = "cmd"

#################################################################################################################

def propos():
   messagebox.showinfo("About", "NMAP Helper V0.1, by Sparda")

def quit():
    if messagebox.askokcancel("QUIT", "Do you want to exit ?"):
        root.quit()

def action(event):
    
    # Obtenir l'élément sélectionné
    select = listeCombo.get()
    print("Vous avez sélectionné : ", select,)
 
def alert():
    showinfo("alerte", "Bravo!")

def T3():

   messagebox.showinfo ("WARNING", "Réglages par défaut")


def T5():

   messagebox.showinfo ("WARNING", "Be careful, T5 scan are too aggressive")

#################################################################################################################

menubar = Menu(root)

#Menu 1
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Open", command=alert)
menu1.add_command(label="Save as...", command=alert)
menu1.add_separator()
menu1.add_command(label="Exit", command=quit)  
menubar.add_cascade(label="File", menu=menu1, font=("arial", 10))


#Menu 2
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="About", command = propos)
menubar.add_cascade(label="Help", menu=menu2, font=("arial", 10))

#################################################################################################################

# label ip publique
from requests import get
ip = get('https://api.ipify.org').text
label = Label(root, text="IP Publique = " + str(ip), font=("arial", 12))
#if str(ip) = 
label.config(bg="white")
label.place(x=20, y=10)

#################################################################################################################


# Variable IP Cible
labelcible = Label(root, text="Cible: ", font=("arial", 12))
labelcible.place(x=270, y=10)
ipvic = StringVar(root, value="IP Cible")
# INPUT IP Cible
entréevic = Entry (root, textvariable=ipvic, font=("arial", 12))
entréevic.place(x=320, y=10)

#################################################################################################################

# Liste scan prédéfinis
listeProduits=["scan reconnaissance", "scan normal","scan intense","scan Xmas"]
#Création de la Combobox via la méthode ttk.Combobox()
listeCombo = ttk.Combobox(root, values=listeProduits, font=("arial", 12))
#Choisir l'élément qui s'affiche par défaut
listeCombo.current(0)
listeCombo.place(x=600, y=10)
listeCombo.bind("<<ComboboxSelected>>", action)

#################################################################################################################


#Bouton SCAN

scan = Button(root, text ="scan", font=("arial", 12))
scan.config(bg="white")
scan.place(x=830, y=5)



#INPUT Commande NMAP

commandenmap = Label(root, text="Commande: ", font=("arial", 12))
commandenmap.place(x=20, y=50)

inputcommande = Entry (root, font=("arial", 12), width=80)
inputcommande.place(x=150, y=50)


#################################################################################################################

#################################################################################################################

#OPTIONS NMAP


#Frame Options Agressivité

lframe = LabelFrame(root, text="Scan Timing", font=("arial", 12), bd=3)
lframe.place(x=20, y=90, height=160,width=300)


c1 = Radiobutton (root, text = "T1",justify = LEFT)
c1.place(x=40, y= 120)

c2 = Radiobutton (root, text = "T2",justify = LEFT)
c2.place(x=40, y= 160)

c3 = Radiobutton (root, text = "T3",justify = LEFT, command=T3)
c3.place(x=140, y= 120)

c4 = Radiobutton (root, text = "T4",justify = LEFT)
c4.place(x=140, y= 160)

c4 = Radiobutton (root, text = "T5",justify = LEFT, command=T5)
c4.place(x=40, y= 200)


#################################################################################################################
#################################################################################################################


#Frame SCAN TYPE

exportframe = LabelFrame(root, text="Scan Type", font=("arial", 12), bd=3)
exportframe.place(x=340, y=90, height=160,width=240)

c5 = Radiobutton (root, text = "TCP")
c5.place(x=350, y= 120)


c6 = Radiobutton (root, text = "UDP")
c6.place(x=350, y= 160)

c7 = Radiobutton (root, text = "ARP")
c7.place(x=350, y= 200)


#################################################################################################################
#################################################################################################################


#FRAME TOP Ports

portframe = LabelFrame(root, text="Top-ports", font=("arial", 12), bd=3)
portframe.place(x=600, y=90, height=160,width=276)

c8 = Radiobutton (root, text = "1-100", justify = LEFT)
c8.place(x=610, y= 120)


c9 = Radiobutton (root, text = "1-1000", justify = LEFT)
c9.place(x=610, y= 160)


#################################################################################################################
#################################################################################################################

#SI Industriel

indusframe = LabelFrame(root, text="SI Industriel", font=("arial", 12), bd=3)
indusframe.place(x=20, y=260, height=60,width=600)

c10 = Radiobutton (root, text = "Check this button if audited network is IE Type (Industrial Ethernet)", justify = LEFT)
c10.place(x=40, y= 285)



#################################################################################################################
#################################################################################################################

#OUTPUT & FINDINGS

#Frame Output

outputnmap = LabelFrame(root, text="Output", font=("arial", 12), bd=3)
outputnmap.place(x=20, y=330, height=300,width=800)
outputTXT = scrolledtext.ScrolledText(outputnmap)
outputTXT.place(x= 30, y=10, width=740)
outputTXT.config(bg="white")

#Frame CVE

CVE = LabelFrame(root, text="CVE findings", font=("arial", 12), bd=3)
CVE.place(x=20, y=680, height=300,width=800)
CVETXT = scrolledtext.ScrolledText(CVE)
CVETXT.place(x= 30, y=10, width = 740)
CVETXT.config(bg="white")


#################################################################################################################
#################################################################################################################
#################################################################################################################

root.config(menu=menubar)
root.mainloop()
