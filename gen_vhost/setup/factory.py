# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_vhost bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_vhost.setup.bundle import GenVhostBundle
from gen_vhost.setup.options import GenVhostBundleOptions
from gen_vhost.setup.registry import GenVhostBundleRegistry
from gen_vhost.setup.dependencies import GenVhostBundleDependencies
from gen_vhost.setup.opt_validator import GenVhostBundleOptionsValidator
from gen_vhost.setup.keys import GenVhostBundleKeys
from gen_vhost.core.service.engine import Service
from gen_vhost.infrastructure.subprocessor import SubProcessor
from gen_vhost.infrastructure.cli.engine import CLI
from gen_vhost.infrastructure.cli.setup.bundle import CLIBundle
from gen_vhost.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_vhost.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_vhost.infrastructure.command.command import CommandBundle
from gen_vhost.infrastructure.command.gen_vhost_command_definition import GenVhostCommandDefinition
from gen_vhost.infrastructure.command.gen_vhost_command_executor import GenVhostCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__ = '1.1.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenVhostBundleFactory:
    '''
        Factory for creating the gen_vhost bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_vhost info file.
            :methods:
                | create_bundle - Creates the gen_vhost bundle with optional pre-configured options.
                | get_version - Returns the factory version.
    '''

    _info_file: str = 'gen_vhost/infrastructure/config/gen_vhost.cfg'

    @classmethod
    def create_bundle(cls, options: GenVhostBundleOptions | None = None) -> GenVhostBundle:
        '''
            Creates the gen_vhost bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_vhost bundle.
            :return: The gen_vhost bundle.
            :exceptions:
                | ATSValueError: The gen_vhost bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_vhost bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_vhost bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_vhost bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_vhost bundle must be provided and have proper values.
                | ATSTypeError:  The gen_vhost bundle must be an instance of GenVhostBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenVhostBundleOptionsValidator.validate(options)

        info_file = options.get(GenVhostBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_vhost_definition: GenVhostCommandDefinition = GenVhostCommandDefinition()

        gen_vhost_bundle: CommandBundle = CommandBundle(
            definition=gen_vhost_definition,
            executor=GenVhostCommandExecutor(gen_vhost_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_vhost_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenVhostBundleRegistry.create_bundle(
            dependencies=GenVhostBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version.

            :return: The factory version.
            :exceptions: None.
        '''
        return __version__

