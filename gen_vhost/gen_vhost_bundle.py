# -*- coding: UTF-8 -*-

'''
Module
    gen_vhost_bundle.py
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
    Defines a GenVhostBundle bundle for the CLI application.
'''

from typing import Any
from dataclasses import dataclass
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.exceptions.ats_value_error import ATSValueError
from gen_vhost.domain.ports.itemplate_provider import ITemplateProvider
from gen_vhost.domain.ports.ifile_writer import IFileWriter
from gen_vhost.domain.ports.ifile_gen import IFileGen
from gen_vhost.infrastructure.icli import ICLI

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'

@dataclass
class GenVhostBundle:
    '''
        GenVhostBundle holding all components (adapters and services) of the CLI application.

        It defines:

            :attributes:
                | template_provider - Adapter for reading templates (default None).
                | file_writer - Adapter for writing files (default None).
                | service - Service orchestrating file generation (default None).
                | parser - CLI argument parser adapter (default None).
                | cli - Command line user interface adapter (default None).
            :methods:
                | validate - Validates that the bundle is valid.
                | merge - Merges non-None values from another bundle.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    template_provider: ITemplateProvider | None = None
    file_writer: IFileWriter | None = None
    service: IFileGen | None = None
    parser: IOptionManager | None = None
    cli: ICLI | None = None

    def validate(self) -> None:
        '''
            Validates that the bundle is valid.

            :exceptions:
                | ATSValueError: Template provider must be provided.
                | ATSValueError: File writer must be provided.
                | ATSValueError: Service must be provided.
                | ATSValueError: Parser must be provided.
                | ATSValueError: CLI must be provided.
        '''
        if self.template_provider is None:
            raise ATSValueError('template provider must be provided.')

        if self.file_writer is None:
            raise ATSValueError('file writer must be provided.')

        if self.service is None:
            raise ATSValueError('service must be provided.')

        if self.parser is None:
            raise ATSValueError('parser must be provided.')

        if self.cli is None:
            raise ATSValueError('cli must be provided.')

    def merge(self, other: 'GenVhostBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <GenVhostBundle>
            :exceptions: None.
        '''
        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the bundle attributes to a dictionary.

            :return: Dictionary representation of the bundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }
