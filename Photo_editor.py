import PIL.Image
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageTk



class Photo_Editor:
    
    #file manager bar.
    def Open_File(self):
        self.path1 = askopenfilename(filetypes =(("PNG FILE", "*.png"),("All Files","*.*")),
                           title = "Choose a file.")
        print(self.path1)
        if self.path1 != "":
            self.path2 = self.path1
            self.img = PhotoImage(file = self.path1)
            #self.img = self.img.subsample(2,2)
            self.canvas.delete(self.img2)
            self.img2 = self.canvas.create_image(self.w/2, self.h/2, image = self.img, anchor = CENTER)
        else:
            self.path1 = self.path2
           
        

    def Rotate_Left(self):
        global picture
        self.angle = self.angle+90
        picture = Image.open(self.path1)
        #picture = picture.resize((self.h, self.w), Image.ANTIALIAS)
        picture = ImageTk.PhotoImage(picture.rotate(self.angle))
        self.canvas.itemconfigure(self.img2, image = picture)   

    def Rotate_Right(self):
        global picture
        self.angle = self.angle-90
        picture = Image.open(self.path1)
        #picture = picture.resize((self.h, self.w), Image.ANTIALIAS)
        picture = ImageTk.PhotoImage(picture.rotate(self.angle))
        self.canvas.itemconfigure(self.img2, image = picture)

    def __init__(self, master):

        master.resizable(False, False)
        self.master = master
        self.style = ttk.Style()
        self.style.configure('1.TFrame', background = '#FF5733')
        self.style.configure('2.TFrame', background = '#e1d8b9')
        self.angle = 0

        
        #picture
        self.path1 = "guitar.png"
        self.path2 = self.path1
        self.img = PhotoImage(file = self.path1)
        self.w = self.img.width()
        self.h = self.img.height()

        #Canvas
        self.canvas = Canvas(master, width = self.w, height = self.h)
        self.canvas.pack(pady = 10)
        self.img2 = self.canvas.create_image(self.w/2, self.h/2, image = self.img, anchor = CENTER)

        #buttons
        self.button_frame = ttk.Frame(master, relief = SUNKEN, style = "1.TFrame")
        self.button_frame.pack(padx = 10)


        ttk.Button(self.button_frame, text = 'SAVE').grid(row = 0, column = 0, padx = 25, pady = 10)
        ttk.Button(self.button_frame, text = 'IMPORT', command = self.Open_File, compound = TOP).grid(row = 0, column = 1, padx = 20, pady = 10)
        ttk.Button(self.button_frame, text = 'CROP').grid(row = 0, column = 2, padx = 25, pady = 10)
        self.rt = ttk.Button(self.button_frame, text = 'Rotate Right', command = self.Rotate_Right).grid(row = 1, column = 0, padx = 25, pady = 10)
        ttk.Button(self.button_frame, text = 'UNDO').grid(row =1, column = 1, padx = 25, pady = 10)
        ttk.Button(self.button_frame, text = 'Rotate Left', command = self.Rotate_Left).grid(row = 1, column = 2, padx = 25, pady = 10)

        #2nd frame
        labelframe = ttk.LabelFrame(master , text = "Effects", style = "2.TFrame")
        labelframe.pack( padx = 10, pady = 10)

         #effects
        autumn = ttk.Label(labelframe, background = "orange", text = "AUTUMN").pack( padx = 1,
                                                                                    ipadx = 15, ipady = 15, side = LEFT)
        autumn = ttk.Label(labelframe, background = "orange", text = "CLASSIC").pack( padx = 1,
                                                                                    ipadx = 15, ipady = 15, side = LEFT)
        autumn = ttk.Label(labelframe, background = "orange", text = "BREEZE").pack( padx = 1,
                                                                                    ipadx = 15, ipady = 15, side = LEFT)
        autumn = ttk.Label(labelframe, background = "orange", text = "CARTOON").pack( padx = 1,
                                                                                    ipadx = 15, ipady = 15, side = LEFT)
        autumn = ttk.Label(labelframe, background = "orange", text = "FOREST").pack( padx = 1,
                                                                                    ipadx = 15, ipady = 15, side = LEFT)        
root = Tk()
Gui = Photo_Editor(root)
root.configure(background = "black")
root.title('Photo Editor')
root.mainloop()

