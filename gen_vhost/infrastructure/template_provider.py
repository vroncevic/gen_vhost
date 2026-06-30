# -*- coding: UTF-8 -*-

'''
Module
    template_provider.py
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
    Defines template provider adapter that loads templates from files.
'''

from typing import override
from os.path import abspath, dirname, join, exists
from ats_utilities.factory_class import require_attributes, format_instance_to_string
from gen_vhost.domain.ports.itemplate_provider import ITemplateProvider

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TemplateProvider(ITemplateProvider):
    '''
        Adapter that reads templates from the filesystem.

        It defines:

            :attributes:
                | _templates_dir - The directory where templates are stored.
            :methods:
                | __init__ - Initializes the TemplateProvider with a directory path.
                | get_template_by_name - Reads template content from file.
                | is_initialized - Checks if the template provider component is initialized.
                | __str__ - Returns the template provider as string representation.
    '''

    def __init__(self, templates_dir: str | None = None):
        '''
            Initializes the TemplateProvider with a directory path.

            :param templates_dir: Path to directory containing templates.
            :type templates_dir: <str | None>
            :exceptions: None.
        '''
        self._templates_dir: str = templates_dir or join(dirname(abspath(__file__)), "templates")

    @require_attributes("_templates_dir")
    @override
    def get_template_by_name(self, name: str) -> str:
        '''
            Reads template content from file based on template name.

            :param name: The name of the template.
            :type name: <str>
            :return: The content of the template file.
            :rtype: <str>
            :exceptions:
                | FileNotFoundError: If the template file does not exist.
                | OSError: If the template file cannot be read.
        '''
        file_path: str = join(self._templates_dir, f"{name}.template")

        if not exists(file_path):
            raise FileNotFoundError(f"Template {name} does not exist at path {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the template provider component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return exists(self._templates_dir)

    @override
    def __str__(self) -> str:
        '''
            Returns the TemplateProvider instance as string representation.

            :return: The TemplateProvider instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
