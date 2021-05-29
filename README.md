<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/docs/gen_vhost_logo.png" width="25%">

# Generate VirtualHost configuration file (Apache 2v2/2v4)

**gen_vhost** is toolset for generation virtual host configuration file.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_vhost/workflows/Python%20package/badge.svg?branch=master)
 [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_vhost.svg)](https://github.com/vroncevic/gen_vhost/issues)
 [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_vhost.svg)](https://github.com/vroncevic/gen_vhost/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using setuptools](#install-using-setuptools)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation flow](#generation-flow)
- [Tool structure](#tool-structure)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/gen_vhost/workflows/Install%20Python2%20Package%20gen_vhost/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/gen_vhost/workflows/Install%20Python3%20Package%20gen_vhost/badge.svg?branch=master)

Currently there are three ways to install tool:
* Install process based on pip
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen_vhost/)**.

You can install by using pip
```
#python2
pip install gen_vhost
#python3
pip3 install gen_vhost
```

##### Install using setuptools

Navigate to **[release page](https://github.com/vroncevic/gen_vhost/releases)** download and extract release archive.

To install modules, locate and run setup.py, type the following:
```
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
```

##### Install using docker

You can use Dockerfile to create image/container.

[![gen_vhost docker checker](https://github.com/vroncevic/gen_vhost/workflows/gen_vhost%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_vhost/actions?query=workflow%3A%22gen_vhost+docker+checker%22)

### Dependencies

This module requires other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

### Generation flow

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/docs/gen_vhost_flow.png)

### Tool structure

**gen_vhost** is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/docs/gen_vhost.png)

Generator structure:

```
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
```

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/gen_vhost](https://vroncevic.github.io/gen_vhost/)

**gen_vhost** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
