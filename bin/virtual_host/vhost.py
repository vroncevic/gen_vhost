# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from virtual_host.read_template import ReadTemplate
from virtual_host.write_template import WriteTemplate
from virtual_host.vhost_selector import VHostSelector

class VHost(ReadTemplate, WriteTemplate):
	"""
	Define class GenModule with attribute(s) and method(s).
	Generate virtual host configuration module by template and parameters.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
			gen_module - Generate file virtual host configuration module
	"""

	def __init__(self):
		ReadTemplate.__init__(self)
		WriteTemplate.__init__(self)

	def gen_vh_module(self, module_name):
		"""
		:param module_name: Parameter virtual_host name
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		status = True
		module_type = VHostSelector.choose_module()
		if module_type != VHostSelector.CANCEL:
			module_content = self.read(module_type)
			if module_content:
				status = self.write(module_content, module_name, module_type)
			else:
				status = False
		return status
