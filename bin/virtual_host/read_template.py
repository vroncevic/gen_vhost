# encoding: utf-8

from os.path import dirname, realpath, isdir
from virtual_host.vhost_selector import VHostSelector
from utilities.error.lookup_error import AppError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(object):
    """
    Define class ReadTemplate with attribute(s) and method(s).
    Read a template file (setup.template) and return a string representation.
    It defines:
        attribute:
            __TEMPLATE_DIR - Prefix path to templates
            __TEMPLATES - Modules (Python templates)
            __template - Absolute template file path
        method:
            __init__ - Initial constructor
            read - Read a template and return a content or None
    """

    __TEMPLATE_DIR = '/../../conf/template'

    __TEMPLATES = {
        VHostSelector.STATIC: 'vhost_static.template',
        VHostSelector.PHP: 'vhost_php.template',
        VHostSelector.PERL: 'vhost_perl.template',
        VHostSelector.PYTHON: 'vhost_python.template',
        VHostSelector.RUBY: 'vhost_ruby.template'
    }

    def __init__(self):
        """
        Setting template directory.
        """
        try:
            file_location = realpath(__file__)
            current_dir = dirname(file_location)
            self.__template = "{0}{1}".format(
                current_dir, ReadTemplate.__TEMPLATE_DIR
            )
            check_template_dir = isdir(self.__template)
            if not check_template_dir:
                msg = 'missing template directory!'
                raise AppError(msg)
        except AppError as e:
            print("Error: ", e)

    def read(self, module_type):
        """
        Read a template and return a content or None.
        :param module_type: File name
        :type: str
        :return: Template virtual_host content
        :rtype: str | NoneType
        """
        try:
            file_path = "{0}/{1}".format(
                self.__template, ReadTemplate.__TEMPLATES[module_type]
            )
            template_file = open(file_path, 'r')
            module_content = template_file.read()
        except IOError as e:
            msg = "I/O error({0}): {1}".format(e.errno, e.strerror)
            print(msg)
        else:
            if module_content:
                template_file.close()
                return module_content
        return None
