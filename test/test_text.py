import noritake.gu600_driver as GU600
from noritake.gu600_comms import GU600CommsSPI
from noritake.gu600_enums import *


def main() -> None:
    text = [
        "Glenn Gould (1982)       -12dB",
        "Johann Sebastian Bach         ",
        "Goldberg Variations           ",
        "Variatio 10.             01:12",
    ]

    spi = GU600CommsSPI(0, 0)
    vfd = GU600.GU600Driver(spi)
    vfd.clear_area(0, 0, 240, 64)
    vfd.select_extended_font(
        ExtendedFontFace.FONTFACE_7x15A,
        FontProportion.FONT_FIXEDSPACE,
        FontSpace.FONTSPACE_1PIXEL,
    )
    for i in range(4):
        vfd.write_text(0, i * 17 + 16, text[i])


if __name__ == "__main__":
    main()
