# Noritake Display driver

GU600 series.

## Prerequisistes

This package is written in Python 3.8.

This driver was designed to work for both asynchronous serial (UART and RS232) and synchronous communications such as SPI and I2C. For SPI to work the python driver has to be installed:

```bash
sudo apt-get update
sudo apt-get -y install python3.8-dev
git clone https://github.com/doceme/py-spidev.git
cd py-spidev
sudo python3.8 ./setup.py install
```

## Test

Run on a command shell:

```bash
python3.8 tests/display.py
```
