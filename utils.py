# -*- coding: utf-8 -*-
#
# Please refer to AUTHORS.md for a complete list of Copyright holders.
# Copyright (C) 2020-2022 Luis Alejandro Martínez Faneyth.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from html.parser import HTMLParser

if not sys.version_info < (3,):
    unicode = str
    basestring = str


def u(u_string):
    """
    Convert a string to unicode working on both python 2 and 3.

    :param u_string: a string to convert to unicode.

    .. versionadded:: 0.1.5
    """
    if isinstance(u_string, unicode):
        return u_string
    return u_string.decode('utf-8')


def html_unescape(_string):
    return HTMLParser().unescape(_string)
