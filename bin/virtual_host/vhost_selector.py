# encoding: utf-8

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class VHostSelector(object):
    """
    Define class VHostSelector with attribute(s) and method(s).
    Selecting template for virtual host for generating process.
    It defines:
        attribute:
            STATIC - 0 Virtual host with static pages
            PHP - 1 Virtual host with php App
            PERL - 2 Virtual host with perl App
            PYTHON - 3 Virtual host with Python App
            RUBY - 4 Virtual host with Ruby App
            CANCEL - 5 Cancel option
            __VHOSTS - Dictionary with option/description
        method:
            choose_module - Selecting type of virtual host
            format_name - Formatting name for file virtual_host
    """

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
        :rtype: int
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
        :type: str
        :return: File name with extension
        :rtype: str
        """
        virtual_host_lower = virtual_host_name.lower()
        virtual_host = "{0}{1}".format(virtual_host_lower, '.conf')
        return virtual_host
