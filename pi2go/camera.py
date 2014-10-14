# This is a work in process currently - I am trying to craft an elegant solution to the camera problem!
# As of current the user is going to need the camera software installed.

import subprocess

subprocess.call("./camera/camera_install.sh", "start")

try:
    subprocess.call("./camera/camera_install.sh", "start")
    
finally:
    subprocess.call("./camera/camera_install.sh", "stop")
    
