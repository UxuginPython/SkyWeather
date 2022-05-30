from WeatherUI import WeatherUI
import SWDriver
wui=WeatherUI(driver=SWDriver)
while True:
    SWDriver.update()
    wui.update()
