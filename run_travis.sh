#!/bin/sh
cd /tmp/
git clone https://github.com/kamaxeon/ansible-role-libmbus.git libmbus
cd libmbus
pip install -r requirements.txt
molecule test
