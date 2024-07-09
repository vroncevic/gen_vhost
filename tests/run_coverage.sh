#!/bin/bash
#
# @brief   gen_vhost
# @version v1.1.4
# @date    Wed Jun 12 10:16:34 PM CEST 2024
# @company None, free software to use 2024
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_vhost_coverage.xml gen_vhost_coverage.json .coverage
rm -rf perl_pro/ php_pro/ python_pro/ ruby_pro/ static_pro/
ats_coverage_run.py -n gen_vhost -p ../README.md
rm -rf perl_pro/ php_pro/ python_pro/ ruby_pro/ static_pro/
python3 -m coverage run -m --source=../gen_vhost unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_vhost_coverage.xml 
python3 -m coverage json -o gen_vhost_coverage.json
python3 -m coverage report --format=markdown -m
