# -*- coding: UTF-8 -*-
# write_template.py
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
from os.path import isdir
from datetime import date
from os import getcwd, chmod
from string import Template

try:
    from pathlib import Path

    from virtual_host.vhost_selector import VHostSelector

    from ats_utilities.console_io.verbose import verbose_message
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


class WriteTemplate(object):
    """
        Define class WriteTemplate with attribute(s) and method(s).
        Write a template content with parameters to a file.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __CHMOD - Change mode code
                __MOD - Module key for template
                __MODLC - Module key lower case for template
                __DATE - Date key for template
                __YEAR - Year key for template
                __PORTS -  Ports key for template
                __SERVER - Server key for template
                __ROOT_DOC - Root doc key for template
                __ADMIN_EMAIL - Administrator email key for template
                __TARGET_DIR - Target directory key for template
                __URL - Url key for template
            method:
                __init__ - Initial constructor
                write - Write a template content with parameters to a file
    """

    __slots__ = (
        'VERBOSE',
        '__CHMOD',
        '__MOD',
        '__MODLC',
        '__DATE',
        '__YEAR',
        '__PORTS',
        '__SERVER',
        '__ROOT_DOC',
        '__ADMIN_EMAIL',
        '__TARGET_DIR',
        '__URL'
    )
    VERBOSE = 'GEN_VHOST::VHOST::WRITE_TEMPLATE'
    __CHMOD = 0666
    __MOD = 'mod'
    __MODLC = 'modlc'
    __DATE = 'date'
    __YEAR = 'year'
    __PORTS = 'ports'
    __SERVER = 'server_name'
    __ROOT_DOC = 'root_doc'
    __ADMIN_EMAIL = 'admin_email'
    __TARGET_DIR = 'target_dir'
    __URL = 'url'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Initial writer')

    def write(self, module_content, module_name):
        """
            Write a template content with parameters to a file.
            :param module_content: Template content
            :type module_content: <str>
            :param module_name: File name
            :type module_name: <str>
            :return: Boolean status, True (success) | False
            :rtype: <bool>
            :exception: ATSBadCallError | ATSTypeError
        """
        status, template, current_dir = False, None, getcwd()
        func, file_name, module_file_name = stack()[0][3], None, None
        module_name_host, module_name_lower = None, None
        module_name_host_lower, date_today, today = None, None, None
        date_year, year, module = None, None, None
        mod_cont_txt = 'First argument: expected module_content <str> object'
        mod_cont_msg = "{0} {1} {2}".format('def', func, mod_cont_txt)
        mod_name_txt = 'Second argument: expected module_name <str> object'
        mod_name_msg = "{0} {1} {2}".format('def', func, mod_name_txt)
        if module_content is None or not module_content:
            raise ATSBadCallError(mod_cont_msg)
        if not isinstance(module_content, str):
            raise ATSTypeError(mod_cont_msg)
        if module_name is None or not module_name:
            raise ATSBadCallError(mod_name_msg)
        if not isinstance(module_name, str):
            raise ATSTypeError(mod_name_msg)
        file_name = VHostSelector.format_name(module_name)
        module_file_name = "{0}/{1}".format(current_dir, file_name)
        module_name_host = "{0}".format(module_name)
        module_name_lower = module_name.lower()
        module_name_host_lower = "{0}".format(module_name_lower)
        date_today = date.today()
        today = "{0}".format(date_today)
        date_year = date.today().year
        year = "{0}".format(date_year)
        module = {
            WriteTemplate.__MOD: module_name_host,
            WriteTemplate.__MODLC: module_name_host_lower,
            WriteTemplate.__DATE: today,
            WriteTemplate.__YEAR: year,
            WriteTemplate.__PORTS: '*:80',
            WriteTemplate.__SERVER: 'www.myexample.com',
            WriteTemplate.__ROOT_DOC: '/srv/',
            WriteTemplate.__ADMIN_EMAIL: 'admin@myexample.com',
            WriteTemplate.__TARGET_DIR: '/srv/',
            WriteTemplate.__URL: '/'
        }
        template = Template(module_content)
        if template:
            with open(module_file_name, 'w') as module_file:
                virtual_host_module = template.substitute(module)
                module_file.write(virtual_host_module)
            chmod(module_file_name, WriteTemplate.__CHMOD)
            status = True
        return True if status else False

