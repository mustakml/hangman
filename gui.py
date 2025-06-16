import tkinter as tk
from tkinter import messagebox

def spiel_beginnen():
    messagebox.showinfo(
        "Spiel beginnen",
        "Spiel wird begonnen"
    )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("HANGMAN")
    root.geometry("500x200")

    button = tk.Button(
        root,
        text = "Spiel beginnen" , 
        command =spiel_beginnen
    )
    button.pack()
 
    root.mainloop()