# -*- coding: UTF-8 -*-

'''
Module
    icli_command.py
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
    Defines abstract ICLICommand strategy interface and CommandOption.
'''

from abc import abstractmethod
from typing import Any
from ats_utilities.option.ioption_command import IOptionCommand
from ats_utilities.option.command_option import CommandOption
from gen_vhost.domain.ports.ifile_gen import IFileGen

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ICLICommand(IOptionCommand):
    '''
        Abstract base class representing a CLI subcommand strategy.

        It defines:

            :attributes: None.
            :methods:
                | name - Property returning name of the command.
                | help_text - Property returning help text of the command.
                | options - Property returning list of command options.
                | execute - Performs subcommand actions.
                | __str__ - Returns the string representation of the command.
    '''

    @property
    @abstractmethod
    def name(self) -> str:
        '''
            Returns the command name key.

            :return: The command name key.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @property
    @abstractmethod
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @property
    @abstractmethod
    def options(self) -> list[CommandOption]:
        '''
            Returns the command options.

            :return: List of command options.
            :rtype: <List[CommandOption]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def execute(self, params: dict[str, Any], service: IFileGen) -> dict[str, Any]:
        '''
            Executes the file generation logic for this command.

            :param params: Subcommand parameters from CLI parser.
            :type params: <dict[str, Any]>
            :param service: Generation orchestrator service instance.
            :type service: <IFileGen>
            :return: Return code, stdout and stderr messages.
            :return type: <dict[str, Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of the command.

            :return: The string representation of the command.
            :rtype: <str>
            :exceptions: None.
        '''
        pass    
