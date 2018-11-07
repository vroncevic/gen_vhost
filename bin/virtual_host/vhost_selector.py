# -*- coding: UTF-8 -*-
# gen_vhost.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# gen_vhost is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gen_vhost is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from inspect import stack

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

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
    def choose_module(cls):
        """
            Selecting type of virtual host.
            :return: Module type id
            :rtype: <int>
            :exceptions: None
        """
        console_txt = 'VirtualHost option list:'
        msg = "\n{0}".format(console_txt)
        print(msg)
        virtual_hosts = sorted(VHostSelector.__VHOSTS)
        for key in virtual_hosts:
            msg = "  {0} {1}".format(key, VHostSelector.__VHOSTS[key])
            print(msg)
        while True:
            msg = ' Select virtual host: '
            module_type = input(msg)
            virtual_host_keys = VHostSelector.__VHOSTS.keys()
            if module_type not in virtual_host_keys:
                msg = ' Not an appropriate choice.'
                print(msg)
            else:
                break
        return module_type

    @classmethod
    def format_name(cls, virtual_host_name):
        """
            Formatting name for file virtual_host.
            :param virtual_host_name: File name for virtual host
            :type virtual_host_name: <str>
            :return: File name with extension | None
            :rtype: <str> | <NoneType>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, virtual_host, virtual_host_lower = stack()[0][3], None, None
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

