from tkinter import *
from tkinter import ttk
import time
from datetime import date

import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

total_slots = 50
empty_slots = 20
spot_no = []
spot_no.append("R1 C2")

class IPS:

    def tick(self):
        global time1
        self.time1 = time.strftime('%H:%M:%S')
        self.clock.config(text="Time : "+self.time1, foreground = "white")
        self.clock.after(1000, self.tick)

    def calander(self):
        self.today_date = date.today()
        s = str(self.today_date)
        
        
        if s[5]+s[6] == "01":
            self.today_date = s[8]+s[9]+' JAN '+s[0]+s[1]+s[2]+s[3]
        if s[5]+s[6] == "02":
            self.today_date = s[8]+s[9]+' FEB '+s[0]+s[1]+s[2]+s[3]
        if s[5]+s[6] == "03":
            self.today_date = s[8]+s[9]+' MAR. '+s[0]+s[1]+s[2]+s[3]
        if s[5]+s[6] == "04":
            self.today_date = s[8]+s[9]+' APR. '+s[0]+s[1]+s[2]+s[3]
        if s[5]+s[6] == "05":
            self.today_date = s[8]+s[9]+' MAY '+s[0]+s[1]+s[2]+s[3]
        if s[5]+s[6] == "06":
            self.today_date = s[8]+s[9]+' JUN '+s[0]+s[1]+s[2]+s[3]
        if s[5]+s[6] == "07":
            self.today_date = s[8]+s[9]+' JUL '+s[0]+s[1]+s[2]+s[3]
        if s[5]+s[6] == "08":
            self.today_date = s[8]+s[9]+' AUG '+s[0]+s[1]+s[2]+s[3]
        if s[5]+s[6] == "09":
            self.today_date = s[8]+s[9]+' SEP '+s[0]+s[1]+s[2]+s[3]
        if s[5]+s[6] == "10":
            self.today_date = s[8]+s[9]+' OCT '+s[0]+s[1]+s[2]+s[3]
        if s[5]+s[6] == "11":
            self.today_date = s[8]+s[9]+' NOV '+s[0]+s[1]+s[2]+s[3]
        if s[5]+s[6] == "12":
            self.today_date = s[8]+s[9]+' DEC '+s[0]+s[1]+s[2]+s[3]
            
        self.date.configure(text = "Date : "+str(self.today_date), foreground = "white")
        #self.date.after(1000,self.calander())

    def dayofweek(self):
       self.today_day = date.today().weekday()
       if self.today_day == 0:
           self.today_day = "Monday"
       if self.today_day == 1:
           self.today_day = "Tuesday"
       if self.today_day == 2:
           self.today_day = "Wednesday"
       if self.today_day == 3:
           self.today_day = "Thursday"
       if self.today_day == 4:
           self.today_day = "friday"
       if self.today_day == 5:
           self.today_day = "Saturday"
       if self.today_day == 6:
           self.today_day = "Sunday"
       self.day.configure(text = "Day : "+str(self.today_day), foreground = "white")
       #self.day.after(1000,self.dayofweek())

    def __init__(self, master):
        
        master.title('Intelligent Parking System')
        master.state("zoomed")
        master.configure(background = 'white')
        
        #styles
        self.style = ttk.Style()
        self.style.configure("1.TFrame", background = "#AED6F1")
        self.style.configure("2.TFrame", background = "#0C0C0C")

        #first frame

        first_frame = ttk.Frame(master, width = 1400, height = 150, style = "2.TFrame")
        first_frame.grid(row = 0, column = 0, columnspan = 3, rowspan = 2, pady = (0,15))
        
        #time by clock
        self.time1 = ''
        self.clock = Label(first_frame, font=("times", 20, 'bold'), background = '#A93226')
        self.clock.pack(ipady = 20, ipadx = 105, padx = 22, pady = (30,20), side = LEFT)
        self.tick()

        #date
        self.today_date = " ",
        self.date = Label(first_frame, font=("times",20,'bold'), background = '#A93226')
        self.date.pack( ipady = 20, ipadx = 75, padx = 33, pady = (30,20), side = LEFT)
        self.calander()

        #day
        self.today_day = " "
        self.day = Label(first_frame, font=('times',20,'bold'), background ='#A93226')
        self.day.pack(ipady = 20, ipadx = 110, padx = (20,55), pady = (30,20), side = LEFT)
        self.dayofweek()

        #piechart
        labels = ["Empty slot"+"("+str(empty_slots)+")", "Filled slots"+"("+str(total_slots - empty_slots)+")"]
        values = [empty_slots, total_slots]
        actualFigure = plt.figure(figsize = (4,4), facecolor = "#17202A")
        actualFigure.text(0.13, 0.92, "Parking Spots Availability", fontsize = 17, color = "#1ABC9C")
        explode = list()
        for k in labels:
            explode.append(0.1)

        pie= plt.pie(values, labels=labels, explode = explode, shadow = True)

        canvas = FigureCanvasTkAgg(actualFigure, root)
        canvas.get_tk_widget().grid(row = 2, column = 0, rowspan = 9, padx = 20, pady = (10, 13), stick = "w")
        canvas.show()

        #spots
        self.spot = ttk.Label(master, text = "     Total Available Spots : "+str(total_slots), foreground = "white", background = "#2ECC71", font = ("Agency FB", 28))
        self.spot.grid(row = 11, column = 0, ipadx = 43, ipady = 8, padx = 20, pady = (0,3), stick = "w")
        self.spot = ttk.Label(master, text = "     Total Empty Spots : "+str(empty_slots), foreground = "white", background = "#2ECC71", font = ("Agency FB", 28))
        self.spot.grid(row = 12, column = 0, ipadx = 59, ipady = 8, padx = 20, pady = (0,3), stick = "w")        
        
        #topframe      
        self.Topframe = ttk.Frame(master, width = 430, height = 380, style = "1.TFrame")
        self.Topframe.grid(row = 2, column = 1, rowspan = 9, stick = 'w')
        self.spot = ttk.Label(self.Topframe, text = "  Nearest Spot : "+str(spot_no[0]), foreground = "white", background = "#1B4F72", font = ("Agency FB", 30))
        self.spot.pack(ipadx = 37, ipady = 15, side = TOP, padx = 10, pady = 13)
        
        self.spot1 = ttk.Label(self.Topframe, text = "  Other Available Spots :", foreground = "white",background = "#515A5A", font = ("Agency FB", 25))
        self.spot1.pack(ipadx = 37, ipady = 6, padx = 10, fill = BOTH, expand = True, anchor = "w")
        
        self.spot2 = ttk.Label(self.Topframe,
                               text = '* '+str(spot_no[0]), foreground = "white", background = '#5DADE2', font = ("Agency FB", 25))
        self.spot2.pack(ipadx = 37, ipady = 6, padx = 10, fill = BOTH, expand = True, anchor = "w")
        
        self.spot3 = ttk.Label(self.Topframe, text = '* '+str(spot_no[0]), foreground = "white", background = "#5DADE2", font = ("Agency FB", 25))
        self.spot3.pack(ipadx = 37, ipady = 6, padx = 10, fill = BOTH, expand = True, anchor = "w")
        
        self.spot4 = ttk.Label(self.Topframe, text = '* '+str(spot_no[0]), foreground = "white", background = "#5DADE2", font = ("Agency FB", 25))
        self.spot4.pack(ipadx = 37, ipady = 6, padx = 10, fill = BOTH, expand = True, anchor = "w")
        
        self.spot5 = ttk.Label(self.Topframe, text = '* '+str(spot_no[0]), foreground = "white", background = "#5DADE2", font = ("Agency FB", 25))
        self.spot5.pack(ipadx = 37, ipady = 6, padx = 10, pady = (0,10), fill = BOTH, expand = True, anchor = "w")

        #parking image
        self.img = PhotoImage(file = "parking spot.png")
        label_image = Label(master, image = self.img)
        label_image.grid(row = 2, column = 2, rowspan = 11, stick = "w")


            
root = Tk()
Gui = IPS(root)
root.configure(background = "#424949")
root.mainloop()

