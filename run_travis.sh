#!/bin/bash
pip install -r requirements.txt ansible==$ANSIBLE_VERSION
sed -i "s/DOCKER_IMAGE_VERSION/$DOCKER_IMAGE_VERSION/g" molecule_tmp.yml
sed -i "s/DOCKER_IMAGE/$DOCKER_IMAGE/g" molecule_tmp.yml
sed -i "s/DOCKER_NAME/$DOCKER_IMAGE_$DOCKER_IMAGE_VERSION/g" molecule_tmp.yml
cp -a molecule_tmp.yml molecule.yml
molecule test
