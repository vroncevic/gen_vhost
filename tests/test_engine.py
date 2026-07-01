# -*- coding: UTF-8 -*-

'''
Module
    test_engine.py
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
    Unit tests for main engine (GenVhost).
'''

import unittest
from unittest.mock import MagicMock, patch
from gen_vhost.engine import GenVhost
from gen_vhost.gen_vhost_bundle import GenVhostBundle
from gen_vhost.domain.ports.itemplate_provider import ITemplateProvider
from gen_vhost.domain.ports.ifile_writer import IFileWriter
from gen_vhost.domain.ports.ifile_gen import IFileGen
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.exceptions.ats_value_error import ATSValueError
from gen_vhost.infrastructure.icli import ICLI

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TestEngine(unittest.TestCase):
    '''
        Defines engine unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_default_init - Tests default constructor initialization.
                | test_custom_injection - Tests custom dependency injection in GenVhost.
                | test_init_failure - Tests engine behavior when dependency initialization fails.
                | test_run_success - Tests that run() executes CLI if initialized.
                | test_run_failure - Tests that run() prints error and does not execute if uninitialized.
                | test_gen_vhost_bundle_helpers - Tests GenVhostBundle helpers.
    '''

    def test_default_init(self) -> None:
        '''
            Tests default constructor initialization of GenVhost.

            :exceptions: None.
        '''
        engine: GenVhost = GenVhost()
        self.assertTrue(engine._is_initialized)
        self.assertIsNotNone(engine._cli)

    def test_custom_injection(self) -> None:
        '''
            Tests custom dependency injection in GenVhost constructor.

            :exceptions: None.
        '''
        mock_provider: MagicMock = MagicMock(spec=ITemplateProvider)
        mock_writer: MagicMock = MagicMock(spec=IFileWriter)
        mock_service: MagicMock = MagicMock(spec=IFileGen)
        mock_parser: MagicMock = MagicMock(spec=IOptionManager)
        mock_cli: MagicMock = MagicMock(spec=ICLI)

        mock_provider.is_initialized.return_value = True
        mock_writer.is_initialized.return_value = True
        mock_service.is_initialized.return_value = True
        mock_cli.is_initialized.return_value = True

        bundle: GenVhostBundle = GenVhostBundle(
            template_provider=mock_provider,
            file_writer=mock_writer,
            service=mock_service,
            parser=mock_parser,
            cli=mock_cli
        )

        engine: GenVhost = GenVhost(bundle)
        self.assertTrue(engine._is_initialized)
        self.assertEqual(engine._cli, mock_cli)

    def test_not_initialized_engine(self) -> None:
        '''
            Tests not initialized engine.

            :exceptions: None.
        '''
        with patch.object(GenVhost, "_info_file", "invalid/path/gen_vhost.cfg"):
            engine: GenVhost = GenVhost()
            self.assertFalse(engine._is_initialized)

    def test_init_failure(self) -> None:
        '''
            Tests engine behavior when dependency initialization fails.

            :exceptions: None.
        '''
        error_message: str = "Service initialization failed"

        with patch('gen_vhost.engine.FileGen', side_effect=ATSValueError(error_message)):
            with patch('builtins.print') as mock_print:
                engine: GenVhost = GenVhost()
                self.assertFalse(engine._is_initialized)
                mock_print.assert_called_with(f'\x1b[31m❌ gen_vhost: {error_message}\x1b[0m')

    def test_process_success(self) -> None:
        '''
            Tests that process() executes CLI if initialized.

            :exceptions: None.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.return_value = {"returncode": 0, "stdout": "done!"}
        bundle: GenVhostBundle = GenVhostBundle(cli=mock_cli)

        engine: GenVhost = GenVhost(bundle)
        self.assertTrue(engine._is_initialized)

        engine.process()
        mock_cli.run.assert_called_once()

    def test_process_failure_exit(self) -> None:
        '''
            Tests that process() handles CLI execution failure.

            :exceptions: None.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.return_value = {"returncode": 1, "stderr": "error message"}
        bundle: GenVhostBundle = GenVhostBundle(cli=mock_cli)

        engine: GenVhost = GenVhost(bundle)
        self.assertTrue(engine._is_initialized)

        with patch('builtins.print') as mock_print:
            engine.process()
            mock_cli.run.assert_called_once()
            mock_print.assert_any_call('\x1b[31m❌ gen_vhost: error message\x1b[0m')

    def test_process_failure(self) -> None:
        '''
            Tests that process() prints error and does not execute if uninitialized.

            :exceptions: None.
        '''
        with patch('gen_vhost.engine.FileGen', side_effect=ATSValueError("Service initialization failed")):
            with patch('builtins.print') as mock_print:
                engine: GenVhost = GenVhost()
                self.assertFalse(engine._is_initialized)
                mock_print.assert_any_call('\x1b[31m❌ gen_vhost: Service initialization failed\x1b[0m')

                engine.process()
                mock_print.assert_called_with('\x1b[31m❌ gen_vhost: engine not initialized.\x1b[0m')

    def test_process_failure_with_unexpected_error(self) -> None:
        '''
            Tests that process() prints error if unexpected error occurs.

            :exceptions: None.
        '''
        with patch('gen_vhost.engine.FileGen', side_effect=Exception("unexpected error")):
            with patch('builtins.print') as mock_print:
                engine: GenVhost = GenVhost()
                self.assertFalse(engine._is_initialized)
                mock_print.assert_any_call('\x1b[31m❌ gen_vhost unexpected exception: unexpected error\x1b[0m')

                engine.process()
                mock_print.assert_called_with('\x1b[31m❌ gen_vhost: engine not initialized.\x1b[0m')

    def test_process_unexpected_exception(self) -> None:
        '''
            Tests engine process catches unexpected exception.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.side_effect = Exception("Unexpected error")

        bundle: GenVhostBundle = GenVhostBundle(cli=mock_cli)
        engine: GenVhost = GenVhost(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()

    def test_process_expected_exception(self) -> None:
        '''
            Tests engine process catches expected exception.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.side_effect = ATSValueError("Expected error")

        bundle: GenVhostBundle = GenVhostBundle(cli=mock_cli)
        engine: GenVhost = GenVhost(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()

    def test_gen_vhost_bundle_helpers(self) -> None:
        '''
            Tests GenVhostBundle merge and to_dict helpers.

            :exceptions: None.
        '''
        provider1: MagicMock = MagicMock(spec=ITemplateProvider)
        writer1: MagicMock = MagicMock(spec=IFileWriter)
        service1: MagicMock = MagicMock(spec=IFileGen)
        parser1: MagicMock = MagicMock(spec=IOptionManager)
        cli1: MagicMock = MagicMock(spec=ICLI)

        bundle1: GenVhostBundle = GenVhostBundle(template_provider=provider1, file_writer=None)

        bundle2: GenVhostBundle = GenVhostBundle(template_provider=None, file_writer=writer1)
        bundle1.merge(bundle2)

        self.assertEqual(bundle1.template_provider, provider1)
        self.assertEqual(bundle1.file_writer, writer1)

        d = bundle1.to_dict()
        self.assertEqual(d["template_provider"], provider1)
        self.assertEqual(d["file_writer"], writer1)

        bundle3: GenVhostBundle = GenVhostBundle(
            template_provider=None, file_writer=writer1, parser=parser1, service=service1, cli=cli1
        )

        with self.assertRaises(ATSValueError):
            bundle3.validate()

        bundle4: GenVhostBundle = GenVhostBundle(
            template_provider=provider1, file_writer=None, parser=parser1, service=service1, cli=cli1
        )

        with self.assertRaises(ATSValueError):
            bundle4.validate()

        bundle5: GenVhostBundle = GenVhostBundle(
            template_provider=provider1, file_writer=writer1, parser=None, service=service1, cli=cli1
        )

        with self.assertRaises(ATSValueError):
            bundle5.validate()

        bundle6: GenVhostBundle = GenVhostBundle(
            template_provider=provider1, file_writer=writer1, parser=parser1, service=None, cli=cli1
        )

        with self.assertRaises(ATSValueError):
            bundle6.validate()

        bundle7: GenVhostBundle = GenVhostBundle(
            template_provider=provider1, file_writer=writer1, parser=parser1, service=service1, cli=None
        )

        with self.assertRaises(ATSValueError):
            bundle7.validate()

    def test_str_repr(self) -> None:
        '''
            Tests string representation of GenVhost and GenVhostBundle.

            :exceptions: None.
        '''
        provider: MagicMock = MagicMock(spec=ITemplateProvider)
        writer: MagicMock = MagicMock(spec=IFileWriter)
        service: MagicMock = MagicMock(spec=IFileGen)
        parser: MagicMock = MagicMock(spec=IOptionManager)
        cli: MagicMock = MagicMock(spec=ICLI)

        provider.is_initialized.return_value = True
        writer.is_initialized.return_value = True
        service.is_initialized.return_value = True
        cli.is_initialized.return_value = True

        bundle: GenVhostBundle = GenVhostBundle(
            template_provider=provider,
            file_writer=writer,
            service=service,
            parser=parser,
            cli=cli
        )
        engine: GenVhost = GenVhost(bundle)

        self.assertIsNotNone(str(bundle))
        self.assertIsNotNone(repr(bundle))
        self.assertIsInstance(str(bundle), str)
        self.assertIsInstance(repr(bundle), str)

        self.assertIsNotNone(str(engine))
        self.assertIsNotNone(repr(engine))
        self.assertIsInstance(str(engine), str)
        self.assertIsInstance(repr(engine), str)
