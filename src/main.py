"""GUI for displaying random Eminem Lyrics from Eminem quotes API"""
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import requests
from image_dir import get_image
from wake_API import wake_api
URL = 'https://eminem-quotes-api.onrender.com/'


class LyricsApp:
    """Create a Window for displaying quotes."""

    def __init__(self, root):
        root.title('Eminem Quotes API GUI')
        root.geometry("1024x768")

        self.canvas = Canvas()
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight =1)

        """Initialize and resize images"""
        image_speech = 'empy_speech-modified.png'
        bubble_image = Image.open(get_image(image_speech))
        bubble_image = bubble_image.resize((800, 800))
        speech_bubble = ImageTk.PhotoImage(bubble_image)

        image_slim = 'SlimShady.png'
        pil_image = Image.open(get_image(get_image(image_slim))).convert("RGBA")
        resized = pil_image.resize((155, 155))
        mini_image = ImageTk.PhotoImage(resized)

        """Build the frame and button using images"""
        self.canvas = Canvas(mainframe, width=800, height=600)
        self.canvas.create_image(400, 300, image=speech_bubble)
        self.canvas.grid(column=0, row=0, columnspan=4, sticky="nsew")
        self.quote_s = self.canvas.create_text(400,250,text="Click em ",
        width=500,font=('Arial', 28, 'bold'))

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
        except requests.exceptions.ConnectionError:
            error_text = 'Connection failed.\nPlease check your internet and retry.'
            self.canvas.itemconfig(self.quote_s, text=error_text)

em_app = Tk()
LyricsApp(em_app)
wake_api()
em_app.mainloop()
