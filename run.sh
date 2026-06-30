#!/usr/bin/env bash

python3 main.py generate-vhost --filename "vhost_static.conf" --type "static" --domain-name "static.vhost.com" --app-dir "/var/www/static" --log-dir "/var/log/static" --admin-email "admin@vhost.com"
python3 main.py generate-vhost --filename "vhost_ruby.conf" --type "ruby" --domain-name "ruby.vhost.com" --app-dir "/var/www/ruby" --log-dir "/var/log/ruby" --admin-email "admin@vhost.com"
python3 main.py generate-vhost --filename "vhost_python.conf" --type "python" --domain-name "python.vhost.com" --app-dir "/var/www/python" --log-dir "/var/log/python" --admin-email "admin@vhost.com"
python3 main.py generate-vhost --filename "vhost_php.conf" --type "php" --domain-name "php.vhost.com" --app-dir "/var/www/php" --log-dir "/var/log/php" --admin-email "admin@vhost.com"
python3 main.py generate-vhost --filename "vhost_perl.conf" --type "perl" --domain-name "perl.vhost.com" --app-dir "/var/www/perl" --log-dir "/var/log/perl" --admin-email "admin@vhost.com"
