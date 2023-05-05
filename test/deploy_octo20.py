# deploy - for upy v.1.20 - 2023/05

from time import sleep
import network

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
print("scan")
print(sta_if.scan())                             
sta_if.connect('ssid', 'password')
print("is_connected",sta_if.isconnected())

sleep(5)
import mip
print("[mip] micropython-octopuslab-installer")
mip.install("github:octopuslab-cz/octopuslab-installer", target=".")

sleep(5)
print("deploy")
import octopuslab_installer
octopuslab_installer.deploy()  #ImportError: no module named 'lib' ...