#import driver

#driver=None
#def set_driver(driver_):
#    global driver
#    driver=driver_
#while driver==None:
#    pass
from tkinter import *
from numpy import sin, cos
class WeatherUI:
    def __init__(self, driver):
        self.driver=driver
        
        #from numpy import sin, cos
        
        #from tkinter import *
        self.window=Tk()
        self.window.title('Weather')
        
        self.overview_font=('', 48, '')
        self.overview_frame=Frame(self.window)
        self.overview_temperature=Label(self.overview_frame, text=self.driver.temperature, font=self.overview_font)
        self.overview_wind_speed=Label(self.overview_frame, text=self.driver.wind_speed, font=self.overview_font)
        self.overview_pressure=Label(self.overview_frame, text=self.driver.pressure, font=self.overview_font)
        self.overview_temperature_label=Label(self.overview_frame, text='Temperature')
        self.overview_wind_speed_label=Label(self.overview_frame, text='Wind Speed')
        self.overview_pressure_label=Label(self.overview_frame, text='Pressure')
        
        self.wind_direction_canvas=Canvas(self.overview_frame, width=100, height=100)
        self.wind_direction_circle=self.wind_direction_canvas.create_oval(0, 0, 100, 100)
        self.wind_direction_line=self.wind_direction_canvas.create_line(50, 50, 50*cos(driver.wind_direction), 50*sin(driver.wind_direction))
        self.wind_direction_label=Label(self.overview_frame, text='Wind Direction')
        
        self.overview_temperature.grid(column=0, row=0)
        self.overview_wind_speed.grid(column=1, row=0)
        self.overview_pressure.grid(column=2, row=0)
        self.wind_direction_canvas.grid(column=3, row=0)
        
        self.overview_temp_label.grid(column=0, row=1)
        self.overview_wind_speed_label.grid(column=1, row=1)
        self.overview_pressure_label.grid(column=2, row=1)
        self.wind_direction_label.grid(column=3, row=1)
        
        self.overview_frame.grid(column=0, row=0)
    def update(self):
        self.window.update()
        self.window.update_idletasks()
