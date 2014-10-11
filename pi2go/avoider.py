# Pi2Go 'avoider sketch' - for the second episode of my robot tutorial series
# This program is fairly simple - it utilises the IR and ultrasonic sensors
# on the Pi2Go in order to sense obstacles and avoid them
# Created by Matthew Timmons-Brown and Simon Beal

# Imports the library
import pi2go

# Intialises the library
pi2go.init()

# Here we set the speed to 40 out of 100 - feel free to change!
speed = 40

# Here is the main body of the program - a lot of while loops and ifs!
# In order to get your head around it go through the logical steps slowly!
try:
  while True:
    if pi2go.irLeft():
      while pi2go.irLeft():
        # While the left sensor is true - spin right
        pi2go.spinRight(speed)
      # This stops the motors
      pi2go.stop()
    if pi2go.irRight():
      while pi2go.irRight():
        # While the right sensor is true - spin left
        pi2go.spinLeft(speed)
      pi2go.stop()
    while not (pi2go.irLeft() or pi2go.irRight()):
      # While the IR sensors aren't detecting anything, try the ultrasonic!
      if pi2go.getDistance() <= 3:
        pi2go.spinRight(speed)
      else:
        pi2go.forward(speed)
    pi2go.stop()

# Cleans up your program nicely
finally:
  pi2go.cleanup()
