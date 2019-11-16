from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from record_module import *
from username import *
from db import *

fname = "testfile.wav"

class Testing_file:
    def __init__(self):
        root = Toplevel()
        root.title("Speaker Recognition - Recognise the User")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.state('zoomed')

        ## Resizable Image

        image = Image.open(r'bggif/speakerid.gif')
        global copy_of_image
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        global label
        label = Label(root, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', self.resize_image)

        ## Adding Buttons

        recording_button = Button(root, fg="white", background="green", activebackground="green",font=("Helvetica",20,'bold italic'), activeforeground="orange", text='Record', padx=10, pady=10, command = record_audio)
        recording_button.place(relx=0.35, rely=0.5, anchor=CENTER)

        play_button = Button(root, fg="white", background="green", activebackground="green",font=("Helvetica",20,'bold italic'), activeforeground="orange", text='Play', padx=10, pady=10, command = self.audioplay)
        play_button.place(relx=0.471, rely=0.5, anchor=CENTER)

        test_button = Button(root, fg="white", background="green", activebackground="green",font=("Helvetica",20,'bold italic'), activeforeground="orange", text='Recognise', padx=10, pady=10, command = self.testaudio)
        test_button.place(relx=0.61, rely=0.5, anchor=CENTER)

        root.mainloop()


    ## Function for resizing the Image

    def resize_image(self,event):
        new_width = event.width
        new_height = event.height
        global copy_of_image
        image = copy_of_image.resize((new_width, new_height))
        global photo
        photo = ImageTk.PhotoImage(image)
        global label
        label.config(image = photo)
        label.image = photo

    def audioplay(self):
        global fname
        play_audio(fname)

    def testaudio(self):
    	k = test1()
    	recog(k)
