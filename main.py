from tkinter import *
from tkinter import ttk
import requests


url = 'https://eminem-quotes-api.onrender.com/'

class LyricsApp:

    def __init__(self, root):
        root.title('Random Lyrics from Eminem')

        self.canvas = Canvas()
        mainframe = ttk.Frame(root)
        mainframe.grid(column=10, row=10)
        root.columnconfigure(0, weight =1)
        root.rowconfigure(0, weight=1)

        self.canvas = Canvas(mainframe, width=800, height=600, bg='red')
        self.canvas.grid(column=0, row=0, columnspan=4, sticky="nsew")
        self.quote_s = self.canvas.create_text(400,300,text='placeholder', width=600,font=('Arial', 32, 'bold'))
        ttk.Button(mainframe, text='Generate', command=self.the_quote).grid(column=2,row=1, sticky=W)

    def the_quote(self, *args):
        try:
            clicked = requests.get(url)
            if clicked.status_code == 200:
                data = clicked.json()
                quotes = data['quotes']
                self.canvas.itemconfig(self.quote_s, text= quotes)
        except ValueError:
            pass



root = Tk()
LyricsApp(root)
root.mainloop()