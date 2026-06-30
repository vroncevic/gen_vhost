# -*- coding: UTF-8 -*-

'''
Module
    test_domain.py
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
    Unit tests for domain models.
'''

import unittest
from typing import Dict
from gen_vhost.domain.models import GeneratedFile

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TestDomain(unittest.TestCase):
    '''
        Defines domain unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_from_template_success - Tests successful creation of GeneratedFile.
                | test_from_template_key_error - Tests that missing template keys raise KeyError.
                | test_from_template_value_error - Tests that malformed template formats raise ValueError.
    '''

    def test_from_template_success(self) -> None:
        '''
            Tests successful creation of GeneratedFile from a raw template.

            :exceptions: None.
        '''
        filename: str = "test_output.txt"
        raw_template: str = "Hello, {name}!"
        params: Dict[str, str] = {"name": "World"}

        generated = GeneratedFile.from_template(filename, raw_template, params)
        self.assertEqual(generated.name, filename)
        self.assertEqual(generated.content, "Hello, World!")

    def test_from_template_key_error(self) -> None:
        '''
            Tests that missing template keys raise KeyError.

            :exceptions: None.
        '''
        filename: str = "test_output.txt"
        raw_template: str = "Hello, {name}!"
        params: Dict[str, str] = {}

        with self.assertRaises(KeyError):
            GeneratedFile.from_template(filename, raw_template, params)

    def test_from_template_value_error(self) -> None:
        '''
            Tests that malformed template formats raise ValueError.

            :exceptions: None.
        '''
        filename: str = "test_output.txt"
        raw_template: str = "Hello, {name:badspec}!"
        params: Dict[str, str] = {"name": "World"}

        with self.assertRaises(ValueError):
            GeneratedFile.from_template(filename, raw_template, params)

    def test_from_template_string_template_success(self) -> None:
        '''
            Tests successful creation of GeneratedFile from a raw template using string.Template.

            :exceptions: None.
        '''
        filename: str = "vhost.conf"
        raw_template: str = "PORTS=${PORTS}"
        params: Dict[str, str] = {"PORTS": "80"}

        generated = GeneratedFile.from_template(filename, raw_template, params)
        self.assertEqual(generated.name, filename)
        self.assertEqual(generated.content, "PORTS=80")
