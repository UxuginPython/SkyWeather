#!/usr/bin/env python3
try:
    from tkinter import *
except:
    from warnings import warn
    warn('This software is designed for Python 3. However, Python 2 was detected.')
    from Tkinter import *
from WeatherUI import WeatherUI
import SWDriver
from sys import exit
window=Tk()
window.title('Weather')
ui=WeatherUI(window, driver=SWDriver)
ui.pack()
while True:
    SWDriver.update()
    ui.update()
    try:
        window.update()
        window.update_idletasks()
    except TclError:
        exit()
