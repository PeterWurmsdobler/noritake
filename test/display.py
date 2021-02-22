import sys

import noritake.gu600_driver as GU600
from noritake.gu600_enums import *
from noritake.gu600_comms import GU600CommsSPI


def usage() -> None:
    print("vfd.py <command> [args...]")
    print("     write <string>")
    print("     goto <x> <y>")
    print("     cls")
    sys.exit(-1)


def main() -> None:
    text = [
        "Glenn Gould (1982)       -12dB",
        "Johann Sebastian Bach         ",
        "Goldberg Variations           ",
        "Variatio 10.                  ",
    ]

    spi = GU600CommsSPI(0, 0)
    vfd = GU600.GU600Driver(spi)
    vfd.send_ClearArea(0, 0, 240, 64)
    vfd.send_SelectExtendedFont(
        ExtendedFontFace.FONTFACE_7x15A,
        FontProportion.FONT_FIXEDSPACE,
        FontSpace.FONTSPACE_1PIXEL,
    )
    for i in range(4):
        vfd.send_Text(0, i * 17 + 16, text[i])


if __name__ == "__main__":
    main()
