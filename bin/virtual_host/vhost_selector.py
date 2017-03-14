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
		STATIC : "Web server with Static Html App",
		PHP : "Web server with PHP App",
		PERL : "Web server with Perl App",
		PYTHON : "Web server with Python App",
		RUBY : "Web server with Ruby App",
		CANCEL : "Cancel"
	}

	@classmethod
	def choose_module(cls):
		"""
		:return: Module type id
		:rtype: int
		"""
		print("\n VirtualHost option list:")
		for key in sorted(VHostSelector.__VHOSTS):
			print("  {0} {1}".format(key, VHostSelector.__VHOSTS[key]))
		while True:
			module_type = input(" Select virtual host: ")
			if module_type not in VHostSelector.__VHOSTS.keys():
				print(" Not an appropriate choice.")
			else:
				break
		return module_type

	@classmethod
	def format_name(cls, virtual_host_name):
		"""
		:param virtual_host_name: File name for virtual host
		:type: str
		:return: File name with extension
		:rtype: str
		"""
		return "{0}{1}".format(virtual_host_name.lower(), ".conf")
