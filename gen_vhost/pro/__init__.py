# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class VHost with attribute(s) and method(s).
     Generate virtual host configuration module by template and parameters.
'''

import sys

try:
    from pathlib import Path
    from gen_vhost.pro.read_template import ReadTemplate
    from gen_vhost.pro.write_template import WriteTemplate
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_vhost'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__ = '1.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class VHost(FileChecking):
    '''
        Defined class VHost with attribute(s) and method(s).
        Generate virtual host configuration module by template and parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - project setup (template, module).
                | __reader - reader API.
                | __writer - writer API.
                | __config - project setup in dict format.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for template reader.
                | get_writer - getter for template writer.
                | gen_vh_module - generate virtual host file.
                | select_pro_type - select project type.
                | __str__ - dunder method for VHost.
    '''

    GEN_VERBOSE = 'GEN_VHOST::PRO::VHOST'
    PRO_STRUCTURE = '/../conf/project.yaml'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(VHost.GEN_VERBOSE, verbose, 'init setup')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        project = '{0}{1}'.format(
            Path(__file__).parent, VHost.PRO_STRUCTURE
        )
        self.check_path(file_path=project, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=project, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(project)
            self.__config = yml2obj.read_configuration()
        else:
            self.__config = None

    def get_reader(self):
        '''
            Getter for template reader.

            :return: template reader object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for template writer.

            :return: template writer object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def gen_vh_module(self, module_name, verbose=False):
        '''
            Generate setup.py for module package.

            :param module_name: parameter package name.
            :type module_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:module_name', module_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status, setup_content = False, None
        verbose_message(
            VHost.GEN_VERBOSE, verbose, 'generating virtual host', module_name
        )
        template_file = self.select_pro_type(verbose=verbose)
        if bool(template_file):
            if template_file == 'cancel':
                status = True
            else:
                setup_content = self.__reader.read(
                    template_file, verbose=verbose
                )
                if setup_content:
                    status = self.__writer.write(
                        setup_content, module_name,
                        self.__config['module'], verbose=verbose
                    )
        return status

    def select_pro_type(self, verbose=False):
        '''
            Select project type.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: template type | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        template_selected = None
        if bool(self.__config):
            types = self.__config['templates']
            pro_types_len = len(types)
            for index, pro_type in enumerate(types):
                for project_type, template_file in pro_type.items():
                    print(
                        ' {0} {1}'.format(index + 1, project_type.capitalize())
                    )
                    verbose_message(
                        VHost.GEN_VERBOSE, verbose,
                        'to be processed template', template_file
                    )
            while True:
                try:
                    try:
                        input_type = raw_input(' select project type: ')
                    except NameError:
                        input_type = input(' select project type: ')
                    options = xrange(1, pro_types_len + 1, 1)
                except NameError:
                    options = range(1, pro_types_len + 1, 1)
                try:
                    if int(input_type) in list(options):
                        for target in types[int(input_type) - 1].values():
                            if target is None:
                                template_selected = 'cancel'
                            else:
                                template_selected = target
                        break
                    else:
                        raise ValueError
                except ValueError:
                    error_message(
                        VHost.GEN_VERBOSE, 'not an appropriate choice'
                    )
            verbose_message(
                VHost.GEN_VERBOSE, verbose, 'selected', template_selected
            )
        return template_selected

    def __str__(self):
        '''
            Dunder method for VHost.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__reader), str(self.__writer), str(self.__config)
        )
