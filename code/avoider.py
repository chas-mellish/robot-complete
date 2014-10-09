#!/usr/bin/env python
#Avoids walls based on the sonar and IR sensors

# Must be run as root - sudo python .py 

import pi2go

pi2go.init()

vsn = pi2go.version()
if vsn == 1:
  print "Running on Pi2Go (NOT BEEN TRIALLED FOR THIS)"
else:
  print "Running on Pi2Go-Lite"

speed = 30
turn_distance = 3
turn_amount = 2

try:
  while True:
    if pi2go.irLeft():
      while pi2go.irLeft():
        pi2go.spinRight(speed)
      pi2go.stop()
    if pi2go.irRight():
      while pi2go.irRight():
        pi2go.spinLeft(speed)
      pi2go.stop()
    while not (pi2go.irLeft() or pi2go.irRight()):
      if pi2go.getDistance() <= turn_distance:
        pi2go.stepSpinR(speed, turn_amount)
      pi2go.forward(speed)
    pi2go.stop()

finally:
  pi2go.cleanup()
