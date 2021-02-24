from typing import List

from noritake.gu600_comms import GU600Comms
from noritake.gu600_config import GU600Config
from noritake.gu600_enums import *

PACKET_HEADER = 0x02
PACKET_FOOTER = 0x03
VFDACK = 0x50
MAX_MESSAGE_SIZE = 256
BRIGHTNESS_LEVELS = 8


class GU600Driver:
    def __init__(self, comms_link: GU600Comms, config: GU600Config) -> None:
        self._comms_link = comms_link
        self._config = config

    @property
    def config(self) -> GU600Config:
        return self._config

    def write(self, message: List[int]) -> bool:
        """Write a sequence of words to device."""
        return self._comms_link.write(message)

    def send_dummy_byte(self) -> bool:
        """Send a dummy byte."""
        return self.write([0x00])

    def send_macro_start(self, marcoNumber: int) -> bool:
        """Start user defined macro 1-7."""
        return self.write([self._minmax(0, marcoNumber, 7)])

    def send_backspace(self) -> bool:
        """Non destructive backspace. The cursor is moved left by the width of the currently select font. If
        the cursor is at the left end of the display, no cursor movement is made."""
        return self.write([0x08])

    def move_curser_horizontal_tab(self) -> bool:
        """Cursor is moved right by the width of the currently select font. If the cursor is at the end of the
        display, no cursor movement is made."""
        return self.write([0x09])

    def move_curser_line_feed(self) -> bool:
        """Moves the cursor down by the height of the currently selected font. If the cursor is at the bottom
        of the display, no cursor movement is made."""
        return self.write([0x0A])

    def move_curser_home(self) -> bool:
        """Moves the cursor horizontal position to 00H, the vertical positioning is dependent on the currently
        selected font, allowing for immediate character writing in the top-left corner of the display."""
        return self.write([0x0B])

    def move_curser_vertical_tab(self) -> bool:
        """Moves the cursor up one character row. If the cursor is at the top of the top end of the display, no
        cursor movement is made."""
        return self.write([0x0C])

    def move_curser_carriage_return(self) -> bool:
        """Moves the cursor horizontal position to 00H. The vertical position is unchanged."""
        return self.write([0x0D])

    def clear_EOL(self) -> bool:
        """Clear all characters from the current cursor position to the end of the display."""
        return self.write([0x0E])

    def send_test(self) -> bool:
        """Place module into self-test mode. The module will repetitively show a few test screens. The test
        mode will stop on the next received byte."""
        return self.write([0x0F])

    def set_cursor_position(self, x: int, y: int) -> bool:
        """Sets the cursor position."""
        return self.write([0x10, x, y])

    def set_area(self, left: int, top: int, right: int, bottom: int) -> bool:
        """Fill specified area. All dots within the specified area are illuminated. Please note that the cursor
        position is affected with this command."""
        return self._send_area_command(0x11, left, top, right, bottom)

    def clear_area(self, left: int, top: int, right: int, bottom: int) -> bool:
        """Clear specified area. All dots within the specified area are cleared. Please note that the cursor
        position is affected with this command."""
        return self._send_area_command(0x12, left, top, right, bottom)

    def clear_all(self) -> bool:
        """Clear entire screen. Please note that the cursor position is affected with this command."""
        return self.clear_area(0, 0, self._config.width - 1, self._config.height - 1)

    def invert_area(self, left: int, top: int, right: int, bottom: int) -> bool:
        """Invert specified area. All dots within the specified area are inverted. Please note that the cursor
        position is affected with this command."""
        return self._send_area_command(0x13, left, top, right, bottom)

    def set_outline(self, left: int, top: int, right: int, bottom: int) -> bool:
        """Draw box outline. All dots within the specified outline are unchanged. Please note that the cursor
        position is affected with this command."""
        return self._send_area_command(0x14, left, top, right, bottom)

    def clear_outline(self, left: int, top: int, right: int, bottom: int) -> bool:
        """Clear box outline. All dots within the specified outline are unchanged. Please note that the cursor
        position is affected with this command."""
        return self._send_area_command(0x15, left, top, right, bottom)

    def set_pixel(self) -> bool:
        """Illuminate a single pixel at the current cursor position."""
        return self.write([0x16])

    def clear_pixel(self) -> bool:
        """Clear a single pixel at the current cursor position."""
        return self.write([0x17])

    def write_graphic(self, data: List[int]) -> bool:
        """Write graphical data, length, direct to display. See write mode command (1AH) for graphic
        orientation and cursor movements."""
        message: List[int] = [0x18, len(data)]
        message.extend(data)
        return self.write(message)

    def reset(self) -> bool:
        """Resets display to power-on defaults:"""
        return self.write([0x19])

    def set_write_mode(
        self,
        graphicOrientation: GraphicOrientation,
        cursorMovement: CursorMovement,
        cursorDirection: CursorDirection,
        underScoreCursor: UnderScoreCursor,
        penType: PenType,
    ) -> bool:
        """Set the write mode according to the
        'GraphicOrientation', 'CursorMovement',
        'CursorDirection', 'UnderScoreCursor', and 'PenType'."""
        message: List[int] = [
            0x1A,
            (graphicOrientation << 7)
            + (cursorMovement << 6)
            + (cursorDirection << 5)
            + (underScoreCursor << 3)
            + penType,
        ]
        return self.write(message)

    def set_macro(self, macroNumber: int, data: List[int]) -> bool:
        """Send macro data to EEPROM. Macro Number = 00H - 07H. Macro 0 is executed at power-up
        only. A maximum of 472 bytes is allowed for macro data. The display may flicker whilst writing
        macro data."""
        message: List[int] = [0x1B, self._minmax(0, macroNumber, 7), len(data)]
        message.extend(data)
        return self.write(message)

    def set_brightness(self, brightness: int) -> bool:
        """Select one of the eight brightness levels ranging from F8H to FFH."""
        message: List[int] = [
            0x1B,
            0xF8 + self._minmax(0, brightness, BRIGHTNESS_LEVELS - 1),
        ]
        return self.write(message)

    def erase_macros(self) -> bool:
        """Clear all downloaded macros in EEPROM. Screen may blank momentarily while macro data is
        being erased."""
        return self.write([0x1B, 0x4D])

    def lock_EEPROM(self) -> bool:
        """All data contained within the non-volatile EEPROM is locked (4CH), and no changes are possible
        until the unlock command (55H) is executed."""
        return self.write([0x1B, 0x4C])

    def unlock_EEPROM(self) -> bool:
        """Unlock EEPROM to permit configuration data being sent."""
        return self.write([0x1B, 0x55])

    def send_checksum(self) -> bool:
        """All data received is added to the checksum. This command will read the lower 8-bits of that
        checksum, before being cleared. Please note that the checksum is cleared when executing the
        test mode."""
        return self.write([0x1B, 0x43])

    def power_on(self) -> bool:
        """Turn on VFD power supply (default)."""
        return self.write([0x1B, 0x50])

    def power_off(self) -> bool:
        """Turn off VFD power supply (The display’s contents will be preserved)."""
        return self.write([0x1B, 0x46])

    def set_hex_mode(self) -> bool:
        """Enable hex receive mode, character 60H is interpreted as a hexadecimal prefix."""
        return self.write([0x1B, 0x48])

    def set_binary_mMode(self) -> bool:
        """Disable hex receive mode."""
        return self.write([0x1B, 0x42])

    def set_serial_config(
        self,
        automaticSend: AutomaticSend,
        packetMode: PacketMode,
        commsBuffer: CommsBuffer,
        parity: Parity,
        baudeRate: BaudeRate,
    ) -> bool:
        """Set Asynchronous Communications, this command takes affect at power-up or hardware reset, using
        'AutomaticSend', 'PacketMode', 'CommsBuffer', 'Parity', and 'BaudeRate'."""
        message: List[int] = [
            0x1B,
            0x49,
            (automaticSend << 7)
            + (packetMode << 6)
            + (commsBuffer << 5)
            + (parity << 3)
            + baudeRate,
        ]
        return self.write(message)

    def enable_IO_port(self, data: int) -> bool:
        """Set I/O port direction. A ‘1’ indicates an input, a ‘0’ an output. All output lines are immediately set
        low. All input lines have their pull-ups enabled. This value is stored in EEPROM and will
        automatically be set at power up."""
        return self.write([0x1B, 0x44, data])

    def set_port_lines(self, data: int) -> bool:
        """Set Output lines on I/O port, a ‘1’ will set 5V on the output ports, or enable the pull-ups on the
        inputs."""
        return self.write([0x1B, 0x4F, data])

    def read_port(self) -> bool:
        """Read current I/O port status. A single byte is transmitted showing the current state of the I/O lines."""
        return self.write([0x1B, 0x52])

    def enable_key_scanning(self) -> bool:
        """Set I/O port to key scanning. The I/O ports are continuously scanned for any key press. This
        mode is stored in EEPROM and will automatically be selected at power up."""
        return self.write([0x1B, 0x4B])

    def select_font(self, fontFace: FontFace) -> bool:
        "Select font according to specified enumerator 'FontFace'."
        return self.write([fontFace])

    def write_graphic_area(
        self, left: int, top: int, right: int, bottom: int, data: List[int]
    ) -> bool:
        """Write graphic data within defined area. See write mode command (1AH) for graphic orientation
        and cursor movements."""
        message: List[int] = [0x1F, left, top, right, bottom]
        message.extend(data)
        return self.write(message)

    def write_character(self, c: int) -> bool:
        """Display character from selected font."""
        return self.write([self._minmax(0x20, c, 0xFF)])

    def select_window1(self) -> bool:
        """Select window 1 so that window and area command functions operate on the underlying data or
        text scroll."""
        return self.write([0x1B, 0x80])

    def select_window2(self) -> bool:
        """Select window 2 so that window and area command functions operate on the underlying data."""
        return self.write([0x1B, 0x81])

    def define_window(self, left: int, top: int, right: int, bottom: int) -> bool:
        """Define window co-ordinates."""
        return self.write([0x1B, 0x82, left, top, right, bottom])

    def set_window_mode(self, windowMode: WindowMode) -> bool:
        """Set window mode according to 'WindowMode'."""
        return self.write([0x1B, 0x52, windowMode])

    def show_window(self) -> bool:
        """Make selected window visible."""
        return self.write([0x1B, 0x84])

    def kill_window(self) -> bool:
        """Destroy selected window. Any scroll, flash and wipe effects will be stopped."""
        return self.write([0x1B, 0x85])

    def flash_window(self, number: int) -> bool:
        """Flash selected window’s underlying data. Flash type depends on window’s write mode.
        Number = number of flashes.
        FFH = infinite.
        00H = stop flashing."""
        return self.write([0x1B, 0x86, number])

    def set_window_flash_speed(self, flashOn: FlashTime, flashOff: FlashTime) -> bool:
        """Set flash rate of selected window according to 'FlashTime'."""
        return self.write([0x1B, 0x87, (flashOn << 4) + flashOff])

    def set_window_wipe_effect(self, wipeEffect: WipeEffect) -> bool:
        """Perform a wipe action on the selected window’s underlying data using 'WipeEffect'."""
        return self.write([0x1B, 0x88, wipeEffect])

    def set_window_wipe_speed(self, wipeSpeed: WipeSpeed) -> bool:
        """Set the wipe effect speed (pixels per second) for the selected window using 'WipeSpeed'."""
        return self.write([0x1B, 0x89, wipeSpeed])

    def select_window_pattern(self, patternType: PatternType) -> bool:
        """Select pre-defined pattern (00H-0FH) for window according to 'PatternType'."""
        return self.write([0x1B, 0x8D, patternType])

    def set_window_pattern_data(self, pattern: List[int]) -> bool:
        """A user 16x16 pixel pattern (32 bytes) can be defined for the selected window.
        All data should be in vertical format with D7 uppermost."""
        assert len(pattern) == 32
        message: List[int] = [0x1F, 0x8E]
        message.extend(pattern)
        return self.write(message)

    def set_window_pattern_option(
        self,
        invertPattern: InvertPattern,
        patternAlignment: PatternAlignment,
        patternAlignV: PatternAlignV,
        patternAlignH: PatternAlignH,
    ) -> bool:
        """Set window pattern options using:
        'InvertPattern', 'PatternAlignment', 'PatternAlignV', and 'PatternAlignH'."""

        message: List[int] = [
            0x1B,
            0x8F,
            (invertPattern << 3)
            + (patternAlignment << 2)
            + (patternAlignV << 1)
            + patternAlignH,
        ]
        return self.write(message)

    def set_scroll_text_in_window(
        self,
        padEndOfText: PadEndOfText,
        scrollContents: ScrollContents,
        scrollDirection: ScrollDirection,
        number: int,
        text: List[int],
    ) -> bool:
        """Scroll text data within area defined by window 1 using
        'PadEndOfText', 'ScrollContents', and 'ScrollDirection'.
        Text to be scrolled with 00H signalling end of text."""
        message: List[int] = [
            0x1B,
            0x90,
            (padEndOfText << 5) + (scrollContents << 4) + scrollDirection,
            number,
        ]
        message.extend(text)
        return self.write(message)

    def set_scroll_speed(self, scrollSpeed: ScrollSpeed) -> bool:
        """Set window 1 scroll speed (pixels per second) using 'ScrollSpeed'."""
        return self.write([0x1B, 0x91, scrollSpeed])

    def select_extended_font(
        self,
        extendedFontFace: ExtendedFontFace,
        fontProportion: FontProportion,
        fontSpace: FontSpace,
    ) -> bool:
        """Select extended font defined by 'ExtendedFontFace', 'FontProportion', and 'FontSpace'."""
        message: List[int] = [
            0x1B,
            0x98,
            (fontSpace << 4) + (fontProportion << 3) + extendedFontFace,
        ]
        return self.write(message)

    def draw_line(self, x: int, y: int) -> bool:
        """Draws line from current cursor position to specified x, y. Cursor position is updated to x, y."""
        return self.write([0x1B, 0x9A, x, y])

    def set_auto_fade(self, luminance: Luminance, fadeSpeed: FadeSpeed) -> bool:
        """Perform automatic fade to a defined level using 'Luminance' and 'FadeSpeed'."""
        return self.write([0x1B, 0x9C, luminance + (fadeSpeed << 4)])

    def set_command_delay(self, delay: int) -> bool:
        """Delay any pending commands by 'delay' in multiple of 10ms delay period."""
        return self.write([0x1B, 0x9F, delay])

    def write_text(self, x: int, y: int, text: str) -> bool:
        """Set the test at cursor position defined by x & y."""
        message: List[int] = [0x10, x, y]
        message.extend([ord(c) for c in text])
        return self.write(message)

    def _minmax(self, minumum: int, value: int, maximum: int) -> int:
        return min(max(minumum, value), maximum)

    def _send_area_command(
        self, command: int, left: int, top: int, right: int, bottom: int
    ) -> bool:
        return self.write([command, left, top, right, bottom])
