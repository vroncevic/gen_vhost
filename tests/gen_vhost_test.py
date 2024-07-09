# -*- coding: UTF-8 -*-

'''
Module
    gen_vhost_test.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_vhost is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_vhost is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines py GenVHostTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenMessageQueue.
Execute
    python3 -m unittest -v gen_vhost_test
'''

import sys
from typing import List
from os import makedirs, rmdir
from unittest import TestCase, main

try:
    from gen_vhost import GenVHost
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_vhost'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__ = '1.1.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenVHostTestCase(TestCase):
    '''
        Defines py GenVHostTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenVHost.
        GenVHost unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create (not None).
                | test_missing_args - Test missing args.
                | test_wrong_arg - Test wrong arg.
                | test_process_perl - Generate perl project structure.
                | test_process_php - Generate php project structure.
                | test_process_python - Generate python project structure.
                | test_process_ruby - Generate ruby project structure.
                | test_process_static - Generate static project structure.
                | test_pro_already_exists - Test pro already exists.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create (not None)'''
        generator: GenVHost = GenVHost()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Test missing args'''
        sys.argv.clear()
        generator: GenVHost = GenVHost()
        self.assertFalse(generator.process())

    def test_wrong_arg(self) -> None:
        '''Test wrong arg'''
        sys.argv.clear()
        sys.argv.insert(0, '-d')
        sys.argv.insert(1, 'wrong_pro')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'perl')
        generator: GenVHost = GenVHost()
        self.assertFalse(generator.process())

    def test_process_perl(self) -> None:
        '''Generate perl project structure'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'perl_pro')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'perl')
        generator: GenVHost = GenVHost()
        self.assertTrue(generator.process())

    def test_process_php(self) -> None:
        '''Generate php project structure'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'php_pro')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'php')
        generator: GenVHost = GenVHost()
        self.assertTrue(generator.process())

    def test_process_python(self) -> None:
        '''Generate python project structure'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'python_pro')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'python')
        generator: GenVHost = GenVHost()
        self.assertTrue(generator.process())

    def test_process_ruby(self) -> None:
        '''Generate ruby project structure'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'ruby_pro')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'ruby')
        generator: GenVHost = GenVHost()
        self.assertTrue(generator.process())

    def test_process_static(self) -> None:
        '''Generate static project structure'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'static_pro')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'static')
        generator: GenVHost = GenVHost()
        self.assertTrue(generator.process())

    def test_pro_already_exists(self) -> None:
        '''Test pro already exists'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'fresh_new')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'ruby')
        generator: GenVHost = GenVHost()
        makedirs('fresh_new')
        self.assertFalse(generator.process())
        rmdir('fresh_new')


if __name__ == '__main__':
    main()
