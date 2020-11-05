import subprocess 

interface = wlan0

print("{+} Changing MAC for " + interface)
subprocess.call(
