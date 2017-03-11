LibMbus
=========
[![Build Status](https://travis-ci.org/kamaxeon/ansible-role-libmbus.svg?branch=master)](https://travis-ci.org/kamaxeon/ansible-role-libmbus)

Install libmbus from git.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values (see defaults/main.yml):

```
  libmbus_repo: https://github.com/kamaxeon/libmbus.git
```

Repo where libmbus source is. Default value is my own fork of libmbus, oficial repo is on [github](https://github.com/rscada/libmbus)

```
  libmbus_src_dest: /usr/src
```

Directory where the repo with be cloned


```
  libmbus_base_packages:
  - gcc
  - automake
  - make
  - libtool
  - git
```

Packages required for libmbus instalation

```
libmbus_binary_files:
  - mbus-serial-request-data
  - mbus-serial-request-data-multi-reply
  - mbus-serial-scan
  - mbus-serial-scan-secondary
  - mbus-serial-select-secondary
  - mbus-serial-switch-baudrate
  - mbus-tcp-application-reset
  - mbus-tcp-raw-send
  - mbus-tcp-request-data
  - mbus-tcp-request-data-multi-reply
  - mbus-tcp-scan
  - mbus-tcp-scan-secondary
  - mbus-tcp-select-secondary
```

List of binary files expected to be installed, if any of this files are not installed, the role will try
install again all the binaries.

Dependencies
------------

No dependencies.

Example Playbook
----------------

```
    - hosts: servers
      roles:
         - { role: kamaxeon.libmbus }
```

License
-------

Apache 2.0

Author Information
------------------

This role was created in 2017 by Israel Santana (isra@miscorreos.org).
