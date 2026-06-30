# -*- coding: UTF-8 -*-

'''
Module
    test_service.py
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
    Unit tests for application service (FileGen).
'''

import unittest
from typing import Dict
from gen_vhost.domain.ports.itemplate_provider import ITemplateProvider
from gen_vhost.domain.ports.ifile_writer import IFileWriter
from gen_vhost.application.service_bundle import ServiceBundle
from gen_vhost.application.service import FileGen

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class MockTemplateProvider(ITemplateProvider):
    '''
        Mock template provider for testing service.

        It defines:

            :attributes:
                | templates - Dictionary of template names to raw contents.
            :methods:
                | get_template_by_name - Retrieves raw template.
    '''

    def __init__(self, templates: Dict[str, str]):
        '''
            Initializes MockTemplateProvider.

            :param templates: Dictionary of templates.
            :type templates: <Dict[str, str]>
            :exceptions: None.
        '''
        self.templates = templates

    def get_template_by_name(self, name: str) -> str:
        '''
            Retrieves raw template.

            :param name: Template name.
            :type name: <str>
            :return: Raw template content.
            :rtype: <str>
            :exceptions: KeyError.
        '''
        if name not in self.templates:
            raise KeyError(f"Template {name} not found.")

        return self.templates[name]

    def is_initialized(self) -> bool:
        '''
            Checks if the template provider is initialized.

            :return: True if initialized, False otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return bool(self.templates)

    def __str__(self) -> str:
        '''
            Returns string representation of MockTemplateProvider.

            :return: String representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return f"MockTemplateProvider(templates={self.templates})"


class MockFileWriter(IFileWriter):
    '''
        Mock file writer for testing service.

        It defines:

            :attributes:
                | written_files - Dictionary tracking written filenames to contents.
            :methods:
                | write_file - Simulates writing a file.
    '''

    def __init__(self) -> None:
        '''
            Initializes MockFileWriter.

            :exceptions: None.
        '''
        self.written_files: Dict[str, str] = {}

    def write_file(self, filepath: str, content: str) -> None:
        '''
            Simulates writing a file by storing path and content.

            :param filepath: Path/name of the file.
            :type filepath: <str>
            :param content: Content to write.
            :type content: <str>
            :exceptions: None.
        '''
        self.written_files[filepath] = content

    def is_initialized(self) -> bool:
        '''
            Checks if the file writer is initialized.

            :return: True if initialized, False otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return bool(self.written_files)

    def __str__(self) -> str:
        '''
            Returns string representation of MockFileWriter.

            :return: String representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return f"MockFileWriter(written_files={self.written_files})"


class TestService(unittest.TestCase):
    '''
        Defines application service unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_init_success - Tests successful service initialization.
                | test_init_missing_bundle - Tests initialization fails when bundle is None.
                | test_init_invalid_bundle - Tests initialization fails when bundle components are None.
                | test_generate_success - Tests successful file generation.
                | test_mock_template_provider_key_error - Tests KeyError raise in MockTemplateProvider.
                | test_service_bundle_helpers - Tests ServiceBundle helpers.
    '''

    def test_init_success(self) -> None:
        '''
            Tests successful service initialization with a valid bundle.

            :exceptions: None.
        '''
        provider: MockTemplateProvider = MockTemplateProvider({"config": "param={value}"})
        writer: MockFileWriter = MockFileWriter()
        bundle: ServiceBundle = ServiceBundle(template_provider=provider, file_writer=writer)
        service: FileGen = FileGen(bundle)
        self.assertIsNotNone(service)

    def test_init_missing_bundle(self) -> None:
        '''
            Tests initialization fails when bundle is None.

            :exceptions: None.
        '''
        with self.assertRaises(ValueError):
            FileGen(None)

    def test_init_invalid_bundle(self) -> None:
        '''
            Tests initialization fails when bundle components are None.

            :exceptions: None.
        '''
        bundle_no_provider: ServiceBundle = ServiceBundle(template_provider=None, file_writer=MockFileWriter())
        with self.assertRaises(ValueError):
            FileGen(bundle_no_provider)

        bundle_no_writer: ServiceBundle = ServiceBundle(template_provider=MockTemplateProvider({}), file_writer=None)
        with self.assertRaises(ValueError):
            FileGen(bundle_no_writer)

    def test_generate_success(self) -> None:
        '''
            Tests successful file generation and writing.

            :exceptions: None.
        '''
        provider: MockTemplateProvider = MockTemplateProvider({"config": "app = {app_name}\nenv = {env}"})
        writer: MockFileWriter = MockFileWriter()
        bundle: ServiceBundle = ServiceBundle(template_provider=provider, file_writer=writer)

        service: FileGen = FileGen(bundle)
        service.execute(
            template_name="config",
            target_filename="generated.ini",
            cli_params={"app_name": "AtsSistem", "env": "dev"}
        )

        self.assertIn("generated.ini", writer.written_files)
        expected_content = "app = AtsSistem\nenv = dev"
        self.assertEqual(writer.written_files["generated.ini"], expected_content)

    def test_mock_template_provider_key_error(self) -> None:
        '''
            Tests that MockTemplateProvider raises KeyError for missing template.

            :exceptions: None.
        '''
        provider: MockTemplateProvider = MockTemplateProvider({})
        with self.assertRaises(KeyError):
            provider.get_template_by_name("nonexistent")

    def test_service_bundle_helpers(self) -> None:
        '''
            Tests ServiceBundle merge and to_dict helpers.

            :exceptions: None.
        '''
        provider1: MockTemplateProvider = MockTemplateProvider({})
        writer1: MockFileWriter = MockFileWriter()
        bundle1: ServiceBundle = ServiceBundle(template_provider=provider1, file_writer=None)

        bundle2: ServiceBundle = ServiceBundle(template_provider=None, file_writer=writer1)
        bundle1.merge(bundle2)

        self.assertEqual(bundle1.template_provider, provider1)
        self.assertEqual(bundle1.file_writer, writer1)

        d: Dict[str, MockTemplateProvider | MockFileWriter] = bundle1.to_dict()
        self.assertEqual(d["template_provider"], provider1)
        self.assertEqual(d["file_writer"], writer1)

    def test_str_repr(self) -> None:
        provider1: MockTemplateProvider = MockTemplateProvider({})
        self.assertIsNotNone(str(provider1))
        self.assertIsNotNone(repr(provider1))
        self.assertIsInstance(str(provider1), str)
        self.assertIsInstance(repr(provider1), str)
        self.assertNotEqual(str(provider1), "")
        self.assertNotEqual(repr(provider1), "")

        writer1: MockFileWriter = MockFileWriter()
        self.assertIsNotNone(str(writer1))
        self.assertIsNotNone(repr(writer1))
        self.assertIsInstance(str(writer1), str)
        self.assertIsInstance(repr(writer1), str)
        self.assertNotEqual(str(writer1), "")
        self.assertNotEqual(repr(writer1), "")

        bundle1: ServiceBundle = ServiceBundle(template_provider=provider1, file_writer=writer1)
        service: FileGen = FileGen(bundle1)

        self.assertIsNotNone(str(service))
        self.assertIsNotNone(repr(service))
        self.assertIsInstance(str(service), str)
        self.assertIsInstance(repr(service), str)
        self.assertNotEqual(str(service), "")
        self.assertNotEqual(repr(service), "")
