# -*- coding: utf-8 -*-
"""
This file is part of pyCMBS. (c) 2012-2014
For COPYING and LICENSE details, please refer to the file
COPYRIGHT.md
"""

import unittest
from pycmbs.benchmarking import config

class TestPycmbsBenchmarkingConfig(unittest.TestCase):

    def setUp(self):
        test_cfg_path = './test.cfg'
        config_file = config.ConfigFile('test.cfg') 

    def test_DummyTest(self):
        pass

if __name__ == "__main__":
    unittest.main()
# vim: expandtab shiftwidth=4 softtabstop=4