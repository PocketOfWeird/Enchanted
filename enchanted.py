from pygame import mixer
from modules.touch_sensor import start_touch_sensor_loop
from modules.touch_manager import touch_manager

mixer.init()

start_touch_sensor_loop(touch_manager)