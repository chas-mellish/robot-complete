# Simple script to install a few bits of software for the Pi2Go-lite
# I have left the Pi2Go bits in - just so that everything works in the library
# Also some people will want to play around with the extra stuff!
# Essentially you will download this twice but I thought that it was best for clarity and neatness
# Plus I have nowhere else *reliable* to host it!

echo "Just installing that stuff for you sir/madam! I'll be finished in a second!"
wget -q https://github.com/the-raspberry-pi-guy/pi2go/blob/master/extra_software/servod.xxx -O servod
wget -q https://raw.githubusercontent.com/the-raspberry-pi-guy/pi2go/master/extra_software/Adafruit_PWM_Servo_Driver.py -O Adafruit_PWM_Servo_Driver.py
wget -q https://raw.githubusercontent.com/the-raspberry-pi-guy/pi2go/master/extra_software/Adafruit_I2C.py -O Adafruit_I2C.py
wget -q https://github.com/the-raspberry-pi-guy/pi2go/blob/master/extra_software/sgh_PCF8591P.pyc -O sgh_PCF8591P.pyc
chmod +x servod
