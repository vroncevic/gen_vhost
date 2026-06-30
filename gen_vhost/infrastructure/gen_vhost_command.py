# -*- coding: UTF-8 -*-

'''
Module
    gen_vhost_command.py
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
    Defines GenVhostCommand class implementing ICLICommand strategy.
'''

from typing import Any, override
from ats_utilities.option.command_option import CommandOption
from ats_utilities.factory_class import format_instance_to_string
from gen_vhost.infrastructure.icli_command import ICLICommand
from gen_vhost.domain.ports.ifile_gen import IFileGen

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class GenVHostCommand(ICLICommand):
    '''
        CLI subcommand for generating virtual host files.

        It defines:

            :attributes: None.
            :methods:
                | name - Returns the command name key.
                | help_text - Returns the command help text.
                | options - Returns the command options.
                | execute - Executes the configuration file generation logic.
                | __str__ - Returns GenVHostCommand instance as string representation.
    '''

    @property
    @override
    def name(self) -> str:
        '''
            Returns the command name key.

            :return: The command name key.
            :rtype: <str>
            :exceptions: None.
        '''
        return "generate-vhost"

    @property
    @override
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
            :rtype: <str>
            :exceptions: None.
        '''
        return "Generate virtual host configuration file for Apache web server"

    @property
    @override
    def options(self) -> list[CommandOption]:
        '''
            Returns the command options.

            :return: List of command options.
            :rtype: <List[CommandOption]>
            :exceptions: None.
        '''
        return [
            CommandOption(
                name="--filename",
                help_text="Output virtual host configuration filename",
                default="vhost_config.conf"
            ),
            CommandOption(
                name="--type",
                help_text="Virtual host type (static, ruby, python, php, perl)",
                default="static"
            ),
            CommandOption(
                name="--url",
                help_text="Virtual host URL path",
                default="/"
            ),
            CommandOption(
                name="--domain-name",
                help_text="Application domain name",
                required=True
            ),
            CommandOption(
                name="--app-dir",
                help_text="Application directory",
                default="/var/www/app"
            ),
            CommandOption(
                name="--log-dir",
                help_text="Application log directory",
                default="/var/log/app"
            ),
            CommandOption(
                name="--admin-email",
                help_text="Administrator email address",
                default="[EMAIL_ADDRESS]"
            ),
            CommandOption(
                name="--ports",
                help_text="Application ports",
                default="80 443"
            ),
            CommandOption(
                name="--www-root",
                help_text="Application web root directory",
                default="/var/www/app"
            ),
            CommandOption(
                name="--logs-root",
                help_text="Application logs root directory",
                default="/var/log/app"
            )
        ]

    @override
    def execute(self, params: dict[str, Any], service: IFileGen) -> dict[str, Any]:
        '''
            Executes the configuration file generation logic.

            :param params: Subcommand parameters from CLI parser.
            :type params: <dict[str, Any]>
            :param service: Generation orchestrator service instance.
            :type service: <IFileGen>
            :return: Return code, stdout and stderr messages.
            :return type: <dict[str, Any]>
            :exceptions: None.
        '''
        target_filename = params.pop("filename")
        vhost_type = params.pop("type", "static")

        template_params = {
            "PORTS": params.get("ports"),
            "ROOT_DOC": params.get("www_root"),
            "SERVER_NAME": params.get("domain_name"),
            "ADMIN_EMAIL": params.get("admin_email"),
            "TARGET_DIR": params.get("app_dir"),
            "URL": params.get("url", "/")
        }

        return service.execute(
            template_name=f"vhost_{vhost_type}",
            target_filename=target_filename,
            cli_params=template_params
        )

    @override
    def __str__(self) -> str:
        '''
            Returns GenVHostCommand instance as string representation.

            :return: GenVHostCommand instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
