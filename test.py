
import time
import evdev
from evdev import *

time.sleep(2)
Inj = UInput()
Inj.write(ecodes.EV_KEY, ecodes.KEY_LEFTALT, 1)
Inj.write(ecodes.EV_KEY, ecodes.KEY_TAB, 1)
Inj.write(ecodes.EV_KEY, ecodes.KEY_LEFTALT, 0)
Inj.write(ecodes.EV_KEY, ecodes.KEY_TAB, 0)
Inj.syn()
