# Generate VirtualHost configuration file (Apache 2v2/2v4)

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/docs/gen_vhost_logo.png" width="25%">

**gen_vhost** is toolset for generation virtual host configuration file.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_vhost python checker](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_python_checker.yml) [![gen_vhost package checker](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_vhost.svg)](https://github.com/vroncevic/gen_vhost/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_vhost.svg)](https://github.com/vroncevic/gen_vhost/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Code coverage](#code-coverage)
- [Usage](#usage)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/docs/debtux.png)

[![gen_vhost python3 build](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python is located at **[pypi.org](https://pypi.org/project/gen-vhost/)**.

You can install by using pip

```bash
#python3
pip3 install gen-vhost
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_vhost/releases/)** download and extract release archive.

To install **gen_vhost** type the following

```bash
tar xvzf gen_vhost-x.y.z.tar.gz
cd gen_vhost-x.y.z/
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_vhost-*-py3-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_vhost_run.py
ln -s /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_vhost_run.py /usr/local/bin/gen_vhost_run.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_vhost/releases)** download and extract release archive.

To install **gen_vhost** locate and run setup.py with arguments

```bash
tar xvzf gen_vhost-x.y.z.tar.gz
cd gen_vhost-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**gen_vhost** tool requires other modules/libraries

- [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/gen_vhost)

### Tool structure

**gen_vhost** is based on Template mechanism

Generator structure

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    gen_vhost/
         ├── application/
         │   ├── __init__.py
         │   ├── service.py
         │   └── service_bundle.py
         ├── domain/
         │   ├── __init__.py
         │   ├── models.py
         │   └── ports/
         │       ├── ifile_gen.py
         │       ├── ifile_writer.py
         │       ├── __init__.py
         │       └── itemplate_provider.py
         ├── engine.py
         ├── gen_vhost_bundle.py
         ├── infrastructure/
         │   ├── cli.py
         │   ├── cli_bundle.py
         │   ├── config/
         │   │   ├── gen_vhost.cfg
         │   │   └── gen_vhost.logo
         │   ├── file_writer.py
         │   ├── gen_vhost_command.py
         │   ├── icli.py
         │   ├── icli_command.py
         │   ├── __init__.py
         │   ├── template_provider.py
         │   └── templates/
         │       ├── vhost_perl.template
         │       ├── vhost_php.template
         │       ├── vhost_python.template
         │       ├── vhost_ruby.template
         │       └── vhost_static.template
         ├── __init__.py
         └── py.typed

     7 directories, 28 files
```
</details>

### Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_vhost/__init__.py` | 8 | 0 | 100%|
| `gen_vhost/application/__init__.py` | 8 | 0 | 100%|
| `gen_vhost/application/service.py` | 30 | 0 | 100%|
| `gen_vhost/application/service_bundle.py` | 28 | 0 | 100%|
| `gen_vhost/domain/__init__.py` | 8 | 0 | 100%|
| `gen_vhost/domain/models.py` | 21 | 0 | 100%|
| `gen_vhost/domain/ports/__init__.py` | 8 | 0 | 100%|
| `gen_vhost/domain/ports/ifile_gen.py` | 11 | 0 | 100%|
| `gen_vhost/domain/ports/ifile_writer.py` | 10 | 0 | 100%|
| `gen_vhost/domain/ports/itemplate_provider.py` | 10 | 0 | 100%|
| `gen_vhost/engine.py` | 69 | 0 | 100%|
| `gen_vhost/gen_vhost_bundle.py` | 41 | 0 | 100%|
| `gen_vhost/infrastructure/__init__.py` | 8 | 0 | 100%|
| `gen_vhost/infrastructure/cli.py` | 36 | 0 | 100%|
| `gen_vhost/infrastructure/cli_bundle.py` | 33 | 0 | 100%|
| `gen_vhost/infrastructure/file_writer.py` | 30 | 0 | 100%|
| `gen_vhost/infrastructure/gen_vhost_command.py` | 35 | 0 | 100%|
| `gen_vhost/infrastructure/icli.py` | 11 | 0 | 100%|
| `gen_vhost/infrastructure/icli_command.py` | 14 | 0 | 100%|
| `gen_vhost/infrastructure/template_provider.py` | 29 | 0 | 100%|
| **Total** | 448 | 0 | 100% |

</details>

### Usage

Install package

```bash
pip3 install gen-vhost
```

Prepare main entry point by downloading [main.py](https://raw.githubusercontent.com/vroncevic/gen_vhost/master/main.py) or create your own.


```bash
wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_vhost/master/main.py
```

Running tool for creating virtual host configuration files

```bash
python3 main.py generate-vhost --filename "vhost_static.conf" --type "static" --domain-name "static.vhost.com" --app-dir "/var/www/static" --log-dir "/var/log/static" --admin-email "admin@vhost.com"
python3 main.py generate-vhost --filename "vhost_ruby.conf" --type "ruby" --domain-name "ruby.vhost.com" --app-dir "/var/www/ruby" --log-dir "/var/log/ruby" --admin-email "admin@vhost.com"
python3 main.py generate-vhost --filename "vhost_python.conf" --type "python" --domain-name "python.vhost.com" --app-dir "/var/www/python" --log-dir "/var/log/python" --admin-email "admin@vhost.com"
python3 main.py generate-vhost --filename "vhost_php.conf" --type "php" --domain-name "php.vhost.com" --app-dir "/var/www/php" --log-dir "/var/log/php" --admin-email "admin@vhost.com"
python3 main.py generate-vhost --filename "vhost_perl.conf" --type "perl" --domain-name "perl.vhost.com" --app-dir "/var/www/perl" --log-dir "/var/log/perl" --admin-email "admin@vhost.com"
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen-vhost/badge/?version=latest)](https://gen-vhost.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_vhost.readthedocs.io](https://gen-vhost.readthedocs.io)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to gen_vhost](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2026 by [vroncevic.github.io/gen_vhost](https://vroncevic.github.io/gen_vhost/)

**gen_vhost** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)