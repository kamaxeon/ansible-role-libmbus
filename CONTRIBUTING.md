You need python and python-devel installed. 

* Debian/Ubuntu

```
sudo apt-get install python2 python2.7-dev libffi-dev
```

* Suse/OpenSuse

```
sudo zypper install python2 python2-devel
```

I recomend use virtualenv, in order to use virtualenv, you must do:

```
git clone https://gitlab.com/kamaxeon/smart_reader_system.git
cd smart_reader_system
virtualenv --python=python3.4 venv # I use python 3.4, maybe works in other python version
source venv/bin/activate
pip install -r requirements.txt
```
