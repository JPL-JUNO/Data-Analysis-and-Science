"""
@File         : clean.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-07-22 22:51:32
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


def generalize(ser, match_name, default):
    """Lower the cardinality."""
    seen = None
    for match, name in match_name:
        mask = ser.str.contains(match)
        if seen is None:
            seen = mask
        else:
            seen |= mask

        ser = ser.where(~mask, name)
    ser = ser.where(seen, default)
    return ser
