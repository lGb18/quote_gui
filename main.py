"""GUI for displaying random Eminem Lyrics from Eminem quotes API"""
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import requests

URL = 'https://eminem-quotes-api.onrender.com/'


class LyricsApp:
    """Create a Window for displaying quotes."""
    def __init__(self, root):
        root.title('Random Lyrics from Eminem')
        root.geometry("1024x768")

        self.canvas = Canvas()
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight =1)

        bubble_image = Image.open("empy_speech-modified.png")
        bubble_image = bubble_image.resize((800, 800))
        speech_bubble = ImageTk.PhotoImage(bubble_image)

        self.canvas = Canvas(mainframe, width=800, height=600)
        self.canvas.create_image(400, 300, image=speech_bubble)
        self.canvas.grid(column=0, row=0, columnspan=4, sticky="nsew")
        self.quote_s = self.canvas.create_text(400,250,text="Click em ",
        width=500,font=('Arial', 28, 'bold'))

        pil_image = Image.open("SlimShady.png").convert("RGBA")
        resized = pil_image.resize((155,155))
        mini_image = ImageTk.PhotoImage(resized)
        # mini_image = ImageTk.PhotoImage(Image.open("SlimShady.png").convert("RGBA"))
        em_button = ttk.Button(root, image=mini_image, command=self.the_quote, )
        em_button.grid(column=0, row=1, sticky=N)

        em_button.image = mini_image
        self.canvas.image = speech_bubble


    def the_quote(self):
        """Fetches quote from the API"""
        try:
            clicked = requests.get(URL)
            if clicked.status_code == 200:
                data = clicked.json()
                quotes = data['quotes']
                self.canvas.itemconfig(self.quote_s, text= quotes)
        except ValueError:
            pass

em_app = Tk()
LyricsApp(em_app)
initialize = requests.get(URL)
em_app.mainloop()
