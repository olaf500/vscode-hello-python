#!/usr/bin/env python3
'''test ev3dev library'''


from ev3dev2.motor import LargeMotor
import os
from time import sleep

os.system('setfont Lat15-TerminusBold14')

mL = LargeMotor('outB'); mL.stop_action = 'hold'
mR = LargeMotor('outC'); mR.stop_action = 'hold'

mL.on_for_rotations(speed=50, rotations=2)

sleep(1)
