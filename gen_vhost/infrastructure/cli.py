# -*- coding: UTF-8 -*-

'''
Module
    cli.py
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
    Defines CLI class implementing inbound CLI port.
'''

from typing import Any, override
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.exceptions.ats_value_error import ATSValueError
from gen_vhost.infrastructure.icli import ICLI
from gen_vhost.infrastructure.cli_bundle import CLIBundle
from gen_vhost.domain.ports.ifile_gen import IFileGen
from gen_vhost.infrastructure.icli_command import ICLICommand

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CLI(ICLI):
    '''
        Adapter that implements CLI commands for the code generator.

        It defines:

            :attributes:
                | _service - File generation orchestrator service.
                | _parser - CLI argument parser.
                | _commands - Map of command names to command instances.
            :methods:
                | __init__ - Initializes the CLI with CLI adapters.
                | run - Parses CLI arguments and executes selected command.
                | is_initialized - Checks if the CLI component is initialized.
                | __str__ - Returns CLI instance as string representation.
    '''

    def __init__(self, component_bundle: CLIBundle | None = None):
        '''
            Initializes the CLI with CLI adapters.

            :param component_bundle: Bundle containing CLI adapters | None.
            :type component_bundle: <CLIBundle | None>
            :exceptions:
                | ATSValueError: Component bundle (CLIBundle) cannot be None or invalid.
        '''
        if component_bundle is None:
            raise ATSValueError('component bundle (CLIBundle) must be provided.')

        component_bundle.validate()
        self._service: IFileGen = component_bundle.service
        self._parser: IOptionManager = component_bundle.parser
        self._commands: dict[str, ICLICommand] = {cmd.name: cmd for cmd in component_bundle.commands}
        self._parser.register_commands(component_bundle.commands)

    @override
    def run(self) -> dict[str, Any]:
        '''
            Parses CLI arguments and executes selected command.

            :return: Return code, stdout and stderr messages.
            :return type: <dict[str, Any]>
            :exceptions:
                | SystemExit: System exit exception.
                | OSError: I/O error exception.
        '''
        command_name, params = self._parser.parse_command()
        cmd = self._commands.get(command_name)

        return cmd.execute(params, self._service) if cmd else {
            "return_code": -1, "stdout": [], "stderr": ["Unknown command"]
        }

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the CLI component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return True

    @override
    def __str__(self) -> str:
        '''
            Returns CLI instance as string representation.

            :return: CLI instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
