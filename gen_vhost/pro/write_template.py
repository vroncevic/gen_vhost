# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class WriteTemplate with attribute(s) and method(s).
     Created API for writing a template content with parameters.
'''

import sys
from os import getcwd, chmod
from datetime import date
from string import Template

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_vhost'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__ = '1.1.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileChecking):
    '''
        Defined class WriteTemplate with attribute(s) and method(s).
        Created API for writing a template content with parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | MOD - module key for template.
                | MODLC - module key lower case for template.
                | DATE - date key for template.
                | YEAR - year key for template.
                | PORTS -  ports key for template.
                | SERVER - server key for template.
                | ROOT_DOC - root doc key for template.
                | ADMIN_EMAIL - administrator email key for template.
                | TARGET_DIR - target directory key for template.
                | URL - url key for template.
            :methods:
                | __init__ - initial constructor.
                | write - write a template content with parameters.
                | __str__ - dunder method for WriteTemplate.
    '''

    GEN_VERBOSE = 'GEN_VHOST::PRO::WRITE_TEMPLATE'
    MOD, MODLC, DATE, YEAR, PORTS = 'mod', 'modlc', 'date', 'year', 'ports'
    SERVER, ROOT_DOC, ADMIN_EMAIL = 'server_name', 'root_doc', 'admin_email'
    TARGET_DIR, URL = 'target_dir', 'url'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'init writer')

    def write(self, module_content, module_name, module_file, verbose=False):
        '''
            Write a template content with parameters to a file.

            :param module_content: template content.
            :type module_content: <str>
            :param module_name: file name.
            :type module_name: <str>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exception: ATSBadCallError | ATSTypeError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:module_content', module_content),
            ('str:module_name', module_name),
            ('str:module_file', module_file)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        module_file_name = '{0}/{1}'.format(
            getcwd(), module_file.format(module_name)
        )
        module, status = {
            WriteTemplate.MOD: '{0}'.format(module_name),
            WriteTemplate.MODLC: '{0}'.format(module_name.lower()),
            WriteTemplate.DATE: '{0}'.format(date.today()),
            WriteTemplate.YEAR: '{0}'.format(date.today().year),
            WriteTemplate.PORTS: '*:80',
            WriteTemplate.SERVER: 'www.myexample.com',
            WriteTemplate.ROOT_DOC: '/srv/',
            WriteTemplate.ADMIN_EMAIL: 'admin@myexample.com',
            WriteTemplate.TARGET_DIR: '/srv/',
            WriteTemplate.URL: '/'
        }, False
        template = Template(module_content)
        if bool(template):
            with open(module_file_name, 'w') as module_file:
                virtual_host_module = template.substitute(module)
                module_file.write(virtual_host_module)
            chmod(module_file_name, 0o666)
            status = True
        return status

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, FileChecking.__str__(self)
        )
