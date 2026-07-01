# -*- coding: UTF-8 -*-

'''
Module
    cli_bundle.py
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
    Defines a CLIBundle bundle for the infrastructure adapters.
'''

from typing import Any
from dataclasses import dataclass
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.exceptions.ats_value_error import ATSValueError
from gen_vhost.domain.ports.ifile_gen import IFileGen
from gen_vhost.infrastructure.icli_command import ICLICommand

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


@dataclass
class CLIBundle:
    '''
        Data class for CLI adapters bundle.

        It defines:

            :attributes:
                | service - Service orchestrating file generation (default None).
                | parser - Argument parser for parsing CLI command args (default None).
                | commands - List of command instances (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    service: IFileGen | None = None
    parser: IOptionManager | None = None
    commands: list[ICLICommand] | None = None

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ATSValueError: Service must be provided.
                | ATSValueError: Parser must be provided.
                | ATSValueError: List of commands must be provided.
        '''
        if self.service is None:
            raise ATSValueError('service must be provided.')

        if self.parser is None:
            raise ATSValueError('parser must be provided.')

        if self.commands is None:
            raise ATSValueError('list of commands must be provided.')

    def merge(self, other: 'CLIBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <CLIBundle>
            :exceptions: None.
        '''
        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the bundle attributes to a dictionary.

            :return: Dictionary representation of the bundle attributes.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }
