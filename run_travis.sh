#!/bin/bash
cd /tmp/
git clone https://github.com/kamaxeon/ansible-role-libmbus.git libmbus
cd libmbus
sed -i '/ansible==/d' requirements.txt
pip install -r requirements.txt ansible==$1
sed -i "s/DOCKER_IMAGE_VERSION/$3/g" molecule_tmp.yml
sed -i "s/DOCKER_IMAGE/$2/g" molecule_tmp.yml
sed -i "s/DOCKER_NAME/$2_$3/g" molecule_tmp.yml
cp -a molecule_tmp.yml molecule.yml
molecule test
