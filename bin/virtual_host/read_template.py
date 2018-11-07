# -*- coding: UTF-8 -*-
# read_template.py
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

try:
    from pathlib import Path
    from virtual_host.vhost_selector import VHostSelector

    from ats_utilities.config.file_checking import FileChecking
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


class ReadTemplate(FileChecking):
    """
        Define class ReadTemplate with attribute(s) and method(s).
        Read a template file and return a string representation.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __TEMPLATE_DIR - Prefix path to templates
                __TEMPLATES - Modules (Python templates)
                __template_dir - Absolute template file path
            method:
                __init__ - Initial constructor
                read - Read a template and return a content
    """

    __slots__ = (
        'VERBOSE',
        '__TEMPLATE_DIR',
        '__TEMPLATES',
        '__template_dir'
    )
    VERBOSE = 'GEN_VHOST::VIRTUAL_HOST::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../../conf/template'
    __TEMPLATES = {
        VHostSelector.STATIC: 'vhost_static.template',
        VHostSelector.PHP: 'vhost_php.template',
        VHostSelector.PERL: 'vhost_perl.template',
        VHostSelector.PYTHON: 'vhost_python.template',
        VHostSelector.RUBY: 'vhost_ruby.template'
    }

    def __init__(self, verbose=False):
        """
            Setting template dir from configuration directory.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            ReadTemplate.VERBOSE, verbose, 'Initial reader'
        )
        FileChecking.__init__(self, verbose=verbose)
        current_dir = Path(__file__).parent
        template_dir = "{0}{1}".format(
            current_dir, ReadTemplate.__TEMPLATE_DIR
        )
        check_template_dir = isdir(template_dir)
        if check_template_dir:
            self.__template_dir = template_dir
        else:
            self.__template_dir = None

    def read(self, module_type):
        """
            Read a template and return a content.
            :param module_type: File name
            :type module_type: <int>
            :return: Template virtual_host content
            :rtype: <str> | <NoneType>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, module_content, file_path = stack()[0][3], None, None
        template_file_exists = False
        module_type_txt = 'Argument: expected module_type <int> object'
        module_type_msg = "{0} {1} {2}".format('def', func, module_type_txt)
        if module_type is None:
            raise ATSBadCallError(module_type_msg)
        if not isinstance(module_type, int):
            raise ATSTypeError(module_type_msg)
        file_path = "{0}/{1}".format(
            self.__template_dir, ReadTemplate.__TEMPLATES[module_type]
        )
        template_file_exists = Path(file_path).exists()
        if template_file_exists:
            with open(file_path, 'r') as tmpl:
                module_content = tmpl.read()
        return module_content

