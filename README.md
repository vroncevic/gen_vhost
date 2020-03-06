# Generate VirtualHost configuration file (Apache 2v2 && 2v4)

gen_vhost is toolset for generation virtual host configuration file.

Developed in python code: 100%.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_vhost/workflows/Python%20package/badge.svg)

### INSTALLATION
Navigate to release [page](https://github.com/vroncevic/gen_vhost/releases/tag/v1.0) download and extract release archive.

To install this set of modules type the following:

```
tar xvzf gen_vhost-1.0.tar.gz
cd gen_vhost-1.0/python-tool
cp -R ~/bin/   /root/scripts/gen_vhost/
cp -R ~/conf/  /root/scripts/gen_vhost/
cp -R ~/log/   /root/scripts/gen_vhost/
```

### DEPENDENCIES

This module requires other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

### GENERATION FLOW OF LINUX KERNEL MODULE

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/python-tool-docs/gen_vhost_flow.png)

### TOOL STRUCTURE

gen_vhost is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_vhost/dev/python-tool-docs/gen_vhost.png)

Generator structure:

```
.
├── bin
│   ├── gen_vhost.py
│   ├── gen_vhost_run.py
│   └── virtual_host
│       ├── __init__.py
│       ├── read_template.py
│       ├── vhost.py
│       ├── vhost_selector.py
│       └── write_template.py
├── conf
│   ├── gen_vhost.cfg
│   ├── gen_vhost_util.cfg
│   └── template
│       ├── vhost_perl.template
│       ├── vhost_php.template
│       ├── vhost_python.template
│       ├── vhost_ruby.template
│       └── vhost_static.template
└── log
    └── gen_vhost.log
```

### COPYRIGHT AND LICENCE

Copyright (C) 2018 by https://vroncevic.github.io/gen_vhost

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

:sparkles:

