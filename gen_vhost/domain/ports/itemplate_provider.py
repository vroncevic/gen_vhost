# -*- coding: UTF-8 -*-

'''
Module
    itemplate_provider.py
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
    Defines abstract interface for template provider.
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


class ITemplateProvider(ABC):
    '''
        Abstract interface for template provider.

        It defines:

            :attributes: None
            :methods:
                | get_template_by_name - Retrieves the raw content of the template by its name.
                | is_initialized - Checks if the template provider component is initialized.
                | __str__ - Returns the template provider as string representation.
    '''

    @abstractmethod
    def get_template_by_name(self, name: str) -> str:
        '''
            Retrieves the raw content of the template by its name.

            :param name: The name of the template.
            :type name: <str>
            :return: The raw template content.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if the template provider component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the template provider as string representation.

            :return: The template provider as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
