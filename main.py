from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import requests


url = 'https://eminem-quotes-api.onrender.com/'

class LyricsApp:

    def __init__(self, root):
        root.title('Random Lyrics from Eminem')
        root.geometry("800x600")

        self.canvas = Canvas()
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight =1)
        root.rowconfigure(0, weight=1)

        mini_image = ImageTk.PhotoImage(Image.open("SlimShady.png").convert("RGBA"))
        em_button = ttk.Button(root, image=mini_image, command=self.the_quote, )
        em_button.grid(column=0, row=1, sticky=W)

        bubble_image = Image.open("speechbubble.png").convert("RGBA")
        speech_bubble = ImageTk.PhotoImage(bubble_image)

        self.canvas = Canvas(mainframe, width=400, height=500)
        self.canvas.grid(column=0, row=0, columnspan=4, sticky="nsew")
        self.quote_s = self.canvas.create_text(200,200,text='placeholder', width=400,font=('Arial', 32, 'bold'))


        em_button.image = mini_image
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