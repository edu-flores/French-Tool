"""Herramienta para facilitar mi redacción en francés (25/03/2020)"""

import tkinter as tk

gui = tk.Tk() #Abrir ventana
gui.title("FrenchTool.py") #Título
gui.geometry("470x70") #Tamaño
gui.resizable(0, 0) #No se puede cambiar de tamaño
gui.wm_attributes("-topmost", True) #No se puede minimizar 

main_label = tk.Label(gui, text = "Press Desirable Character... ", font = ("Times New Roman", "17"))
main_label.grid(row = 1, column = 3, columnspan = 7)

def CopyChar(character):
	gui.clipboard_clear()
	gui.clipboard_append(character)

à_button = tk.Button(gui, text = "à", font = ("Arial", "15"), command = lambda:CopyChar("à"), width = 3, height = 1) #Si no usas lambda la función corre aunque no presiones el botón. TIL.
à_button.grid(row = 2, column = 1)

è_button = tk.Button(gui, text = "è", font = ("Arial", "15"), command = lambda:CopyChar("è"), width = 3, height = 1)
è_button.grid(row = 2, column = 2)

ù_button = tk.Button(gui, text = "ù", font = ("Arial", "15"), command = lambda:CopyChar("ù"), width = 3, height = 1)
ù_button.grid(row = 2, column = 3)

â_button = tk.Button(gui, text = "â", font = ("Arial", "15"), command = lambda:CopyChar("â"), width = 3, height = 1)
â_button.grid(row = 2, column = 4)

ê_button = tk.Button(gui, text = "ê", font = ("Arial", "15"), command = lambda:CopyChar("ê"), width = 3, height = 1)
ê_button.grid(row = 2, column = 5)

î_button = tk.Button(gui, text = "î", font = ("Arial", "15"), command = lambda:CopyChar("î"), width = 3, height = 1)
î_button.grid(row = 2, column = 6)

ô_button = tk.Button(gui, text = "ô", font = ("Arial", "15"), command = lambda:CopyChar("ô"), width = 3, height = 1)
ô_button.grid(row = 2, column = 7)

û_button = tk.Button(gui, text = "û", font = ("Arial", "15"), command = lambda:CopyChar("û"), width = 3, height = 1)
û_button.grid(row = 2, column = 8)

æ_button = tk.Button(gui, text = "æ", font = ("Arial", "15"), command = lambda:CopyChar("æ"), width = 3, height = 1)
æ_button.grid(row = 2, column = 9)

œ_button = tk.Button(gui, text = "œ", font = ("Arial", "15"), command = lambda:CopyChar("œ"), width = 3, height = 1)
œ_button.grid(row = 2, column = 10)

ç_button = tk.Button(gui, text = "ç", font = ("Arial", "15"), command = lambda:CopyChar("ç"), width = 3, height = 1)
ç_button.grid(row = 2, column = 11)

gui.mainloop() #Para que se quede abierto