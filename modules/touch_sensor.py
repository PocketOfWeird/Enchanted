import time
import board
import busio
import adafruit_mpr121

def start_touch_sensor_loop(touch_manager) -> None:
    i2c = busio.I2C(board.SCL, board.SDA)
    mpr121 = adafruit_mpr121.MPR121(i2c)
    
    while True:
        for i in range(12):
            if mpr121[i].value:
                touch_manager(i)
        time.sleep(0.25)