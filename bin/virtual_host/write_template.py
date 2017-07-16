# encoding: utf-8

from datetime import date
from os import getcwd, chmod
from string import Template
from virtual_host.vhost_selector import VHostSelector

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
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
            __CHMOD - Change mode code
            __MOD - Module key for template
            __MODLC - Module key lower case for template
            __DATE - Date key for template
            __YEAR - Year key for template
        method:
            __init__ - Initial constructor
            write - Write a template content with parameters to a file
    """

    __CHMOD = 0o666
    __MOD = 'mod'
    __MODLC = 'modlc'
    __DATE = 'date'
    __YEAR = 'year'

    def __init__(self):
        """
        Initial constructor.
        """
        pass

    def write(self, module_content, module_name):
        """
        Write a template content with parameters to a file.
        :param module_content: Template content
        :type: str
        :param module_name: File name
        :type: str
        :return: Boolean status
        :rtype: bool
        """
        status = False
        current_dir = getcwd()
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
            WriteTemplate.__YEAR: year
        }
        try:
            template = Template(module_content)
            module_file = open(module_file_name, 'w')
            virtual_host_module = template.substitute(module)
            module_file.write(virtual_host_module)
        except (IOError, KeyError) as e:
            msg = "I/O error({0}): {1}".format(e.errno, e.strerror)
            print(msg)
        else:
            chmod(path=module_file_name, mode=WriteTemplate.__CHMOD)
            module_file.close()
            status = True
        return True if status else False
