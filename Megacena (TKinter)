from random import sample
from tkinter import *

def megacena():

    numbers = list(range(1, 61))

    result = sample(numbers, 6)

    game["text"] = f"""O seu jogo é:
    
{sorted(result)}

Boa sorte!"""


window = Tk()
window.title("Gerador de jogos da mega cena")
window.geometry("400x400")

instruction = Label(window, text="Clique no botão para gerar o seu jogo da mega cena.")
instruction.grid(column=0, row=0, padx=15, pady=15)
instruction.configure(font=("Arial", 12))

tile = Button(window, text="Sortear!", command=megacena)
tile.grid(column=0, row=1, padx=10, pady=10)
tile.configure(font=("Arial", 15))

game = Label(window, text="")
game.grid(column=0, row=2, padx=10, pady=10)
game.configure(font=("Arial", 12))

window.mainloop()
