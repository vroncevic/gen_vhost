# -*- coding: UTF-8 -*-

'''
Module
    project_setup_test.py
Info
    Unit tests for ProjectSetup class.
'''

from __future__ import annotations

import unittest

from gen_vhost.core.model.project_setup import ProjectSetup


class TestProjectSetup(unittest.TestCase):
    def test_project_setup_initialization(self) -> None:
        vhost_config = {'key': 'value'}
        setup = ProjectSetup(vhost_config=vhost_config)
        self.assertEqual(setup.vhost_config, vhost_config)
