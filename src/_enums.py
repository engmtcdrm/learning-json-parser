from enum import Enum

class Value(Enum):
    STRING = 1
    NUMBER = 2
    OBJECT = 3
    ARRAY = 4
    TRUE = 5
    FALSE = 6
    NULL = 7

class EscapeChar(Enum):
    QUOTATIONMARK = 1
    REVERSESOLIDUS = 2
    SOLIDUS = 3
    BACKSPACE = 4
    FORMFEED = 5
    LINEFEED = 6
    CARRIAGERETURN = 7
    HORIZONTALTAB = 8
    UNICODE = 9

class Whitespace(Enum):
    SPACE = 1
    LINEFEED = 2
    CARRIAGERETURN = 3
    HORIZONTALTAB = 4