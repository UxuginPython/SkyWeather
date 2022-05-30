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

overview_font=('', 48, '')
overview_frame=Frame(window)
overview_temp=Label(frame, text=driver.temp, font=font)
overview_wind_speed=Label(frame, text=driver.wind_speed, font=font)
overview_pressure=Label(frame, text=driver.pressure, font=font)
overview_temp_label=Label(frame, text='Temperature')
overview_wind_speed_label=Label(frame, text='Wind Speed')
overview_pressure_label=Label(frame, text='Pressure')

wind_direction_canvas=Canvas(overview_frame, width=100, height=100)
wind_direction_circle=canvas.create_oval(0, 0, 100, 100)
wind_direction_line=canvas.create_line(50, 50, 50*cos(driver.wind_direction), 50*sin(driver.wind_direction))
wind_direction_label=Label(overview_frame, text='Wind Direction')

overview_temp.grid(column=0, row=0)
overview_wind_speed.grid(column=1, row=0)
overview_pressure.grid(column=2, row=0)
wind_direction_canvas.grid(column=3, row=0)

overview_temp_label.grid(column=0, row=1)
overview_wind_speed_label.grid(column=1, row=1)
overview_pressure_label.grid(column=2, row=1)
wind_direction_label.grid(column=3, row=1)

overview_frame.grid(column=0, row=0)
mainloop()
