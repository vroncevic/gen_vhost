# -*- coding: UTF-8 -*-

'''
Module
    service.py
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
    Defines application service for file generation.
'''

from typing import Any, override
from gen_vhost.domain.ports.ifile_gen import IFileGen
from gen_vhost.application.service_bundle import ServiceBundle
from gen_vhost.domain.ports.itemplate_provider import ITemplateProvider
from gen_vhost.domain.ports.ifile_writer import IFileWriter
from gen_vhost.domain.models import GeneratedFile

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FileGen(IFileGen):
    '''
        Service for orchestrating the file generation process.

        It defines:

            :attributes:
                | _template_provider - Adapter for providing raw templates.
                | _file_writer - Adapter for writing files.
            :methods:
                | execute - Generates and writes user files.
                | is_initialized - Checks if the file generator component is initialized.
    '''

    def __init__(self, component_bundle: ServiceBundle) -> None:
        '''
            Initializes the FileGen with a template provider and file writer.

            :param component_bundle: Bundle containing template provider and file writer.
            :type component_bundle: <ServiceBundle>
            :exceptions:
                | ValueError: Component bundle (ServiceBundle) cannot be None or invalid.
        '''
        if component_bundle is None:
            raise ValueError('component bundle (ServiceBundle) cannot be None.')

        component_bundle.validate()
        self._template_provider: ITemplateProvider = component_bundle.template_provider
        self._file_writer: IFileWriter = component_bundle.file_writer

    @override
    def execute(self, template_name: str, target_filename: str, cli_params: dict[str, Any]) -> dict[str, Any]:
        '''
            Generates a user file from a template and writes it to target path.

            :param template_name: The name of the template to use.
            :type template_name: <str>
            :param target_filename: The output filename/path.
            :type target_filename: <str>
            :param cli_params: Parameters for template formatting.
            :type cli_params: <dict[str, Any]>
            :return: Return code, stdout and stderr messages.
            :return type: <dict[str, Any]>
            :exceptions:
                | FileNotFoundError: Template file not found.
                | OSError: An I/O error occurred while writing the file.
        '''
        # Get raw template from infrastructure (through port)
        raw_template: str = self._template_provider.get_template_by_name(template_name)

        # Let the domain model handle the "business logic" of parameter replacement
        generated_file: GeneratedFile = GeneratedFile.from_template(target_filename, raw_template, cli_params)

        # Write file where the user requested (delegated to IFileWriter)
        status: bool = self._file_writer.write_file(generated_file.name, generated_file.content)

        return {
            "returncode": 0 if status else 1,
            "stdout": f"file created: {target_filename}" if status else "",
            "stderr": f"failed to create file: {target_filename}" if not status else ""
        }

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the file generator component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return True
