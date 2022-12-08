#!/usr/bin/env python3
from datetime import datetime
try:
    from tkinter import *
except:
    from warnings import warn
    warn('WeatherUI is designed for Python 3. However, Python 2 was detected.')
    from Tkinter import *
from numpy import sin, cos
def create_point(canvas, x, y):
    return canvas.create_oval(x-1, y-1, x+1, y+1)
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
    def pack(self):
        self.canvas.pack()
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
    def pack(self):
        self.temperature.grid(column=0, row=0)
        self.wind_speed.grid(column=1, row=0)
        self.pressure.grid(column=2, row=0)
        self.wind_direction.grid(column=3, row=0)
        
        self.temperature_label.grid(column=0, row=1)
        self.wind_speed_label.grid(column=1, row=1)
        self.pressure_label.grid(column=2, row=1)
        self.wind_direction_label.grid(column=3, row=1)
        
        self.frame.pack()
class Graph:
    def __init__(self, master, datafunc, data=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], scaley=100):
        self.master=master
        self.datafunc=datafunc
        self.canvas=Canvas(master, width=460, height=100)
        if len(data)!=24:
            raise ValueError('\'data\' must be of length 24.')
        self.data=data
        self.scaley=scaley
        self.points=[]
        for i in enumerate(data):
            self.points.append(create_point(self.canvas, i[0]*20, 100-i[1]*(100/self.scaley)))
        self.render()
    def grid(self, row=0, column=0):
        self.canvas.grid(row=row, column=column)
    def pack(self):
        self.canvas.pack()
    def render(self):
        self.data.append(self.datafunc())
        del(self.data[0])
        for i in self.points:
            #print(i)
            self.canvas.delete(i)
        self.points=[]
        for i in enumerate(self.data):
            self.points.append(create_point(self.canvas, i[0]*20, 100-i[1]*(100/self.scaley)))
    renderflag=True
    def update(self):
        #if datetime.now().second==0 and datetime.now().minute==0:
        if datetime.now().second==0:
            if self.renderflag:
                self.data.append(self.datafunc())
                del(self.data[0])
                for i in enumerate(self.points):
                    #print(i)
                    self.canvas.delete(self.points[i[0]])
                self.points=[]
                for i in enumerate(self.data):
                    self.points.append(create_point(self.canvas, i[0]*20, 100-i[1]*(100/self.scaley)))
                self.renderflag=False
        else:
            self.renderflag=True
class WeatherUI:
    def __init__(self, master, driver):
        self.driver=driver
        self.frame=Frame(master)
        self.overview=Overview(self.frame, self.driver)
        #self.temp_graph=Graph(self.frame, self.getTemp)
        self.overview.grid(column=0, row=0)
        #self.temp_graph.grid(column=0, row=1)
    #def getTemp(self):
        #return self.driver.temperature
    def grid(self, row, column):
        self.frame.grid(column=column, row=row)
    def pack(self):
        self.frame.pack()
    def update(self):
        self.overview.update()
        #self.temp_graph.update()
