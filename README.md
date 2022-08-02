# OctopusLab Init Lite

This module facilitates provisioning of ESP32 boards with MicroPython projects.

We use it for deployment of [OctopusLab tools](https://docs.octopuslab.cz/) on ESP32 boards (all examples bellow), but it may work on other MicroPython ports as well.

Purpose of this tool is to download a `.tar` file and unpack it to the file storage over existing content.

Alternatively tar archive si stored locally for later offline restore a.k.a. factory reset.

In the future optional wipe of dangling files will be added.

## How to use?

Bootstrap your ESP32 with latest MicroPython [documentation](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro)

```
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin
screen /dev/ttyUSB0 115200
```

Connect to WiFi
```
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('essid', 'password')
```

Install
```
import upip
upip.install('micropython-octopuslab-installer')
```

Run
```
from octopuslab_installer import deploy
deploy()
```

After this OctopusLab from `https://octopusengine.org/download/micropython/stable.tar` is installed in your ESP **don't forget to reboot**.

Please proceed with inital configuration of your OctopusLab enabled board as per [documentation](https://docs.octopuslab.cz/install/#setup-nastaveni-systemu)

## Alternative images

You may like to install an image from your custom location.

```
from octopuslab_installer import deploy
deploy('http://192.168.1.100:8000/latest.tar')
```

Optionally you may store downloaded image for later offline restore.

```
from octopuslab_installer import deploy
deploy('https://www.dtlab.cz/download/sensobox/latest.tar', '/img/latest.tar')
```

Then you may redeploy offline from the local file as follows. This may be used for "factory reset" of your device.

```
from octopuslab_installer import deploy
deploy('/img/latest.tar')
```

Also you may use wifi connection shortcut if you redeploy updated image and you've lost connection e.g. due to a reboot.

```
from octopuslab_installer import connect
connect('myssid', 'mypass')
```

# Build and publish new version of this module

```
# initial setup of build environment
git clone git@github.com:octopusengine/octopuslab-installer.git
cd octopuslab-installer/
python3 -m venv venv
source ./venv/bin/activate
pip install --upgrade wheel setuptools

# PyPi publisher and authorisation
pip install --upgrade twine
mcedit ~/.pypirc
chmod o-rwx ~/.pypirc

# build command
python setup.py sdist

# publish
twine upload -r pypi dist/*
```
