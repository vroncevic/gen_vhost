# -*- coding: UTF-8 -*-

'''
Module
    models.py
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
    Defines domain models representing generated files.
'''

from dataclasses import dataclass
from string import Template
from typing import Any

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


@dataclass
class GeneratedFile:
    '''
        Domain model representing a generated file.

        It defines:

            :attributes:
                | name - The target filename or path.
                | content - The rendered string content of the file.
            :methods:
                | from_template - Factory method to build GeneratedFile from template.
    '''

    name: str
    content: str

    @classmethod
    def from_template(cls, filename: str, raw_template: str, params: dict[str, Any]) -> "GeneratedFile":
        '''
            Factory method to build GeneratedFile from template.

            :param filename: The destination filename or path.
            :type filename: <str>
            :param raw_template: The raw template content.
            :type raw_template: <str>
            :param params: Formatting parameters to fill the template.
            :type params: <dict[str, Any]>
            :return: The generated file domain model instance.
            :rtype: <GeneratedFile>
            :exceptions: None.
        '''
        if '$' in raw_template:
            rendered_content = Template(raw_template).substitute(params)
        else:
            rendered_content = raw_template.format(**params)

        return cls(name=filename, content=rendered_content)
