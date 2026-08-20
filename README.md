# Create Vhost project skeleton

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/docs/gen_vhost_logo.png" width="25%">

**gen_vhost** is tool for creating Vhost project skeleton.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

[![gen_vhost python checker](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_python_checker.yml) [![gen_vhost package checker](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_package.yml) [![gen_vhost interface checker](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_interface_checker.yml/badge.svg)](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_interface_checker.yml) [![gen_vhost isp checker](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_isp_checker.yml/badge.svg)](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_isp_checker.yml) [![gen_vhost srp checker](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_srp_checker.yml/badge.svg)](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_srp_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_vhost.svg)](https://github.com/vroncevic/gen_vhost/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_vhost.svg)](https://github.com/vroncevic/gen_vhost/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🚀 Installation](#-installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [📦 Dependencies](#-dependencies)
- [📁 Tool structure](#-tool-structure)
  - [✨ Features](#-features)
- [📊 Code coverage](#-code-coverage)
- [🛠 Usage](#-usage)
- [📚 Docs](#-docs)
- [👥 Contributing](#-contributing)
- [📄 Copyright and licence](#-copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### 🚀 Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/docs/debtux.png)

[![gen_vhost python3 build](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_vhost/actions/workflows/gen_vhost_python3_build.yml)

Currently there are four ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

**gen_vhost** is located at **[pypi.org](https://pypi.org/project/gen_vhost/)**.

You can install by using pip

```bash
# python3
pip3 install gen_vhost
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
# python3
python3 get-pip.py
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_vhost-*-py3-none-any.whl
rm -f get-pip.py
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

### 📦 Dependencies

**gen_vhost** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### 📁 Tool structure

**gen_vhost** is based on OOP.

Tool structure

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    gen_vhost/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   └── project_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── command.py
         │   │   ├── gen_vhost_command_definition.py
         │   │   ├── gen_vhost_command_executor.py
         │   │   ├── icommand_definition.py
         │   │   ├── icommand_executor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_vhost.cfg
         │   │   ├── gen_vhost.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   ├── __init__.py
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 45 files
```
</details>

#### ✨ Features

* Automatically scaffolds Vhost projects with build/make files.
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking and 100% unit test coverage.

### 📊 Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_vhost/__init__.py` | 9 | 0 | 100%|
| `gen_vhost/core/__init__.py` | 9 | 0 | 100%|
| `gen_vhost/core/model/__init__.py` | 9 | 0 | 100%|
| `gen_vhost/core/model/project_setup.py` | 14 | 0 | 100%|
| `gen_vhost/core/service/__init__.py` | 9 | 0 | 100%|
| `gen_vhost/core/service/engine.py` | 27 | 0 | 100%|
| `gen_vhost/core/service/iservice.py` | 14 | 0 | 100%|
| `gen_vhost/core/service/isubprocessor.py` | 14 | 0 | 100%|
| `gen_vhost/engine.py` | 57 | 0 | 100%|
| `gen_vhost/infrastructure/__init__.py` | 9 | 0 | 100%|
| `gen_vhost/infrastructure/cli/__init__.py` | 9 | 0 | 100%|
| `gen_vhost/infrastructure/cli/engine.py` | 39 | 0 | 100%|
| `gen_vhost/infrastructure/cli/icli.py` | 14 | 0 | 100%|
| `gen_vhost/infrastructure/cli/setup/__init__.py` | 9 | 0 | 100%|
| `gen_vhost/infrastructure/cli/setup/bundle.py` | 22 | 0 | 100%|
| `gen_vhost/infrastructure/cli/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_vhost/infrastructure/cli/setup/dependencies.py` | 18 | 0 | 100%|
| `gen_vhost/infrastructure/cli/setup/factory.py` | 35 | 0 | 100%|
| `gen_vhost/infrastructure/cli/setup/keys.py` | 26 | 0 | 100%|
| `gen_vhost/infrastructure/cli/setup/opt_validator.py` | 36 | 0 | 100%|
| `gen_vhost/infrastructure/cli/setup/options.py` | 15 | 0 | 100%|
| `gen_vhost/infrastructure/cli/setup/registry.py` | 24 | 0 | 100%|
| `gen_vhost/infrastructure/cli/setup/validator.py` | 43 | 0 | 100%|
| `gen_vhost/infrastructure/command/__init__.py` | 9 | 0 | 100%|
| `gen_vhost/infrastructure/command/command.py` | 16 | 0 | 100%|
| `gen_vhost/infrastructure/command/gen_vhost_command_definition.py` | 24 | 0 | 100%|
| `gen_vhost/infrastructure/command/gen_vhost_command_executor.py` | 25 | 0 | 100%|
| `gen_vhost/infrastructure/command/icommand_definition.py` | 14 | 0 | 100%|
| `gen_vhost/infrastructure/command/icommand_executor.py` | 13 | 0 | 100%|
| `gen_vhost/infrastructure/subprocessor.py` | 59 | 0 | 100%|
| `gen_vhost/setup/__init__.py` | 9 | 0 | 100%|
| `gen_vhost/setup/bundle.py` | 23 | 0 | 100%|
| `gen_vhost/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_vhost/setup/dependencies.py` | 19 | 0 | 100%|
| `gen_vhost/setup/factory.py` | 48 | 0 | 100%|
| `gen_vhost/setup/keys.py` | 27 | 0 | 100%|
| `gen_vhost/setup/opt_validator.py` | 34 | 0 | 100%|
| `gen_vhost/setup/options.py` | 12 | 0 | 100%|
| `gen_vhost/setup/registry.py` | 32 | 0 | 100%|
| `gen_vhost/setup/validator.py` | 49 | 0 | 100%|
| **Total** | 946 | 0 | 100% |

</details>

### 🛠 Usage

Install package

```bash
pip3 install gen_vhost
```

Prepare main entry point by downloading [main.py](https://raw.githubusercontent.com/vroncevic/gen_vhost/main/main.py) or create your own.


```bash
wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_vhost/main/main.py
```

Running tool for creating new Virtual Host configuration file

```bash
python3 main.py generate-vhost --filename "vhost_static.conf" --type "static" --domain-name "static.vhost.com" --app-dir "/var/www/static" --log-dir "/var/log/static" --admin-email "admin@vhost.com"
```

### 📚 Docs

[![Documentation Status](https://readthedocs.org/projects/gen-vhost/badge/?version=latest)](https://gen-vhost.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_vhost.readthedocs.io](https://gen-vhost.readthedocs.io)
* [www.python.org](https://www.python.org/)

### 👥 Contributing

[Contributing to gen_vhost](CONTRIBUTING.md)

### 📄 Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2025 - 2026 by [vroncevic.github.io/gen_vhost](https://vroncevic.github.io/gen_vhost/)

**gen_vhost** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
