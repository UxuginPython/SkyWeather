import WeatherUI
import SWDriver
WeatherUI.set_driver(SWDriver)
while True:
    SWDriver.update()
    WeatherUI.update()
