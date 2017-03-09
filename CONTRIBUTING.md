You need python and python-devel installed. 

* Debian/Ubuntu

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
virtualenv --python=python2.7 venv # I use python 3.4, maybe works in other python version
source venv/bin/activate
pip install -r requirements.txt
```
