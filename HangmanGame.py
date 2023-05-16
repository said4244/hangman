import tkinter as tk
from tkinter import messagebox
import random


class Hangman:

    def __init__(self, root):
        with open("easywords.txt") as f:
            self.words = f.read().splitlines() 
        self.word = random.choice(self.words) #random word is chosen here
        self.root = root
        root.title("Hangman")
        root.geometry('400x150')

        #Menu
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        
        self.sub_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="|||", menu=self.sub_menu)
        self.sub_menu.add_command(label="Settings", command=self.show_settings)
        self.sub_menu.add_command(label="Main Page", command=self.show_main_page)
        
        #Main Page
        self.main_page = tk.Frame(root)
        self.main_page.pack(side="top", fill="both", expand=True)
        
        self.label = tk.Label(self.main_page, text="Guess the word:")
        self.label.pack()
        
        self.guessed_word = tk.Label(self.main_page, text="_ " * len(self.word))#putting underscores for the word
        self.guessed_word.pack()
        
        self.entry = tk.Entry(self.main_page) #an entry for the input
        self.entry.pack()
        
        self.button = tk.Button(self.main_page, text="Guess", command=self.guess) #a button that calls the function guess
        self.button.pack()

        self.incorrect_label = tk.Label(self.root) #displays the incorrect guessed letters
        self.incorrect_label.pack()
        
        self.incorrect_guesses = 0
        self.incorrect_letters = [] 
        self.correct_letters = []

        #settings page
        self.settings_page = tk.Frame(root, bg="white")

        self.easy_button = tk.Button(self.settings_page, text="Easy", command=self.easy)
        self.easy_button.pack()

        self.medium_button = tk.Button(self.settings_page, text="Medium", command=self.medium) 
        self.medium_button.pack()

        self.hard_button = tk.Button(self.settings_page, text="Hard", command=self.hard) 
        self.hard_button.pack()
        
    #switch to easy words
    def easy(self):
        with open("easywords.txt") as f: 
            self.words = f.read().splitlines()
        self.word = random.choice(self.words)
        self.guessed_word.config(text="_ " * len(self.word))
        self.incorrect_guesses = 0
        self.incorrect_letters = []
        self.correct_letters = []
        self.update_incorrect_letters()
        self.show_main_page()

    #switch to medium words
    def medium(self):
        with open("mediumwords.txt") as f: 
            self.words = f.read().splitlines()
        self.word = random.choice(self.words)
        self.guessed_word.config(text="_ " * len(self.word))
        self.incorrect_guesses = 0
        self.incorrect_letters = []
        self.correct_letters = []
        self.update_incorrect_letters()
        self.show_main_page()

    #switch to hard words
    def hard(self):
        with open("hardwords.txt") as f: 
            self.words = f.read().splitlines()
        self.word = random.choice(self.words)
        self.guessed_word.config(text="_ " * len(self.word))
        self.incorrect_guesses = 0
        self.incorrect_letters = []
        self.correct_letters = []
        self.update_incorrect_letters()
        self.show_main_page()

    #checking user input
    def guess(self):
        letter = self.entry.get().lower() #gets the input from the entry, and makes it lower to also accept captial entries
        if letter in self.word:
            self.correct_letters.append(letter)
            self.display_word()
        else:
            if letter in self.incorrect_letters: #if already guessed, ignore
                pass
            else:
                self.incorrect_letters.append(letter)
                self.incorrect_guesses += 1
            self.update_incorrect_letters() #calls the update_incorrect_letters
        
        self.entry.delete(0, 'end') #deletes the letters in the entry
        if "_" not in self.guessed_word["text"]: #checks if the whole word is guessed
            messagebox.showinfo("Congratulations!", "You guessed the word correctly!")
            self.reset_game()
        elif self.incorrect_guesses == 6:
            messagebox.showerror("Error", "You lost the game! The word was {}".format(self.word))
            self.reset_game()

    #play again
    def reset_game(self):
        self.word = random.choice(self.words)
        self.guessed_word.config(text="_ " * len(self.word))
        self.incorrect_guesses = 0
        self.incorrect_letters = []
        self.correct_letters = []
        self.update_incorrect_letters()


    #displaying right guessed letters
    def display_word(self):
        guessed_word = "" # new variable to put in the right letter with the underscores
        for letter in self.word: #runs in range of the len(self.word)
            if letter in self.correct_letters:
                guessed_word += letter #adding the leter in the new word variable IF the letter is in the word
            else:
                guessed_word += "_ " #adding the underscores when the letter is NOT in the word
        self.guessed_word.config(text=guessed_word) #changing the SELF.guessed_word into the new guessed_word which looks something like this: _ _ _ _ a _ _

    #displaying the wrong guessed letters
    def update_incorrect_letters(self):
        self.incorrect_label.config(text="Incorrect letters: {}".format(", ".join(self.incorrect_letters)))

    
    #switching between settings page and main page and vice versa
    def show_settings(self):
        self.incorrect_label.pack_forget()
        self.main_page.pack_forget()
        self.settings_page.pack(side="top", fill="both", expand=True)
        
    def show_main_page(self):
        self.incorrect_label.pack(side="bottom")
        self.settings_page.pack_forget()
        self.main_page.pack(side="top", fill="both", expand=True)

root = tk.Tk()
app = Hangman(root)
root.mainloop()
