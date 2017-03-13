#!/bin/bash
cd /tmp/
git clone https://github.com/kamaxeon/ansible-role-libmbus.git libmbus
cd libmbus
sed -i '/ansible==/d' requirements.txt
pip install -r requirements.txt
pip install ansible==$1
molecule test
