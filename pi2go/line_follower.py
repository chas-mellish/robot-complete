# Pi2Go 'follower sketch' - for the third episode of my robot tutorial series
# This program is also fairly simple - it utilises the Line IRs
# on the Pi2Go in order to sense obstacles and avoid them
# Created by Matthew Timmons-Brown and Simon Beal

import pi2go, time

pi2go.init()

# Here we set the speed to 40 out of 100 - feel free to change!
speed = 60

try:
  while True:
    left = pi2go.irLeftLine()
    right = pi2go.irRightLine()
    if left == right:
      # Forward
      pi2go.forward(speed)
    elif left == True:
      # Left
      pi2go.spinRight(speed)
    elif right == True:
      # Right
      pi2go.spinLeft(speed)

finally: # Even if there was an error, cleanup
  pi2go.cleanup()
