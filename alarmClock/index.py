#ALARM CLOCK

#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
from pygame import mixer
from tkinter import messagebox


clock = Tk()
clock.title("Alarm Clock")
clock.geometry("830x530")

alarm_time = StringVar()
msgs = StringVar()
head = Label(clock,text="Alarm Clock", font=("comic sans", 40))
head.grid(row=0,columnspan=3, pady=15)
mixer.init()

def alarm_clock():
   alm = alarm_time.get()

   AlmTime = alm
   currentTime = time.strftime("%H:%M")
   #currentTime = datetime.datetime.now() 

   while AlmTime != currentTime:
      currentTime = time.strftime("%H:%M")

   if AlmTime == currentTime: 
      mixer.music.load("Ring.mp3")
      mixer.music.play() 
      msg = messagebox.showinfo('Info',f'{msgs.get()}')
      if msg == 'ok':
         mixer.music.stop()
         
    


#loop end...............................................

clockimg = PhotoImage(file = "images/clock-removebg-preview.png")
img = Label(clock,image=clockimg , width=365,height=450)
img.grid(rowspan=4,column=0)

#addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",15,"bold"), height=1)
setYourAlarm.grid(row=1,column=1)


clock_time = Entry(clock,textvariable=alarm_time, font=("comic sans", 15, "bold"),width=7)
clock_time.grid(row=1, column=2)

msg = Label(clock, text="Message",fg="blue",relief = "solid",font=("Helevetica",15,"bold"),width=15, height=1)
msg.grid(row=2, column=1)

msginput = Entry(clock,textvariable=msgs, font=("comic sans",18), width=15)
msginput.grid(row=2, column=2, columnspan=2)

suggetion=Label(clock, text= "Enter time in 24 hour format!", fg="black",bg="pink",font=("Arial",20,"bold")).place(x=380,y=450)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,font=("camic sans",20), command=alarm_clock)
submit.grid(row=3,column=1,columnspan=3)

clock.mainloop()
#Execution of the window.   

