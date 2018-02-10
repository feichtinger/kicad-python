# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# (C) 2018 by Thomas Pointhuber, <thomas.pointhuber@gmx.at>

from kicad.pcbnew.drawing import Drawing
from kicad.pcbnew.module import Module
from kicad.pcbnew.track import Track
from kicad.pcbnew.zone import Zone

from kicad.pcbnew._native import _pcbnew


class Board(object):
    """Create a new Board object

    :param board: already existing board object
    :type board: :class:`pcbnew.BOARD`

    :Example:

    >>> from kicad.pcbnew import Board
    >>> b = Board()
    """
    def __init__(self, board=None):
        if board is None:
            board = _pcbnew.BOARD()

        self._obj = board

    def get_native(self):
        """Get native object from the low level API

        :return: :class:`pcbnew.BOARD`
        """
        return self._obj

    @staticmethod
    def from_editor():
        """Get the current board visible in pcbnew

        :return: :class:`kicad.pcbnew.Board`

        :Example:

        >>> from kicad.pcbnew import Board
        >>> b = Board.from_editor()
        """
        return Board(_pcbnew.GetBoard())

    @staticmethod
    def from_file(path):
        """Load a board from a given filepath

        :param path: path to the ".kicad_mod" file
        :type path: ``str``

        :return: :class:`kicad.pcbnew.Board`

        :Example:

        >>> from kicad.pcbnew import Board
        >>> b = Board.from_file("path/to/board.kicad_mod")# doctest: +SKIP
        """
        return Board(_pcbnew.LoadBoard(path))

    @staticmethod
    def from_source(source):
        pass  # TODO: missing

    def save(self):
        pass  # TODO: missing

    def export(self, path, type):
        pass  # TODO: missing

    @property
    def filename(self):
        return self._obj.GetFileName()

    @filename.setter
    def filename(self, filename):
        self._obj.SetFileName(filename)

    @property
    def aux_origin(self):
        return self._obj.GetAuxOrigin()  # TODO: format conversation?

    @aux_origin.setter
    def aux_origin(self, origin):
        self._obj.SetAuxOrigin(origin)  # TODO: format conversation?

    @property
    def grid_origin(self):
        return self._obj.GetGridOrigin()  # TODO: format conversation?

    @grid_origin.setter
    def grid_origin(self, origin):
        self._obj.SetGridOrigin(origin)  # TODO: format conversation?

    @property
    def modules(self):
        it = self._obj.GetModules().begin()  # TODO: check
        while it is not None:
            yield Module(it)
            it = it.Next()

    @property
    def tracks(self):
        it = self._obj.GetTracks().begin()  # TODO: check
        while it is not None:
            yield Track(it)  # TODO: vias also included
            it = it.Next()

    @property
    def zones(self):
        it = self._obj.GetZones().begin()  # TODO: check
        while it is not None:
            yield Zone(it)
            it = it.Next()

    def is_zone_filled(self):
        pass  # TODO: implement

    def zone_fill(self):
        pass  # TODO: implement

    def zone_unfill(self):
        pass  # TODO: implement

    @property
    def drawings(self):
        it = self._obj.GetDrawings().begin()  # TODO: check
        while it is not None:
            yield Drawing(it)
            it = it.Next()

    @property
    def layers_enabled(self):
        return self._obj.GetEnabledLayers()  # TODO: add wrapper and setter