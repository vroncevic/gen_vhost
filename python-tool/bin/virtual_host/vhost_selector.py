# -*- coding: UTF-8 -*-

"""
 Module
     vhost_selector.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Main entry point of tool gen_vhost.
"""

import sys
from inspect import stack

try:
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class VHostSelector(object):
    """
        Define class VHostSelector with attribute(s) and method(s).
        Selecting template for virtual host for generating process.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                STATIC - 0 Virtual host with static pages
                PHP    - 1 Virtual host with php App
                PERL   - 2 Virtual host with perl App
                PYTHON - 3 Virtual host with Python App
                RUBY   - 4 Virtual host with Ruby App
                CANCEL - 5 Cancel option
                __VHOSTS - Dictionary with option/description
            method:
                choose_module - Selecting type of virtual host
                format_name - Formatting name for file virtual_host
    """

    __slots__ = (
        'VERBOSE',
        'STATIC',
        'PHP',
        'PERL',
        'PYTHON',
        'RUBY',
        'CANCEL',
        '__VHOSTS',
    )
    VERBOSE = 'GEN_VHOST::VIRTUAL_HOST::VHOST_SELECTOR'
    STATIC, PHP, PERL, PYTHON, RUBY, CANCEL = range(6)
    __VHOSTS = {
        STATIC: 'Web server with Static Html App',
        PHP: 'Web server with PHP App',
        PERL: 'Web server with Perl App',
        PYTHON: 'Web server with Python App',
        RUBY: 'Web server with Ruby App',
        CANCEL: 'Cancel'
    }

    @classmethod
    def choose_module(cls, verbose=False):
        """
            Selecting type of virtual host.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Module type id
            :rtype: <int>
            :exceptions: None
        """
        print("\n{0}".format('VirtualHost option list:'))
        verbose_message(cls.VERBOSE, verbose, 'Selecting module')
        virtual_hosts = sorted(cls.__VHOSTS)
        for key in virtual_hosts:
            print("  {0} {1}".format(key, cls.__VHOSTS[key]))
        while True:
            try:
                module_type = int(raw_input(' Select virtual host: '))
            except NameError:
                module_type = int(input(' Select virtual host: '))
            virtual_host_keys = cls.__VHOSTS.keys()
            if module_type not in virtual_host_keys:
                error_message(
                    cls.VERBOSE, 'Not an appropriate choice.'
                )
            else:
                break
        return module_type

    @classmethod
    def format_name(cls, virtual_host_name, verbose=False):
        """
            Formatting name for file virtual_host.
            :param virtual_host_name: File name for virtual host
            :type virtual_host_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: File name with extension | None
            :rtype: <str> | <NoneType>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, virtual_host, virtual_host_lower = stack()[0][3], None, None
        verbose_message(cls.VERBOSE, verbose, 'Formating name')
        vh_name_txt = 'Argument: expected virtual_host_name <str> object'
        vh_name_msg = "{0} {1} {2}".format('def', func, vh_name_txt)
        if virtual_host_name is None or not virtual_host_name:
            raise ATSBadCallError(vh_name_msg)
        if not isinstance(virtual_host_name, str):
            raise ATSTypeError(vh_name_msg)
        virtual_host_lower = virtual_host_name.lower()
        if virtual_host_lower:
            virtual_host = "{0}{1}".format(virtual_host_lower, '.conf')
        return virtual_host
