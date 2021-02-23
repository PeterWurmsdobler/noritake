from enum import IntEnum


class GraphicOrientation(IntEnum):
    """Argument type used in 'send_write_mode'."""

    ORIENTATION_HORIZONTAL = 0
    ORIENTATION_VERTICAL = 1


class CursorMovement(IntEnum):
    """Argument type used in 'send_write_mode'."""

    MOVEMENT_HORIZONTAL = 0
    MOVEMENT_VERTICAL = 1


class CursorDirection(IntEnum):
    """Argument type used in 'send_write_mode'."""

    DIRECTION_FORWARD = (0,)
    DIRECTION_BACKWARDS = 1


class UnderScoreCursor(IntEnum):
    """Argument type used in 'send_write_mode'."""

    UNDERSCORECURSOR_STATICOFF = 0
    UNDERSCORECURSOR_FLASHOFF = 1
    UNDERSCORECURSOR_STATICON = 2
    UNDERSCORECURSOR_FLASHON = 3


class PenType(IntEnum):
    """Argument type used in 'send_write_mode'."""

    PENTYPE_OVER = 0
    PENTYPE_AND = 1
    PENTYPE_OR = 2
    PENTYPE_XOR = 3


class PacketMode(IntEnum):
    """Argument type used in 'set_serial_config'."""

    PACKETMODE_OFF = 0
    PACKETMODE_ON = 1


class AutomaticSend(IntEnum):
    """Argument type used in 'set_serial_config'."""

    AUTOMATICSEND_OFF = 0
    AUTOMATICSEND_ON = 1


class CommsBuffer(IntEnum):
    """Argument type used in 'set_serial_config'."""

    COMMSBUFFER_OFF = 0
    COMMSBUFFER_ON = 1


class Parity(IntEnum):
    """Argument type used in 'set_serial_config'."""

    PARITY_NONE = 0
    PARITY_EVEN = 1


class BaudeRate(IntEnum):
    """Argument type used in 'set_serial_config'."""

    BAUDRATE_4800 = 0
    BAUDRATE_9600 = 1
    BAUDRATE_19200 = 2
    BAUDRATE_38400 = 3
    BAUDRATE_57600 = 4
    BAUDRATE_76800 = 5
    BAUDRATE_1200 = 6
    BAUDRATE_2400 = 7


class FontFace(IntEnum):
    """Argument type used in 'select_font'."""

    PROPORTIONAL_MINI = 0x1C
    FIXEDSPACED_5X7 = 0x1D
    FIXEDSPACED_10x14 = 0x1E


class ExtendedFontFace(IntEnum):
    """Argument type used in 'select_extended_font'."""

    FONTFACE_5x5A = 0x00
    FONTFACE_5x7A = 0x01
    FONTFACE_10x14A = 0x02
    FONTFACE_7x15A = 0x03
    FONTFACE_5x7C = 0x04
    FONTFACE_10x14C = 0x05


class FontProportion(IntEnum):
    """Argument type used in 'select_extended_font'."""

    FONT_FIXEDSPACE = 0
    FONT_PROPORTIONAL = 1


class FontSpace(IntEnum):
    """Argument type used in 'select_extended_font'."""

    FONTSPACE_1PIXEL = 0
    FONTSPACE_2PIXEL = 1
    FONTSPACE_3PIXEL = 2
    FONTSPACE_4PIXEL = 3
    FONTSPACE_5PIXEL = 4
    FONTSPACE_6PIXEL = 5
    FONTSPACE_7PIXEL = 6
    FONTSPACE_8PIXEL = 7


class WindowMode(IntEnum):
    """Argument type used in 'set_window_mode'."""

    WINDOWMODE_INVERT = 0
    WINDOWMODE_CLEAR = 1
    WINDOWMODE_FILL = 2
    WINDOWMODE_PATTERN = 3


class FlashTime(IntEnum):
    """Argument type used in 'set_window_flash_speed'."""

    FLASHTIME_15ms = 0
    FLASHTIME_30ms = 1
    FLASHTIME_45ms = 2
    FLASHTIME_100ms = 3
    FLASHTIME_150ms = 4
    FLASHTIME_200ms = 5
    FLASHTIME_250ms = 6
    FLASHTIME_350ms = 7
    FLASHTIME_500ms = 8
    FLASHTIME_750ms = 9
    FLASHTIME_1_0sec = 10
    FLASHTIME_1_5sec = 11
    FLASHTIME_2_0sec = 12
    FLASHTIME_2_5sec = 13
    FLASHTIME_3_0sec = 14
    FLASHTIME_3_5sec = 15


class WipeEffect(IntEnum):
    """Argument type used in 'set_window_wipe_effect'."""

    WIPEEFFECT_LEFT_TO_RIGHT_COVER = 0x00
    WIPEEFFECT_RIGHT_TO_LEFT_COVER = 0x01
    WIPEEFFECT_TOP_TO_BOTTOM_COVER = 0x02
    WIPEEFFECT_BOTTOM_TO_TOP_COVER = 0x03
    WIPEEFFECT_LEFT_TO_RIGHT_UNCOVER = 0x04
    WIPEEFFECT_RIGHT_TO_LEFT_UNCOVER = 0x05
    WIPEEFFECT_TOP_TO_BOTTOM_UNCOVER = 0x06
    WIPEEFFECT_BOTTOM_TO_TOP_UNCOVER = 0x07
    WIPEEFFECT_HORIZONTAL_CENTRE_TO_EDGE_COVER = 0x08
    WIPEEFFECT_HORIZONTAL_EDGE_TO_CENTRE_UNCOVER = 0x09
    WIPEEFFECT_VERTICAL_CENTRE_TO_EDGE_COVER = 0x0A
    WIPEEFFECT_VERTICAL_EDGE_TO_CENTRE_UNCOVER = 0x0B


class WipeSpeed(IntEnum):
    """Argument type used in 'set_window_wipe_speed'."""

    WIPESPEED_HALT = 0x00
    WIPESPEED_17HZ = 0x01
    WIPESPEED_35HZ = 0x02
    WIPESPEED_52HZ = 0x03
    WIPESPEED_70HZ = 0x04
    WIPESPEED_87HZ = 0x05
    WIPESPEED_105HZ = 0x06
    WIPESPEED_122HZ = 0x07
    WIPESPEED_140HZ = 0x08
    WIPESPEED_157HZ = 0x09
    WIPESPEED_175HZ = 0x0A
    WIPESPEED_192HZ = 0x0B
    WIPESPEED_210HZ = 0x0C
    WIPESPEED_227HZ = 0x0D
    WIPESPEED_245HZ = 0x0E
    WIPESPEED_262HZ = 0x0F
    WIPESPEED_315HZ = 0x10


class PatternType(IntEnum):
    """Argument type used in 'select_window_pattern'."""

    PATTERNTYPE_FULL = 0x00
    PATTERNTYPE_HALF = 0x01
    PATTERNTYPE_45ASCEND = 0x02
    PATTERNTYPE_45DESCEND = 0x03
    PATTERNTYPE_VZIGZAG = 0x04
    PATTERNTYPE_HZIGZAG = 0x05
    PATTERNTYPE_45GRID = 0x06
    PATTERNTYPE_MESH = 0x07
    PATTERNTYPE_SQUARES1 = 0x08
    PATTERNTYPE_SQUARES2 = 0x09
    PATTERNTYPE_SQUARES3 = 0x0A
    PATTERNTYPE_DIAMONDS = 0x0B
    PATTERNTYPE_SQUARES4 = 0x0C
    PATTERNTYPE_CIRCLES = 0x0D
    PATTERNTYPE_SHADES1 = 0x0E
    PATTERNTYPE_SHADES2 = 0x0F


class InvertPattern(IntEnum):
    """Argument type used in 'set_window_pattern_option'."""

    INVERTPATTERN_OFF = 0
    INVERTPATTERN_ON = 1


class PatternAlignment(IntEnum):
    """Argument type used in 'set_window_pattern_option'."""

    PATTERNALIGNMENT_OFF = 0
    PATTERNALIGNMENT_ON = 1


class PatternAlignV(IntEnum):
    """Argument type used in 'set_window_pattern_option'."""

    PATTERNALIGN_BOTTOM = 0
    PATTERNALIGN_TOP = 1


class PatternAlignH(IntEnum):
    """Argument type used in 'set_window_pattern_option'."""

    PATTERNALIGN_RIGHT = 0
    PATTERNALIGN_LEFT = 1


class ScrollSpeed(IntEnum):
    """Argument type used in 'set_scroll_speed'."""

    SCROLLSPEED_HALT = 0x00
    SCROLLSPEED_35HZ = 0x01
    SCROLLSPEED_70HZ = 0x02
    SCROLLSPEED_105HZ = 0x03
    SCROLLSPEED_140HZ = 0x04
    SCROLLSPEED_175HZ = 0x05
    SCROLLSPEED_210HZ = 0x06
    SCROLLSPEED_245HZ = 0x07
    SCROLLSPEED_315HZ = 0x08


class PadEndOfText(IntEnum):
    """Argument type used in 'set_scroll_text_in_window'."""

    PADENDOFTEXT_OFF = 0
    PADENDOFTEXT_ON = 1


class ScrollContents(IntEnum):
    """Argument type used in 'set_scroll_text_in_window'."""

    SCROLLCONTENTS_OFF = 0
    SCROLLCONTENTS_ON = 1


class ScrollDirection(IntEnum):
    """Argument type used in 'set_scroll_text_in_window'."""

    SCROLLDIRECTION_UP = 0
    SCROLLDIRECTION_DOWN = 1
    SCROLLDIRECTION_LEFT = 2
    SCROLLDIRECTION_RIGHT = 3


class Luminance(IntEnum):
    """Argument type used in 'set_auto_fade'."""

    LUMINANCE_0 = 0
    LUMINANCE_14 = 1
    LUMINANCE_28 = 2
    LUMINANCE_43 = 3
    LUMINANCE_57 = 4
    LUMINANCE_71 = 5
    LUMINANCE_86 = 6
    LUMINANCE_100 = 7


class FadeSpeed(IntEnum):
    """Argument type used in 'set_auto_fade'."""

    FADESPEED_FASTEST = 0
    FADESPEED_FAST = 1
    FADESPEED_SLOW = 2
    FADESPEED_SLOWEST = 3
