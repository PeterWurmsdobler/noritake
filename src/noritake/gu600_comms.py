import ctypes
from typing import List

import spidev

UInt8 = ctypes.c_uint8

PACKET_HEADER = 0x02
PACKET_FOOTER = 0x03
VFDACK = 0x50
MAX_MESSAGE_SIZE = 256
BRIGHTNESS_LEVELS = 8


class GU600Comms:
    def write(self, message: List[UInt8]) -> bool:
        pass


class GU600CommsSPI(GU600Comms):
    def __init__(self, spi_num: int, spi_ce: int) -> None:
        self.spi = spidev.SpiDev()
        self.spi.open(spi_num, spi_ce)
        # on raspberry pi zero w buster, speed was set to 1250000 and didn't work
        self.spi.max_speed_hz = 500000

    def write(self, message: List[UInt8]) -> bool:
        pass
        # self.spi.writeUInt8s([UInt8(0xFA, data])
        # time.sleep(0.00001)


class GU600CommsI2C(GU600Comms):
    def __init__(self) -> None:
        pass

    def write(self, message: List[UInt8]) -> bool:
        pass


class GU600CommsRS232(GU600Comms):
    def __init__(self, port: str, baud: int) -> None:
        pass

    def write(self, message: List[UInt8]) -> bool:
        pass
