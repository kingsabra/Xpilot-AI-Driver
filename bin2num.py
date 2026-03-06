from __future__ import annotations

from typing import Iterable, Union


BitSeq = Union[str, Iterable[Union[str, int, bool]]]


def bin2num(bits: BitSeq) -> int:
    """
    Convert a sequence of bits to an integer.

    Accepts:
    - "0101" (string)
    - ['0','1',...] (iterable)
    - [0,1,...] (iterable)
    """
    if isinstance(bits, str):
        s = bits.strip()
    else:
        s = "".join("1" if int(b) else "0" for b in bits)

    if s == "":
        return 0
    if any(ch not in "01" for ch in s):
        raise ValueError(f"Invalid bit sequence: {bits!r}")
    return int(s, 2)

