import ctypes
from typing import List

from noritake.gu600_enums import *
from noritake.gu600_comms import GU600Comms

UInt8 = ctypes.c_uint8

PACKET_HEADER = 0x02
PACKET_FOOTER = 0x03
VFDACK = 0x50
MAX_MESSAGE_SIZE = 256
BRIGHTNESS_LEVELS = 8


class GU600Driver:
    def __init__(self, comms_link: GU600Comms) -> None:
        self.comms_link = comms_link

    def write(self, message: List[UInt8]) -> bool:
        return self.comms_link.write(message)

    def _minmax(self, minumum: int, value: int, maximum: int) -> int:
        return min(max(minumum, value), maximum)

    def send_DummyByte(self) -> bool:
        return self.write([UInt8(0x00)])

    def send_MacroStart(self, marcoNumber: int) -> bool:
        return self.write([UInt8(self._minmax(0, marcoNumber, 7))])

    def send_Backspace(self) -> bool:
        return self.write([UInt8(0x08)])

    def send_HorizontalTab(self) -> bool:
        return self.write([UInt8(0x09)])

    def send_LineFeed(self) -> bool:
        return self.write([UInt8(0x0A)])

    def send_Home(self) -> bool:
        return self.write([UInt8(0x0B)])

    def send_VerticalTab(self) -> bool:
        return self.write([UInt8(0x0C)])

    def send_CarriageReturn(self) -> bool:
        return self.write([UInt8(0x0D)])

    def send_ClearEOL(self) -> bool:
        return self.write([UInt8(0x0E)])

    def send_Test(self) -> bool:
        return self.write([UInt8(0x0F)])

    def send_CursorPosition(self, x: int, y: int) -> bool:
        return self.write([UInt8(0x10), UInt8(x), UInt8(y)])

    def _send_AreaCommand(
        self, command: UInt8, left: int, top: int, right: int, bottom: int
    ) -> bool:
        return self.write(
            [command, UInt8(left), UInt8(top), UInt8(right), UInt8(bottom)]
        )

    def send_SetArea(self, left: int, top: int, right: int, bottom: int) -> bool:
        return self._send_AreaCommand(UInt8(0x11), left, top, right, bottom)

    def send_ClearArea(self, left: int, top: int, right: int, bottom: int) -> bool:
        return self._send_AreaCommand(UInt8(0x12), left, top, right, bottom)

    def send_InvertArea(self, left: int, top: int, right: int, bottom: int) -> bool:
        return self._send_AreaCommand(UInt8(0x13), left, top, right, bottom)

    def send_SetOutline(self, left: int, top: int, right: int, bottom: int) -> bool:
        return self._send_AreaCommand(UInt8(0x14), left, top, right, bottom)

    def send_ClearOutline(self, left: int, top: int, right: int, bottom: int) -> bool:
        return self._send_AreaCommand(UInt8(0x15), left, top, right, bottom)

    def send_SetPixel(self) -> bool:
        return self.write([UInt8(0x16)])

    def send_ClearPixel(self) -> bool:
        return self.write([UInt8(0x17)])

    def send_GraphicWrite(self, data: List[UInt8]) -> bool:
        message: List[UInt8] = [UInt8(0x18)]
        message.extend(data)
        return self.write(message)

    def send_Reset(self) -> bool:
        return self.write([UInt8(0x19)])

    def send_WriteMode(
        self,
        graphicOrientation: GraphicOrientation,
        cursorMovement: CursorMovement,
        cursorDirection: CursorDirection,
        underScoreCursor: UnderScoreCursor,
        penType: PenType,
    ) -> bool:

        message: List[UInt8] = [
            UInt8(0x1A),
            UInt8(
                (graphicOrientation << 7)
                + (cursorMovement << 6)
                + (cursorDirection << 5)
                + (underScoreCursor << 3)
                + penType
            ),
        ]
        return self.write(message)

    def send_SetMacro(self, macroNumber: int, data: List[UInt8]) -> bool:
        message: List[UInt8] = [UInt8(0x1B), UInt8(self._minmax(0, macroNumber, 7))]
        message.extend(data)
        return self.write(message)

    def send_Brightness(self, brightness: int) -> bool:
        # 8 levels from 0xf8 to 0xff
        message: List[UInt8] = [
            UInt8(0x1B),
            UInt8(0xF8 + self._minmax(0, brightness, BRIGHTNESS_LEVELS - 1)),
        ]
        return self.write(message)

    def send_EraseMacros(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x4D)])

    def send_LockUnlockEEPROM(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x4C), UInt8(0x55)])

    def send_Checksum(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x43)])

    def send_PowerOn(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x50)])

    def send_PowerOff(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x46)])

    def send_HexMode(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x48)])

    def send_BinaryMode(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x42)])

    def send_SetSerialCommunications(
        self,
        automaticSend: AutomaticSend,
        packetMode: PacketMode,
        commsBuffer: CommsBuffer,
        parity: Parity,
        baudeRate: BaudeRate,
    ) -> bool:

        message: List[UInt8] = [
            UInt8(0x1B),
            UInt8(0x49),
            UInt8(
                (automaticSend << 7)
                + (packetMode << 6)
                + (commsBuffer << 5)
                + (parity << 3)
                + baudeRate
            ),
        ]
        return self.write(message)

    def send_EnableIOPort(self, data: UInt8) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x44), data])

    def send_SetPortLines(self, data: UInt8) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x4F), data])

    def send_ReadPort(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x52)])

    def send_EnableKeyScanning(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x4B)])

    def send_SelectFont(self, fontFace: FontFace) -> bool:
        return self.write([UInt8(fontFace)])

    def send_GraphicAreaWrite(
        self, left: int, top: int, right: int, bottom: int, data: List[UInt8]
    ) -> bool:
        message: List[UInt8] = [
            UInt8(0x1F),
            UInt8(left),
            UInt8(top),
            UInt8(right),
            UInt8(bottom),
        ]
        message.extend(data)
        return self.write(message)

    def send_CharacterWrite(self, c: UInt8) -> bool:
        return self.write([c])

    def send_Window1Select(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x80)])

    def send_Window2Select(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x81)])

    def send_WindowDefine(self, left: int, top: int, right: int, bottom: int) -> bool:
        return self.write(
            [
                UInt8(0x1B),
                UInt8(0x82),
                UInt8(left),
                UInt8(top),
                UInt8(right),
                UInt8(bottom),
            ]
        )

    def send_WindowMode(self, windowMode: WindowMode) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x52), UInt8(windowMode)])

    def send_WindowShow(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x84)])

    def send_WindowKill(self) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x85)])

    def send_WindowFlash(self, number: int) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x86), UInt8(number)])

    def send_WindowFlashSpeed(self, flashOn: FlashTime, flashOff: FlashTime) -> bool:
        message: List[UInt8] = [
            UInt8(0x1B),
            UInt8(0x87),
            UInt8((flashOn << 4) + flashOff),
        ]
        return self.write(message)

    def send_WindowWipeEffect(self, wipeEffect: WipeEffect) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x88), UInt8(wipeEffect)])

    def send_WindowWipeSpeed(self, wipeSpeed: WipeSpeed) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x89), UInt8(wipeSpeed)])

    def send_WindowPatternSelect(self, patternType: PatternType) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x8D), UInt8(patternType)])

    def send_WindowPatternData(self, pattern: List[UInt8]) -> bool:
        assert len(pattern) == 32
        message: List[UInt8] = [UInt8(0x1F), UInt8(0x8E)]
        message.extend(pattern)
        return self.write(message)

    def send_WindowPatternOption(
        self,
        invertPattern: InvertPattern,
        patternAlignment: PatternAlignment,
        patternAlignV: PatternAlignV,
        patternAlignH: PatternAlignH,
    ) -> bool:

        message: List[UInt8] = [
            UInt8(0x1B),
            UInt8(0x8F),
            UInt8(
                (invertPattern << 3)
                + (patternAlignment << 2)
                + (patternAlignV << 1)
                + patternAlignH
            ),
        ]
        return self.write(message)

    def send_ScrolltextInWindow(
        self,
        padEndOfText: PadEndOfText,
        scrollContents: ScrollContents,
        scrollDirection: ScrollDirection,
        number: int,
        text: List[UInt8],
    ) -> bool:

        message: List[UInt8] = [
            UInt8(0x1B),
            UInt8(0x90),
            UInt8((padEndOfText << 5) + (scrollContents << 4) + scrollDirection),
            UInt8(number),
        ]
        message.extend(text)
        return self.write(message)

    def send_ScrollSpeed(self, scrollSpeed: ScrollSpeed) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x91), UInt8(scrollSpeed)])

    def send_SelectExtendedFont(
        self,
        extendedFontFace: ExtendedFontFace,
        fontProportion: FontProportion,
        fontSpace: FontSpace,
    ) -> bool:

        message: List[UInt8] = [
            UInt8(0x1B),
            UInt8(0x98),
            UInt8((fontSpace << 4) + (fontProportion << 3) + extendedFontFace),
        ]
        return self.write(message)

    def send_DrawLine(self, x: int, y: int) -> bool:
        message: List[UInt8] = [
            UInt8(0x1B),
            UInt8(0x9A),
            UInt8(x),
            UInt8(y),
        ]
        return self.write(message)

    def send_AutoFade(self, luminance: Luminance, fadeSpeed: FadeSpeed) -> bool:
        message: List[UInt8] = [
            UInt8(0x1B),
            UInt8(0x9C),
            UInt8(luminance + (fadeSpeed << 4)),
        ]
        return self.write(message)

    def send_CommandDelay(self, delay: int) -> bool:
        return self.write([UInt8(0x1B), UInt8(0x9F), UInt8(delay)])

    def send_Text(self, x: int, y: int, text: str) -> bool:
        message: List[UInt8] = [UInt8(0x10), UInt8(x), UInt8(y)]
        message.extend([UInt8(ord(c)) for c in text])
        return self.write(message)
