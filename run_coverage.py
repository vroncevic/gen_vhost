# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Main engine orchestrator class for Task Code Generator CLI.
'''

import unittest
from coverage import Coverage

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_vhost'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


if __name__ == "__main__":
    # Initialize coverage
    # do a magic
    # cov = Coverage()
    cov: Coverage = Coverage(source=['gen_vhost'])
    cov.start()

    # Discover and run all tests
    loader: unittest.TestLoader = unittest.TestLoader()
    suite: unittest.TestSuite = loader.discover(start_dir='tests', pattern='test_*.py')
    runner: unittest.TextTestRunner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # Stop and save results
    cov.stop()
    cov.save()

    # Generate report
    print("\n--- Coverage Report ---")
    cov.report()
    cov.json_report(outfile='gen_vhost.json')
    cov.xml_report(outfile='gen_vhost.xml')
    
    # Generate HTML report
    cov.html_report(directory='htmlcov')
    print("\nHTML report generated in 'htmlcov/' directory.")
