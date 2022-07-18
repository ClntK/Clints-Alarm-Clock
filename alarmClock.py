# Filename: alarmClock.py
# Created Date: 07/08/2022
# Author: Clint Kline
# Purpose: to wake me up

# libraries
from time import time
from tkinter import * 
from tkinter import ttk 
import datetime
import time
import winsound
import threading
import shutil
import winsound
import keyboard


# create the clock window
clock = Tk()
clock.title("Clint's Clock")
clock.geometry("400x400")
clock.configure(bg="black")

# draw a progress bar
frame = ttk.Frame(clock, height=50, width=150)
progressbar = ttk.Progressbar(frame, mode='indeterminate')
progressbar.grid(column=2, row=0, sticky=W)


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarmIsSet(set_alarm_timer)
    alarm(set_alarm_timer)      
    
    
def alarmIsSet(set_alarm_timer):
    alarm_is_set = Label (clock, text= f"The alarm is set to {set_alarm_timer}", fg="red", bg="black", font="Arial").place(x=105, y=300)
    snoozeTip = Label (clock, text="..hit spacebar to snooze..", fg="yellow", bg="black",font="Arial").place(x=110, y=330)
    frame.place(x=150, y=195)

#  functions
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%m/%d/%Y")
        print(now)
        
        if now == set_alarm_timer:
            print("Wake Up.")
            playAlarm()
            break
    
    
def playAlarm():  
    snooze = False
    while snooze == False:          
        freq = 500
        dur = 250
        
        # alarm sound
        for i in range(0,5):
            winsound.Beep(freq, dur)
            freq+=300
            if keyboard.is_pressed(" "):
                print("snoozed")
                snooze = True
    
    
def digitalclock():    
    text_input = time.strftime("%H:%M:%S")
    clockDisplay.config(text=text_input)
    clock.after(200, digitalclock)
    
    
def start_submit_thread(event):
    global submit_thread
    submit_thread = threading.Thread(target=actual_time)
    submit_thread.daemon = True
    progressbar.start()
    submit_thread.start()
    clock.after(20, check_submit_thread)


def check_submit_thread():
    if submit_thread.is_alive():
        clock.after(20, check_submit_thread)
    else:
        progressbar.stop()

# variables

clockDisplay = Label(clock, font=("Courier", 30, 'bold'), bg="black", fg="red", bd=30)
clockDisplay.grid(row=0, column=1)
clockDisplay.place(x=70, y=10)

time_format = Label (clock, text= "Enter time in 24 hr format: ", fg="grey", bg="black",font="Arial").place(x=110, y=270)
addTime = Label (clock, text = "Hour     Min       Sec", font=("Helvetica", 12, "bold"), fg="grey", bg="black").place(x=125, y=140)
setYourAlarm = Label (clock, text = "Set the alarm: ", fg="grey", bg="black", font=("Helvetica", 12, "bold")).place(x=140, y=110)

hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "grey",width = 5).place(x=130,y=170)
minTime= Entry(clock,textvariable = min,bg = "grey",width = 5).place(x=185,y=170)
secTime = Entry(clock,textvariable = sec,bg = "grey",width = 5).place(x=240,y=170)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="grey",width = 10,command=lambda:start_submit_thread(None)).place(x =160,y=220)

digitalclock()
clock.mainloop()

#Execution of the window.