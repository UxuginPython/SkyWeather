#import driver
driver=None
def set_driver(driver_):
    global driver
    driver=driver_
while driver==None:
    pass

from numpy import sin, cos

from tkinter import *
window=Tk()
window.title('Weather')

class overview:
    font=('', 48, '')
    frame=Frame(window)
    temp=Label(frame, text=driver.temp, font=font)
    wind_speed=Label(frame, text=driver.wind_speed, font=font)
    pressure=Label(frame, text=driver.pressure, font=font)
    temp_label=Label(frame, text='Temperature')
    wind_speed_label=Label(frame, text='Wind Speed')
    pressure_label=Label(frame, text='Pressure')
class wind_direction(overview):
    canvas=Canvas(overview.frame, width=100, height=100)
    circle=canvas.create_oval(0, 0, 100, 100)
    line=canvas.create_line(50, 50, 50*cos(driver.wind_direction), 50*sin(driver.wind_direction))
    wd_label=Label(overview.frame, text='Wind Direction')

overview.temp.grid(column=0, row=0)
overview.wind_speed.grid(column=1, row=0)
overview.pressure.grid(column=2, row=0)
wind_direction.canvas.grid(column=3, row=0)

overview.temp_label.grid(column=0, row=1)
overview.wind_speed_label.grid(column=1, row=1)
overview.pressure_label.grid(column=2, row=1)
wind_direction.wd_label.grid(column=3, row=1)

overview.frame.grid(column=0, row=0)
mainloop()
