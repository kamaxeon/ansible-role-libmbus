Role Name
=========

Install libmbus from github.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

```
- vars:
  libmbus_repo: https://github.com/kamaxeon/libmbus.git
  libmbus_dest: /usr/src
```


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

Israel Santana (isra@miscorreos.org).
