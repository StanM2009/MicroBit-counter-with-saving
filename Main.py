from microbit import *
import os
import time

def get_nv_data(name):
    try:
        with open(name) as f:
            v = int(f.read())
    except OSError:
        v = 0
        try:
            with open(name, "w") as f:
                f.write(str(v))
        except OSError:
            print("Can't create file %s" % name)
    except ValueError:
        print("invalid data in file %s" % name)
        v = 0
    return v


def set_nv_data(name, value):
    try:
        with open(name, "w") as f:
            f.write(str(value))
    except OSError:
        print("Can't write to file %s" % name)


count = get_nv_data("data.txt")
delay = 0
last_tick = 0

while True:
    delay += time.ticks_ms() - last_tick
    if delay >= 100 + (len(str(count)) -1) * 35:
        delay = 0
        display.scroll(count, delay=100, wait=False)
    if pin_logo.is_touched():
        count = 0
        set_nv_data("data.txt", count)
        delay = 0
        display.scroll(count, delay=100, wait=False)
    elif button_a.was_pressed():
        count += 1
        set_nv_data("data.txt", count)
        delay = 0
        display.scroll(count, delay=100, wait=False)
    elif button_b.was_pressed():
        count += 10
        set_nv_data("data.txt", count)
        delay = 0
        display.scroll(count, delay=100, wait=False)
    last_tick = time.ticks_ms()
