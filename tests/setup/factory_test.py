# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenVhostBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_vhost.setup.bundle import GenVhostBundle
from gen_vhost.setup.factory import GenVhostBundleFactory


class TestGenVhostBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenVhostBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenVhostBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_vhost/infrastructure/config/gen_vhost.cfg'}
        bundle = GenVhostBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenVhostBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenVhostBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenVhostBundleFactory.get_version(), '1.1.8')
