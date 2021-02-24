from typing import Mapping


class GU600Config:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height


GU600Models: Mapping[str, GU600Config] = {
    "GW64x16C-K610A": GU600Config(64, 16),
    "GW64x32C-K610A": GU600Config(64, 32),
    "GW128x32C-K610A": GU600Config(128, 32),
    "GU128x32D-K610A8": GU600Config(128, 32),
    "GU126x32F-K611A4": GU600Config(128, 32),
    "GU126x32F-K612A4": GU600Config(128, 32),
    "GU128x64D-K610A8": GU600Config(128, 64),
    "GU128x64D-K612A8": GU600Config(128, 64),
    "GU126x64F-K612A4": GU600Config(128, 64),
    "GU144x16D-K610A8": GU600Config(144, 16),
    "GU144x40D-K610A8": GU600Config(144, 40),
    "GU180x32D-K610A8": GU600Config(180, 32),
    "GU180x32D-K612A8": GU600Config(180, 32),
    "GU240x64D-K612A8": GU600Config(240, 64),
    "GU256x32D-K610A8": GU600Config(256, 32),
    "GU256x32D-K612A8": GU600Config(256, 32),
}
