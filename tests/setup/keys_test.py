# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenVhostBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_vhost.setup.keys import GenVhostBundleKeys


class TestGenVhostBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenVhostBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenVhostBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenVhostBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenVhostBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenVhostBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenVhostBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenVhostBundleKeys.OPTION_INFO_FILE, opts)
