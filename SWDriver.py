#!/usr/bin/env python3
#Actual driver unfinished;
#This is just a placeholder to test the UI.
from random import randrange
temperature=70
wind_speed=10
pressure=50
wind_direction=0
connected=True
def update():
    global temperature, wind_speed, pressure, wind_direction
    #temperature=randrange(0, 100)
    #wind_speed=randrange(0, 100)
    #pressure=randrange(0, 100)
    wind_direction+=1
