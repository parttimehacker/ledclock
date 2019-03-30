#!/usr/bin/python3
""" test ledclock.py """

from threading import Lock

import ledclock

if __name__ == '__main__':
    LOCK = Lock()
    DISPLAY = ledclock.LedClock(LOCK)
    DISPLAY.run()

    while True:
        # simple input driver
        COMMAND = input("> ")
        if COMMAND == 'e':
            print("exiting")
            break
        elif COMMAND == 'a':
            DISPLAY.set_alarm(True)
        elif COMMAND == 'o':
            DISPLAY.set_alarm(False)
        elif COMMAND == 't':
            DISPLAY.set_mode(ledclock.TIME_MODE)
        elif COMMAND == 'w':
            DISPLAY.set_mode(ledclock.WHO_MODE)
        elif COMMAND == 'c':
            DISPLAY.set_mode(ledclock.COUNT_MODE)
        else:
            print("a, e, o, t, w")
