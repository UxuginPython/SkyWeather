try:
    from tkinter import *
except:
    from warnings import warn
    warn('This software is designed for Python 3. However, Python 2 was detected.')
    from Tkinter import *
from WeatherUI import WeatherUI
import SWDriver
window=Tk()
window.title('Weather')
ui=WeatherUI(window, driver=SWDriver)
ui.pack()
while True:
    SWDriver.update()
    ui.update()
    window.update()
    window.update_idletasks()
