from machine import Pin, UART
from primitives.pushbutton import Pushbutton
import uasyncio as asyncio
import _thread
from utime import ticks_ms, sleep_ms
from ledDisk import LedDisk, RED

light_blue = (0,0,127)
light_orange = (100,50,0)
light_red = (127,0,0)

state_time = [3,0.3333/2,3] # in minutes
state_colors = (light_blue, light_orange, light_red)
nb_states = len(state_time)
tick_time = .5 #seconds



# Configure led disk
led_pin = 22
leds = LedDisk(led_pin)
leds.Off()
# leds.rotate(2000)
# leds.wave(4000)

# Bluetooth serial connexion
uart = UART(0,9600)


# Global variables
state = 0
t0 = 0
tmax = state_time[state]*60*1000
time = 0.

# Signals when to change to another duration
# (and also start countdown to zero) 
FLAG_STATE_CHANGE = False
# Signals if the countdown has started yet
FLAG_START = False
# Signals when to stop the countdown
FLAG_STOPPED = False
# Signal when to start the coundown
FLAG_BEGIN = True
FLAG_QUESTION = False

BRIGHTNESS_MAX = .8
BRIGHTNESS_MIN = .3

T_QUESTION = 10*1000#10*60*1000
T_FLASH = 1*60*1000


pin = Pin(9, Pin.IN, pull=Pin.PULL_UP)  # Pushbutton



    
async def switch_state():
    global state
    state += 1
    state = state%nb_states
    leds.Blink(state_colors[state], timeout = 1000)
    print('Changing state to:', state)
    start()

def single_press():
    print('Single press')
    if FLAG_START or FLAG_STOPPED:
        print('flag', FLAG_START)
        print('Start')
        await switch_state()
    resume()

def long_press():
    print("Long press")
    stop()

def resume():
    global FLAG_START
    FLAG_START = True
    
def start():
    global t0, tmax
    t0 = ticks_ms()
    tmax = state_time[state]*60*1000
    
def stop():
    global FLAG_START, FLAG_STOPPED
    FLAG_START = False
    FLAG_STOPPED = True
    leds.Off()
    
def pause():
    global FLAG_START
    FLAG_START = False
    
def double_press():
    print('Double press')
    pause()

def get_bt_message(data):
    global FLAG_START
    global t0
    msg = ''.join([chr(b) for b in data])
    msg = msg.strip()
    print('Message: ', msg)
    if msg[0] == 'T':
        try:
            tmax = int(msg[1:])*60*1000
            print('New time:', tmax, msg[1:])
            FLAG_START = True
            t0 = ticks_ms()
        except:
            pass
    if msg[0] == 'C':
        try:
            # change time left
            time_left = int(msg[1:])
            t0 = tmax-*60*1000
        except:
            pass
    elif msg == 'START':
        print('Start/Restart')
        start()
        resume()
    elif msg == 'PAUSE':
        print('Pausing')
        pause()
    elif msg == 'RESUME':
        print('Resuming')
        resume()
    elif msg == 'STOP':
        print('Stopping')
        stop()
    elif msg == 'SWITCH':
        switch_state()
        
    
def bt_thread():
    global blue_btn
    while True:
        if uart.any():
            print('/BT')
            data = uart.read(32)
            get_bt_message(data)
            print('BT/')
            
_thread.start_new_thread(bt_thread, ())

async def main():
    global FLAG_QUESTION, t0, time
    pb = Pushbutton(pin, suppress = True)
    pb.release_func(single_press, ())  # Callback on button press
    pb.double_func(double_press, ())
    pb.long_func(long_press, ())  # Callback on long press
    t0 = ticks_ms()
    while True:
        await asyncio.sleep(tick_time)
#         if FLAG_STOP:
#             leds.Off()
#             FLAG_STOP = False
#             FLAG_BEGIN = False
#             FLAG_START = False
            
        if FLAG_START:
            time = ticks_ms()-t0
            print(time, time/tmax)
            if time>tmax-T_QUESTION:
                if not FLAG_QUESTION:
                    leds.Blink(RED, timeout = 2_000)
                FLAG_QUESTION = True
            leds.Step(time/tmax, BRIGHTNESS_MIN, BRIGHTNESS_MAX)
            if time > tmax:
                print('Stop')
                leds.Flash(timeout = T_FLASH)
                #
        else:
            # continue adding time to t0 to resume where we stopped
            t0 = ticks_ms()-time
            print('Pause block', t0, FLAG_START)


try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()
