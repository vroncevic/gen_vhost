# -*- coding: UTF-8 -*-

'''
Module
    gen_vhost_command_definition.py
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
    Defines GenVhostCommandDefinition class.
'''

from __future__ import annotations

from collections.abc import Sequence

from ats_utilities.option.command.data import OptionData
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__ = '1.1.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenVhostCommandDefinition:
    '''
        CLI subcommand metadata definition for Virtual Host configuration generation.

        It defines:

            :methods:
                | name - Returns the command name.
                | help_text - Returns the command help text.
                | options - Returns the sequence of command options.
                | __str__ - Returns the command definition as string representation.
    '''

    @property
    def name(self) -> str:
        '''
            Returns the command name.

            :return: The command name.
        '''
        return 'generate-vhost'

    @property
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
        '''
        return 'Generate virtual host configuration file for Apache web server'

    @property
    def options(self) -> Sequence[OptionData]:
        '''
            Returns the command options.

            :return: Sequence of command options.
        '''
        return [
            OptionData(
                name="--filename",
                help_text="Output virtual host configuration filename",
                action=None,
                default="vhost_config.conf",
                required=False,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--type",
                help_text="Virtual host type (static, ruby, python, php, perl)",
                action=None,
                default="static",
                required=False,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--url",
                help_text="Virtual host URL path",
                action=None,
                default="/",
                required=False,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--domain-name",
                help_text="Application domain name",
                action=None,
                default=None,
                required=True,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--app-dir",
                help_text="Application directory",
                action=None,
                default="/var/www/app",
                required=False,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--log-dir",
                help_text="Application log directory",
                action=None,
                default="/var/log/app",
                required=False,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--admin-email",
                help_text="Administrator email address",
                action=None,
                default="[EMAIL_ADDRESS]",
                required=False,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--ports",
                help_text="Application ports",
                action=None,
                default="80 443",
                required=False,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--www-root",
                help_text="Application web root directory",
                action=None,
                default="/var/www/app",
                required=False,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--logs-root",
                help_text="Application logs root directory",
                action=None,
                default="/var/log/app",
                required=False,
                choices=None,
                nargs=None
            )
        ]

    def __str__(self) -> str:
        '''
            Returns the command definition as string representation.

            :return: The command definition as string representation.
        '''
        return to_str(self)
