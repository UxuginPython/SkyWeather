try:
    from tkinter import *
except:
    from warnings import warn
    warn('WeatherUI is designed for Python 3. However, Python 2 was detected.')
    from Tkinter import *
from numpy import sin, cos
class WindDirection:
    def __init__(self, master, driver):
        self.driver=driver
        self.canvas=Canvas(master, width=100, height=100)
        self.circle=self.canvas.create_oval(0, 0, 100, 100)
        self.line=self.canvas.create_line(50, 50, 50*cos(self.driver.wind_direction)+50, 50*sin(self.driver.wind_direction)+50) #Sorry this is ugly and very non-Pythonic
    def update(self):
        self.canvas.delete(self.line)
        self.line=self.canvas.create_line(50, 50, 50*cos(self.driver.wind_direction)+50, 50*sin(self.driver.wind_direction)+50)
    def grid(self, row=0, column=0):
        self.canvas.grid(column=column, row=row)
class Overview:
    def __init__(self, master, driver):
        self.font=('', 48, '')
        self.frame=Frame(master)
        self.driver=driver
        self.temperature=Label(self.frame, text=self.driver.temperature, font=self.font)
        self.wind_speed=Label(self.frame, text=self.driver.wind_speed, font=self.font)
        self.pressure=Label(self.frame, text=self.driver.pressure, font=self.font)
        self.wind_direction=WindDirection(self.frame, self.driver)
        
        self.temperature_label=Label(self.frame, text='Temperature')
        self.wind_speed_label=Label(self.frame, text='Wind Speed')
        self.pressure_label=Label(self.frame, text='Pressure')
        self.wind_direction_label=Label(self.frame, text='Wind Direction')
    def update(self):
        self.temperature.config(text=self.driver.temperature)
        self.wind_speed.config(text=self.driver.wind_speed)
        self.pressure.config(text=self.driver.pressure)
        self.wind_direction.update()
    def grid(self, row=0, column=0):
        self.temperature.grid(column=0, row=0)
        self.wind_speed.grid(column=1, row=0)
        self.pressure.grid(column=2, row=0)
        self.wind_direction.grid(column=3, row=0)
        
        self.temperature_label.grid(column=0, row=1)
        self.wind_speed_label.grid(column=1, row=1)
        self.pressure_label.grid(column=2, row=1)
        self.wind_direction_label.grid(column=3, row=1)
        
        self.frame.grid(column=column, row=row)
class WeatherUI:
    def __init__(self, master, driver):
        self.driver=driver
        self.frame=Frame(master)
        self.overview=Overview(self.frame, self.driver)
        self.overview.grid(column=0, row=0)
    def grid(self, row, column):
        self.frame.grid(column=column, row=row)
    def pack(self):
        self.frame.pack()
    def update(self):
        self.overview.update()
