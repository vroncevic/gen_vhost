# -*- coding: UTF-8 -*-

'''
Module
    test_infrastructure.py
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
    Unit tests for infrastructure adapters.
'''

import tempfile
import unittest
from os.path import exists, join
from unittest.mock import patch, MagicMock
from typing import Any, override
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.engine import Checker
from ats_utilities.reporter.engine import Reporter
from ats_utilities.option.command_option import CommandOption
from ats_utilities.option.ioption_parser import IOptionManager
from gen_vhost.infrastructure.icli_command import ICLICommand
from gen_vhost.infrastructure.cli_bundle import CLIBundle
from gen_vhost.infrastructure.cli import CLI
from gen_vhost.infrastructure.file_writer import FileWriter
from gen_vhost.infrastructure.template_provider import TemplateProvider
from gen_vhost.infrastructure.gen_vhost_command import GenVHostCommand
from gen_vhost.domain.ports.ifile_gen import IFileGen

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyCommand(ICLICommand):
    '''
        Dummy CLI command for testing ArgParser.

        It defines:

            :attributes: None.
            :methods:
                | name - Command name.
                | help_text - Command help text.
                | options - Command options.
                | execute - Simulates command execution.
    '''

    @property
    @override
    def name(self) -> str:
        '''
            Returns command name.

            :return: The command name.
            :rtype: <str>
            :exceptions: None.
        '''
        return "dummy"

    @property
    @override
    def help_text(self) -> str:
        '''
            Returns command help text.

            :return: The command help.
            :rtype: <str>
            :exceptions: None.
        '''
        return "Dummy command for tests"

    @property
    @override
    def options(self) -> list[CommandOption]:
        '''
            Returns command options.

            :return: List of command options.
            :rtype: <List[CommandOption]>
            :exceptions: None.
        '''
        return [
            CommandOption(name="--foo", help_text="foo parameter", default="bar"),
            CommandOption(name="--req", help_text="required parameter", required=True)
        ]

    @override
    def execute(self, params: dict, service: IFileGen) -> None:
        '''
            Simulates execution.

            :param params: Execution params.
            :type params: <dict>
            :param service: Generation service.
            :type service: <IFileGen>
            :exceptions: None.
        '''
        pass

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of the command.

            :return: The string representation of the command.
            :rtype: <str>
            :exceptions: None.
        '''
        return f"DummyCommand(name='{self.name}', help_text='{self.help_text}', options={self.options})"


class TestInfrastructure(unittest.TestCase):
    '''
        Defines infrastructure adapters unit tests.

        It defines:

            :attributes: None.
            :methods:
                | test_arg_parser_success - Tests successful CLI argument parsing.
                | test_cli_bundle_validation - Tests validation checks of CLIBundle.
                | test_cli_run_executes_command - Tests that CLI.run executes matching command strategy.
                | test_gen_vhost_command_metadata - Tests GenVHostCommand properties.
                | test_cli_bundle_helpers - Tests CLIBundle helper methods.
                | test_cli_bundle_validate_commands_none - Tests CLIBundle validation with None commands.
                | test_cli_init_missing_bundle - Tests CLI init with None bundle.
                | test_concrete_file_writer - Tests concrete FileWriter.
                | test_concrete_template_provider - Tests concrete TemplateProvider.
    '''

    def test_arg_parser_success(self) -> None:
        '''
            Tests successful registration and parsing of CLI arguments.

            :exceptions: None.
        '''
        context: ContextBundle = ContextBundle(checker=Checker(), reporter=Reporter(), verbose=False)
        params: dict[str, str] = {
            'ats_name': 'test_cli',
            'ats_version': '1.1.6',
            'ats_licence': 'MIT',
            'ats_build_date': '2026-06-22'
        }
        bundle: OptionComponentBundle = OptionComponentBundle(parameters=params, context_bundle=context)
        parser: OptionManager = OptionManager(bundle)

        cmd: DummyCommand = DummyCommand()
        parser.register_commands([cmd])

        test_args: list[str] = ["main.py", "dummy", "--req", "val", "--foo", "baz"]
        cmd_name: str
        params: dict[str, str]

        with patch("sys.argv", test_args):
            cmd_name, params = parser.parse_command()

        self.assertEqual(cmd_name, "dummy")
        self.assertEqual(params["req"], "val")
        self.assertEqual(params["foo"], "baz")

    def test_cli_bundle_validation(self) -> None:
        '''
            Tests validation checks of CLIBundle.

            :exceptions: None.
        '''
        bundle: CLIBundle = CLIBundle(service=None, parser=None, commands=None)
        with self.assertRaises(ValueError):
            bundle.validate()

        bundle_partial: CLIBundle = CLIBundle(service=MagicMock(), parser=None, commands=[])
        with self.assertRaises(ValueError):
            bundle_partial.validate()

    def test_cli_run_executes_command(self) -> None:
        '''
            Tests that CLI.run parses arguments and delegates execution to the matched command.

            :exceptions: None.
        '''
        mock_service: MagicMock = MagicMock(spec=IFileGen)
        mock_parser: MagicMock = MagicMock(spec=IOptionManager)
        mock_command: MagicMock = MagicMock(spec=ICLICommand)
        mock_command.name = "dummy"

        mock_parser.parse_command.return_value = ("dummy", {"foo": "bar"})

        cli_bundle: CLIBundle = CLIBundle(service=mock_service, parser=mock_parser, commands=[mock_command])
        cli: CLI = CLI(cli_bundle)
        cli.run()

        mock_parser.parse_command.assert_called_once()
        mock_command.execute.assert_called_once_with({"foo": "bar"}, mock_service)

        self.assertIsNotNone(str(cli))
        self.assertIsNotNone(repr(cli))
        self.assertIsInstance(str(cli), str)
        self.assertIsInstance(repr(cli), str)
        self.assertNotEqual(str(cli), "")
        self.assertNotEqual(repr(cli), "")

    def test_gen_vhost_command_metadata(self) -> None:
        '''
            Tests GenVHostCommand properties and parameter mapping execution.

            :exceptions: None.
        '''
        cmd: GenVHostCommand = GenVHostCommand()
        self.assertEqual(cmd.name, "generate-vhost")
        self.assertEqual(cmd.help_text, "Generate virtual host configuration file for Apache web server")
        self.assertEqual(len(cmd.options), 10)
        self.assertIsNotNone(str(cmd))
        self.assertIsNotNone(repr(cmd))
        self.assertIsInstance(str(cmd), str)
        self.assertIsInstance(repr(cmd), str)
        self.assertNotEqual(str(cmd), "")
        self.assertNotEqual(repr(cmd), "")

        mock_service: MagicMock = MagicMock(spec=IFileGen)
        params: dict[str, str] = {
            "filename": "vhost.conf",
            "type": "static",
            "ports": "80 443",
            "www_root": "/var/www/app",
            "domain_name": "example.com",
            "admin_email": "admin@example.com",
            "app_dir": "/var/www/app",
            "url": "/"
        }
        cmd.execute(params, mock_service)

        mock_service.execute.assert_called_once_with(
            template_name="vhost_static",
            target_filename="vhost.conf",
            cli_params={
                "PORTS": "80 443",
                "ROOT_DOC": "/var/www/app",
                "SERVER_NAME": "example.com",
                "ADMIN_EMAIL": "admin@example.com",
                "TARGET_DIR": "/var/www/app",
                "URL": "/"
            }
        )

    def test_cli_bundle_helpers(self) -> None:
        '''
            Tests CLIBundle helper methods (merge, to_dict).

            :exceptions: None.
        '''
        mock_service: MagicMock = MagicMock(spec=IFileGen)
        mock_parser: MagicMock = MagicMock(spec=IOptionManager)

        bundle1: CLIBundle = CLIBundle(service=mock_service, parser=None, commands=None)
        bundle2: CLIBundle = CLIBundle(service=None, parser=mock_parser, commands=[])
        bundle1.merge(bundle2)

        self.assertEqual(bundle1.service, mock_service)
        self.assertEqual(bundle1.parser, mock_parser)
        self.assertEqual(bundle1.commands, [])

        d: dict[str, Any] = bundle1.to_dict()
        self.assertEqual(d["service"], mock_service)
        self.assertEqual(d["parser"], mock_parser)
        self.assertEqual(d["commands"], [])

    def test_cli_bundle_validate_commands_none(self) -> None:
        '''
            Tests CLIBundle validate raises ValueError when commands list is None.

            :exceptions: None.
        '''
        bundle: CLIBundle = CLIBundle(service=MagicMock(), parser=MagicMock(), commands=None)
        with self.assertRaises(ValueError):
            bundle.validate()

    def test_cli_init_missing_bundle(self) -> None:
        '''
            Tests CLI initialization raises ValueError when bundle is None.

            :exceptions: None.
        '''
        with self.assertRaises(ValueError):
            CLI(None)

    def test_concrete_file_writer(self) -> None:
        '''
            Tests concrete FileWriter.

            :exceptions: None.
        '''
        writer: FileWriter = FileWriter()

        with tempfile.TemporaryDirectory() as tmpdir:
            file_path: str = join(tmpdir, "nested_dir", "test_file.txt")
            writer.write_file(file_path, "hello world")

            self.assertTrue(exists(file_path))
            with open(file_path, "r", encoding="utf-8") as f:
                content: str = f.read()
            self.assertEqual(content, "hello world")

        self.assertIsNotNone(str(writer))
        self.assertIsNotNone(repr(writer))
        self.assertIsInstance(str(writer), str)
        self.assertIsInstance(repr(writer), str)
        self.assertNotEqual(str(writer), "")
        self.assertNotEqual(repr(writer), "")

    def test_concrete_template_provider(self) -> None:
        '''
            Tests concrete TemplateProvider.

            :exceptions: None.
        '''
        provider: TemplateProvider = TemplateProvider()

        static_template: str = provider.get_template_by_name("vhost_static")
        self.assertTrue(len(static_template) > 0)

        ruby_template: str = provider.get_template_by_name("vhost_ruby")
        self.assertTrue(len(ruby_template) > 0)

        with tempfile.TemporaryDirectory() as tmpdir:
            custom_provider: TemplateProvider = TemplateProvider(templates_dir=tmpdir)
            self.assertEqual(custom_provider._templates_dir, tmpdir)

            with self.assertRaises(FileNotFoundError):
                custom_provider.get_template_by_name("nonexistent")

        self.assertIsNotNone(str(provider))
        self.assertIsNotNone(repr(provider))
        self.assertIsInstance(str(provider), str)
        self.assertIsInstance(repr(provider), str)
        self.assertNotEqual(str(provider), "")
        self.assertNotEqual(repr(provider), "")

    def test_command_option_init(self) -> None:
        '''
            Tests CommandOption initialization and attributes.

            :exceptions: None.
        '''
        opt: CommandOption = CommandOption(
            name="--test",
            help_text="Test description",
            default="default_val",
            required=True,
            choices=["choice1", "choice2"]
        )
        self.assertEqual(opt.name, "--test")
        self.assertEqual(opt.help_text, "Test description")
        self.assertEqual(opt.default, "default_val")
        self.assertTrue(opt.required)
        self.assertEqual(opt.choices, ["choice1", "choice2"])

    def test_str_repr(self) -> None:
        '''
            Tests string representation of infrastructure adapters and components.

            :exceptions: None.
        '''
        service: MagicMock = MagicMock(spec=IFileGen)
        parser: MagicMock = MagicMock(spec=IOptionManager)
        cmd1: GenVHostCommand = GenVHostCommand()
        bundle: CLIBundle = CLIBundle(service=service, parser=parser, commands=[cmd1])
        cli: CLI = CLI(bundle)

        self.assertIsNotNone(str(cmd1))
        self.assertIsNotNone(repr(cmd1))
        self.assertIsInstance(str(cmd1), str)
        self.assertIsInstance(repr(cmd1), str)

        self.assertIsNotNone(str(bundle))
        self.assertIsNotNone(repr(bundle))
        self.assertIsInstance(str(bundle), str)
        self.assertIsInstance(repr(bundle), str)

        self.assertIsNotNone(str(cli))
        self.assertIsNotNone(repr(cli))
        self.assertIsInstance(str(cli), str)
        self.assertIsInstance(repr(cli), str)
