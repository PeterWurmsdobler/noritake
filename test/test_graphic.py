import noritake.gu600_driver as GU600
from noritake.gu600_comms import GU600CommsSPI
from noritake.gu600_enums import *


def main() -> None:
    mandl = [0x1C, 0x5C, 0x48, 0x3E, 0x1D, 0x1D, 0x14, 0x36]
    cyclist1 = [
        0x00,
        0x00,
        0x00,
        0x00,
        0x07,
        0x04,
        0xC7,
        0xFE,
        0x72,
        0x73,
        0x32,
        0x3E,
        0x3F,
        0x1D,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
    ]
    cyclist2 = [
        0x00,
        0x3C,
        0x42,
        0x81,
        0xB9,
        0xC1,
        0x42,
        0x7C,
        0x20,
        0xD8,
        0xFC,
        0x3C,
        0xFC,
        0xCA,
        0x49,
        0xB1,
        0x89,
        0x42,
        0x3C,
        0x00,
    ]

    spi = GU600CommsSPI(0, 0)
    vfd = GU600.GU600Driver(spi)
    vfd.send_ClearArea(0, 0, 240, 64)
    vfd.send_WriteMode(
        GraphicOrientation.ORIENTATION_HORIZONTAL,
        CursorMovement.MOVEMENT_VERTICAL,
        CursorDirection.DIRECTION_FORWARD,
        UnderScoreCursor.UNDERSCORECURSOR_STATICOFF,
    )
    vfd.send_CursorPosition(0x1F, 0x1C)
    vfd.send_GraphicWrite(mandl)

    vfd.send_WriteMode(
        GraphicOrientation.ORIENTATION_VERTICAL,
        CursorMovement.MOVEMENT_HORIZONTAL,
        CursorDirection.DIRECTION_FORWARD,
        UnderScoreCursor.UNDERSCORECURSOR_STATICOFF,
    )
    vfd.send_CursorPosition(0x48, 0x08)
    vfd.send_GraphicWrite(cyclist1)
    vfd.send_CursorPosition(0x48, 0x10)
    vfd.send_GraphicWrite(cyclist2)


if __name__ == "__main__":
    main()