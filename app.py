"""
A simple application.
"""

import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self, title: str):
        super().__init__()
        self.title(title)

        label = tk.Label(self, text="Your name")
        label.pack()

        self.username = tk.Entry(self)
        self.username.pack()

        self.submit = tk.Button(self, text="Submit")
        self.submit.pack()

        self.submit.config(command=self.submit_form)

    def submit_form(self):
        username = self.username.get().strip()
        if username:
            self.welcome(username)
            self.username.delete("0", "end")

    def welcome(self, name: str):
        messagebox.showinfo("Welcome", f"Hi {name}, how are you?")


if __name__ == "__main__":
    app = App("Hello")
    app.mainloop()

