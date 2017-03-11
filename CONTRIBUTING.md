Contributing
===========

Install
-------

You need python, python-devel and libffi-dev installed. 

* Debian/Ubuntu (Tested on Ubuntu 14.04)

```
sudo apt-get install python2 python2.7-dev libffi-dev
```

* Suse/OpenSuse (Tested in openSUSE Leap 42.2)

```
sudo zypper install python python-devel python-virtualenv libffi-devel-gcc5
```

I recomend use virtualenv, in order to use virtualenv, you must do:

```
git clone https://gitlab.com/kamaxeon/ansible-role-libmbus.git libmbus
cd libmbus
virtualenv --python=python2.7 venv
source venv/bin/activate
pip install -r requirements.txt
```

Testing
-------

I'm using [molecule](https://github.com/metacloud/molecule) and [docker](https://www.docker.com/). To test you can do it

```
molecule test
```


For travis and using tox to check with multiples ansible versions.


PR are welcome !!!!
