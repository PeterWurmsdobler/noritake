from noritake.gu600_comms import GU600CommsSPI
from noritake.gu600_config import GU600Models
from noritake.gu600_driver import GU600Driver
from noritake.gu600_enums import ExtendedFontFace, FontProportion, FontSpace


def main() -> None:
    text = [
        "Glenn Gould (1982)       -12dB",
        "Johann Sebastian Bach         ",
        "Goldberg Variations           ",
        "Variatio 10.             01:12",
    ]

    cfg = GU600Models["GU240x64D-K612A8"]
    spi = GU600CommsSPI(0, 0)
    vfd = GU600Driver(spi, cfg)
    vfd.clear_all()
    vfd.select_extended_font(
        ExtendedFontFace.FONTFACE_7x15A,
        FontProportion.FONT_FIXEDSPACE,
        FontSpace.FONTSPACE_1PIXEL,
    )
    for i in range(4):
        vfd.write_text(0, i * 17 + 16, text[i])


if __name__ == "__main__":
    main()
