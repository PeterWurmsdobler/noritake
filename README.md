# Noritake Display driver

This repository implements a driver for the Noritake Itron GU600 series of VFDs.

## Prerequisistes

This package is written for Python 3.7. Make sure python3.8 is installed on your system.

```commandline
user@host:~$ sudo apt-get update
user@host:~$ sudo apt-get -y install python3.8-dev
```

This driver was designed to work for both asynchronous (UART and RS232) and synchronous communications such as SPI and I2C. 

For SPI to work the python driver has to be installed:

```commandline
user@host:~$ git clone https://github.com/doceme/py-spidev.git
user@host:~$ cd py-spidev
user@host:~$ sudo python3.7 ./setup.py install
```

## Install

Install the package by cloning the repository, change into the repo and run the installation, like:

```commandline
user@host:~$ git clone https://github.com/PeterWurmsdobler/noritake.git
user@host:~$ cd noritake
user@host:~$ sudo python3.7 ./setup.py install
```

## Test

Provided the package has been installed, run on a command shell:

```commandline
user@host:~$ python3.7 test/test_text.py
user@host:~$ python3.7 test/test_graphic.py
```

## Usage

Provided the package has been installed, you can create a python program:

```python
from noritake.gu600_comms import GU600CommsSPI
from noritake.gu600_config import GU600Models
from noritake.gu600_driver import GU600Driver
from noritake.gu600_enums import ExtendedFontFace, FontProportion, FontSpace

cfg = GU600Models["GU240x64D-K612A8"]
spi = GU600CommsSPI(0, 0)
vfd = GU600Driver(spi, cfg)
vfd.clear_all()
vfd.select_extended_font(
    ExtendedFontFace.FONTFACE_7x15A,
    FontProportion.FONT_FIXEDSPACE,
    FontSpace.FONTSPACE_1PIXEL,
)
vfd.write_text(10, 20, "Hello World")
```
