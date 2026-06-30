# -*- coding: UTF-8 -*-

'''
Module
    ifile_writer.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_vhost is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_vhost is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines abstract interface for file writing.
'''

from abc import ABC, abstractmethod

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class IFileWriter(ABC):
    '''
        Abstract interface for writing files.

        It defines:

            :attributes: None
            :methods:
                | write_file - Writes content to the specified target file.
                | is_initialized - Checks if the file writer component is initialized.
                | __str__ - Returns the file writer as string representation.
    '''

    @abstractmethod
    def write_file(self, filename: str, content: str) -> bool:
        '''
            Writes content to a file at the specified path.

            :param filename: The destination file path.
            :type filename: <str>
            :param content: The text content to write.
            :type content: <str>
            :return: True if file was written successfully, False otherwise.
            :return type: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if the file writer component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the file writer as string representation.

            :return: The file writer as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
