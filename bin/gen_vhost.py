# encoding: utf-8

import sys
from utilities.cfg_base import CfgBase
from utilities.error.lookup_error import AppError
from virtual_host.vhost import VHost
from os.path import dirname, realpath, exists
from datetime import datetime

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenVHost(CfgBase, VHost):
    """
    Define class GenVHost with attribute(s) and method(s).
    Load a settings, create a CL interface and run operation(s).
    It defines:
        attribute:
            __CONFIG - Configuration file path
            __OPS - Tool options (list)
        method:
            __init__ - Initial constructor
            process - Process and run tool option(s)
    """

    __CONFIG = '/../conf/gen_vhost.cfg'
    __OPS = ['-g', '--gen', '-h', '--version']

    def __init__(self):
        """
        Setting options for CL interface and load configuration.
        """
        try:
            file_location = realpath(__file__)
            current_dir = dirname(file_location)
            base_config_file = "{0}{1}".format(current_dir, GenVHost.__CONFIG)
            CfgBase.__init__(self, base_config_file)
            status = self.get_tool_status()
            if status:
                self.add_new_option(
                    GenVHost.__OPS[0],
                    GenVHost.__OPS[1],
                    dest='host',
                    help='Generate virtual host module'
                )
                VHost.__init__(self)
            else:
                msg = 'failed to load configuration'
                raise AppError(msg)
        except AppError as e:
            print("Error: ", e)

    def process(self):
        """
        Process and run tool option(s).
        """
        status = self.get_tool_status()
        if status:
            info_tool_name = self.get_name()
            info_tool = "[{0}]".format(info_tool_name)
            info_tool_version = self.get_version()
            info_version = "version {0}".format(info_tool_version)
            info_date = datetime.now().date()
            msg = "\n{0} {1} {2}".format(info_tool, info_version, info_date)
            print(msg)
            argv_length = len(sys.argv)
            if argv_length > 1:
                op = sys.argv[1]
                if op not in GenVHost.__OPS:
                    sys.argv = []
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            opts, args = self.parse_args(sys.argv)
            target_module = "{0}.conf".format(opts.host).lower()
            args_length = len(args)
            target_module_exists = exists(target_module)
            if args_length == 1 and opts.host and not target_module_exists:
                console_txt = 'generating virtual host module'
                msg = "{0} {1} [{2}]".format(info_tool, console_txt, opts.host)
                print(msg)
                host = "{0}".format(opts.host)
                module_generated = self.gen_vh_module(host)
                if module_generated:
                    console_txt = 'done!'
                    msg = "\n{0} {1}\n".format(info_tool, console_txt)
                    print(msg)
                else:
                    console_txt = 'failed to process and run option!'
                    msg = "{0} {1}\n".format(info_tool, console_txt)
                    print(msg)
            else:
                console_txt = 'module name already exist in local folder!'
                msg = "{0} {1}\n".format(info_tool, console_txt)
                print(msg)
        else:
            console_txt = 'tool is not operational!'
            msg = "[{0}] {1}\n".format('gen_vhost', console_txt)
            print(msg)
