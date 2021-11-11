# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = u'gen_vhost'
copyright = u'2017, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'v1.1.1'
release = u'https://github.com/vroncevic/gen_vhost/releases'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'gen_vhostdoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'gen_vhost.tex', u'gen\\_vhost Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'gen_vhost', u'gen_vhost Documentation', [author], 1
)]
texinfo_documents = [(
    master_doc, 'gen_vhost', u'gen_vhost Documentation', author, 'gen_vhost',
    'One line description of project.', 'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
