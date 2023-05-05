# deploy - for upy v.1.19 - 2022/09

from time import sleep

import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
sleep(5)
print("wifi connect")
wlan.connect('ssid', 'password')

sleep(5)
print("upip: micropython-octopuslab-installer")
import upip
upip.install('micropython-octopuslab-installer')

sleep(5)
print("deploy")
from lib import octopuslab_installer
octopuslab_installer.deploy()