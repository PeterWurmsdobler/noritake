# Noritake Display driver

This repository implements a driver for the Noritake Itron GU600 series of VFDs.

## Prerequisistes

The prerequisites for this package are in essence Python 3.7 and an SPI driver.

### Python 3.7

To install python 3.7 on a normal Raspberry Pi4 use `apt-get`:

```commandline
user@host:~$ sudo apt-get update
user@host:~$ sudo apt-get -y install python3.7-dev
```

If Python 3.7 is not available as Debian package, then follow the instructions on [Install Python 3.7 on Raspberry PI](https://installvirtual.com/install-python-3-7-on-raspberry-pi/) to install from source. Only replace `3.7.0` with `3.7.9` to get the latest of `3.7`.


### SPI driver

This driver was designed to work for both asynchronous (UART and RS232) and synchronous communications such as SPI and I2C. For SPI to work the python driver has to be installed:

```commandline
user@host:~$ git clone https://github.com/doceme/py-spidev.git
user@host:~$ cd py-spidev
user@host:~$ sudo python3.7 ./setup.py install
```

### Pi4 pin assignments

If the Noritake Itron GU600 VFD is connected to a Raspberry Pi4, then the following pins have to be connected to enable communication over SPI0:

| VFD pin | VFD signal  | RPi4 pin | RPi4 signal          |
| :-----: |:------------| :------: |:---------------------|
|    1    |    VCC      |    2     |  5V Power            |
|    2    |    SCK      |   23     |  GPIO 11 (SPI0 SCLK) |
|    3    |    /SS      |   24     |  GPIO  8 (SPI0 CE0)  |
|    4    |    SIN      |   19     |  GPIO 10 (SPI0 MOSI) |
|    5    |    GND      |   20     |  Ground              |
|    6    |    SOUT     |   21     |  GPIO  9 (SPI0 MISO) |


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
