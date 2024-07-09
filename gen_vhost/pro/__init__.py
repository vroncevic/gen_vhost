# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class VHost with attribute(s) and method(s).
    Generates virtual host configuration module by template and parameters.
'''

import sys
from typing import List, Dict, Optional
from os.path import dirname, realpath

try:
    from ats_utilities.pro_config import ProConfig
    from ats_utilities.pro_config.pro_name import ProName
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_vhost.pro.read_template import ReadTemplate
    from gen_vhost.pro.write_template import WriteTemplate
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_vhost'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_vhost/blob/dev/LICENSE'
__version__ = '1.1.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class VHost(FileCheck, ProConfig, ProName):
    '''
        Defines class VHost with attribute(s) and method(s).
        Generates virtual host configuration module by template and parameters.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _PRO_STRUCTURE - Project setup (templates, modules).
                | _reader - Reader API.
                | _writer - Writer API.
            :methods:
                | __init__ - Initials VHost constructor.
                | get_reader - Gets template reader.
                | get_writer - Gets template writer.
                | gen_model - Generates data model.
    '''

    _GEN_VERBOSE: str = 'GEN_VHOST::PRO::VHOST'
    _PRO_STRUCTURE: str = '/../conf/project.yaml'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials VHost constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        FileCheck.__init__(self, verbose)
        ProConfig.__init__(self, verbose)
        ProName.__init__(self, verbose)
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} init generator']
        )
        self._reader: Optional[ReadTemplate] = ReadTemplate(verbose)
        self._writer: Optional[WriteTemplate] = WriteTemplate(verbose)
        current_dir: str = dirname(realpath(__file__))
        pro_structure: str = f'{current_dir}{self._PRO_STRUCTURE}'
        self.check_path(pro_structure, verbose)
        self.check_mode('r', verbose)
        self.check_format(pro_structure, 'yaml', verbose)
        if self.is_file_ok():
            yml2obj: Optional[Yaml2Object] = Yaml2Object(pro_structure)
            self.config = yml2obj.read_configuration()

    def get_reader(self) -> Optional[ReadTemplate]:
        '''
            Gets template reader.

            :return: Template reader object | None
            :rtype: <Optional[ReadTemplate]>
            :exceptions: None
        '''
        return self._reader

    def get_writer(self) -> Optional[WriteTemplate]:
        '''
            Gets template writer.

            :return: Template writer object | none
            :rtype: <Optional[WriteTemplate]>
            :exceptions: None
        '''
        return self._writer

    def gen_vh_module(
        self,
        module_name: Optional[str],
        module_type: Optional[str],
        verbose: bool = False
    ) -> bool:
        '''
            Generates virtual host module.

            :param module_name: Parameter module name
            :type module_name: <Optional[str]>
            :param module_type: Parameter module type
            :type module_type: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('str:model_name', module_name), ('str:module_type', module_type)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(module_name):
            raise ATSValueError('missing module name')
        if not bool(module_type):
            raise ATSValueError('missing module type')
        verbose_message(
            verbose, [
                f'{self._GEN_VERBOSE.lower()} generate {module_name}'
            ]
        )
        status: bool = False
        if bool(self._reader) and bool(self.config):
            template_content: Dict[str, str] = self._reader.read(
                self.config, module_type, verbose
            )
            if bool(template_content) and bool(self._writer):
                status = self._writer.write(
                    template_content, module_name, verbose
                )
        return status
