from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import requests


url = 'https://api.kanye.rest/'

class LyricsApp:

    def __init__(self, root):
        root.title('Random Lyrics from Eminem')
        root.geometry("1024x768")

        self.canvas = Canvas()
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight =1)
        root.rowconfigure(0, weight=1)

        bubble_image = Image.open("speech-bubble-png-13.png").convert("RGBA")
        bubble_image = bubble_image.resize((700, 600))
        speech_bubble = ImageTk.PhotoImage(bubble_image)

        self.canvas = Canvas(mainframe, width=800, height=600)
        self.canvas.create_image(400, 350, image=speech_bubble)
        self.canvas.grid(column=0, row=0, columnspan=4, sticky="nsew")
        self.quote_s = self.canvas.create_text(400,250,text='placeholder', width=400,font=('Arial', 28, 'bold'))

        mini_image = ImageTk.PhotoImage(Image.open("SlimShady.png").convert("RGBA"))
        em_button = ttk.Button(root, image=mini_image, command=self.the_quote, )
        em_button.grid(column=0, row=1, sticky=W)

        em_button.image = mini_image
        self.canvas.image = speech_bubble
    def the_quote(self, *args):
        try:
            clicked = requests.get(url)
            if clicked.status_code == 200:
                data = clicked.json()
                quotes = data['quote']
                self.canvas.itemconfig(self.quote_s, text= quotes)
        except ValueError:
            pass


root = Tk()
initialize = requests.get(url)
LyricsApp(root)
root.mainloop()