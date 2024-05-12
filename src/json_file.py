import os

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import StrPath as _StrPath
else:
    from typing import Union

    _StrPath = Union[str, os.PathLike]

class JSONFile:
    """
    Represents a JSON file.

    :param path: The path to the JSON file.
    """
    def __init__(self, path: _StrPath):
        self._path = path
        self._linesep = os.linesep

    def read(self) -> str:
        with open(self._path, encoding='utf-8', newline="") as f:
            content = f.read()

            nl_cnt = content.count("\n")

            if nl_cnt > 0:
                win_eol_cnt = content.count('\r\n')

                if win_eol_cnt == nl_cnt:
                    self._linesep = '\r\n'
                elif win_eol_cnt == 0:
                    self._linesep = '\n'
                else:
                    self._linesep = 'mixed'

        return content

    def write(self, data) -> str:
        pass
