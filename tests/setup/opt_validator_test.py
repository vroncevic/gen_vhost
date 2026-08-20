# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenVhostBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_vhost.setup.opt_validator import GenVhostBundleOptionsValidator


class TestGenVhostBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenVhostBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenVhostBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenVhostBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenVhostBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenVhostBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenVhostBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenVhostBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenVhostBundleOptionsValidator.is_valid({'info_file': 123}))
