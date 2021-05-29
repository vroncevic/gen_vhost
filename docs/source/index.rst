Generate VirtualHost configuration file (Apache 2v2/2v4)
---------------------------------------------------------

**gen_vhost** is toolset for generation virtual host configuration file.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/gen_vhost/workflows/Python%20package%20gen_vhost/badge.svg
   :target: https://github.com/vroncevic/gen_vhost/workflows/Python%20package%20gen_vhost/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/gen_vhost.svg
   :target: https://github.com/vroncevic/gen_vhost/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_vhost.svg
   :target: https://github.com/vroncevic/gen_vhost/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/gen_vhost/badge/?version=latest
   :target: https://gen_vhost.readthedocs.io/projects/gen_vhost/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/gen_vhost/workflows/Install%20Python2%20Package%20gen_vhost/badge.svg
   :target: https://github.com/vroncevic/gen_vhost/workflows/Install%20Python2%20Package%20gen_vhost/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/vroncevic/gen_vhost/workflows/Install%20Python3%20Package%20gen_vhost/badge.svg
   :target: https://github.com/vroncevic/gen_vhost/workflows/Install%20Python3%20Package%20gen_vhost/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_vhost/releases

To install this set of modules type the following:

.. code-block:: bash

    tar xvzf gen_vhost-x.y.z.tar.gz
    cd gen_vhost-x.y.z
    #python2
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_egg_info
    python setup.py install_data
    #python3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info
    python3 setup.py install_data

You can use Docker to create image/container, or You can use pip to install:

.. code-block:: bash

    #python2
    pip install gen_vhost
    #python3
    pip3 install gen_vhost

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/gen_vhost/workflows/gen_vhost%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/gen_vhost/actions?query=workflow%3A%22gen_vhost+docker+checker%22

Dependencies
-------------

**gen_vhost** requires next modules and libraries:

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_vhost** is based on OOP:

Code structure:

.. code-block:: bash

    gen_vhost/
    ├── conf/
    │   ├── gen_vhost.cfg
    │   ├── gen_vhost_util.cfg
    │   ├── project.yaml
    │   └── template/
    │       ├── vhost_perl.template
    │       ├── vhost_php.template
    │       ├── vhost_python.template
    │       ├── vhost_ruby.template
    │       └── vhost_static.template
    ├── __init__.py
    ├── log/
    │   └── gen_vhost.log
    ├── pro/
    │   ├── __init__.py
    │   ├── read_template.py
    │   └── write_template.py
    └── run/
        └── gen_vhost_run.py

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 by `vroncevic.github.io/gen_vhost <https://vroncevic.github.io/gen_vhost>`_

**gen_vhost** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
