import subprocess

try:
    subprocess.call("./camera/camera_install.sh", "start")
    
finally:
    subprocess.call("./camera/camera_install.sh", "stop")
    
