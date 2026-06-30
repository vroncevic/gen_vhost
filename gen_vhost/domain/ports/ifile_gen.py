# -*- coding: UTF-8 -*-

'''
Module
    ifile_gen.py
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
    Defines abstract interface for file generation.
'''

from abc import ABC, abstractmethod
from typing import Any

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class IFileGen(ABC):
    '''
        Abstract interface for file generation.

        It defines:

            :attributes: None
            :methods:
                | execute - Executes the file generation.
                | is_initialized - Checks if the file generator component is initialized.
                | __str__ - Returns the file generator as string representation.
    '''

    @abstractmethod
    def execute(self, template_name: str, target_filename: str, cli_params: dict[str, Any]) -> dict[str, Any]:
        '''
            Executes the file generation.

            :param template_name: The name of the template to use.
            :type template_name: <str>
            :param target_filename: The output filename/path.
            :type target_filename: <str>
            :param cli_params: Parameters for template formatting.
            :type cli_params: <dict[str, Any]>
            :return: Return code, stdout and stderr messages.
            :return type: <dict[str, Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if the file generator component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the file generator as string representation.

            :return: The file generator as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
