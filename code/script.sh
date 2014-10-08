# Simple script to install a few bits of software for the Pi2Go-lite
# I have left the Pi2Go bits in - just so that everything works in the library
# Also some people will want to play around with the extra stuff!

wget -q https://github.com/the-raspberry-pi-guy/pi2go/blob/master/extra_software/servod.xxx -O servod
wget -q http://4tronix.co.uk/pi2go/Adafruit_PWM_Servo_Driver.py -O Adafruit_PWM_Servo_Driver.py
wget -q http://4tronix.co.uk/pi2go/Adafruit_I2C.py -O Adafruit_I2C.py
wget -q http://4tronix.co.uk/pi2go/sgh_PCF8591P.pyc -O sgh_PCF8591P.pyc
chmod +x servod
