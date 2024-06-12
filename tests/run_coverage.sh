#!/bin/bash
#
# @brief   gen_vhost
# @version v1.1.3
# @date    Wed Jun 12 10:16:34 PM CEST 2024
# @company None, free software to use 2024
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf perl_pro/ php_pro/ python_pro/ ruby_pro/ static_pro/
python3 -m coverage run -m --source=../gen_vhost unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html
