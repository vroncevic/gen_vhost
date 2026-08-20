# -*- coding: UTF-8 -*-

'''
Module
    gen_vhost_command_test.py
Info
    Unit tests for GenVhostCommandDefinition and GenVhostCommandExecutor.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from gen_vhost.core.service.iservice import IService
from gen_vhost.core.model.project_setup import ProjectSetup
from gen_vhost.infrastructure.command.gen_vhost_command_definition import GenVhostCommandDefinition
from gen_vhost.infrastructure.command.gen_vhost_command_executor import GenVhostCommandExecutor


class TestGenVhostCommand(unittest.TestCase):

    def test_definition(self) -> None:
        definition = GenVhostCommandDefinition()
        self.assertEqual(definition.name, 'generate-vhost')
        self.assertEqual(definition.help_text, 'Generate virtual host configuration file for Apache web server')
        self.assertEqual(len(definition.options), 10)
        self.assertTrue(isinstance(str(definition), str))

    def test_executor_execute_success(self) -> None:
        definition = GenVhostCommandDefinition()
        executor = GenVhostCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}
        
        params = {'name': 'test', 'output': '.'}
        result = executor.execute(params=params, service=mock_service)
        
        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(params=ProjectSetup(vhost_config=params))

    def test_executor_execute_not_initialized(self) -> None:
        definition = GenVhostCommandDefinition()
        executor = GenVhostCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = False
        
        result = executor.execute(params={}, service=mock_service)
        self.assertEqual(result['returncode'], 1)
        self.assertIn('service not initialized', result['stderr'])

    def test_executor_str_representation(self) -> None:
        definition = GenVhostCommandDefinition()
        executor = GenVhostCommandExecutor(definition)
        self.assertTrue(isinstance(str(executor), str))
