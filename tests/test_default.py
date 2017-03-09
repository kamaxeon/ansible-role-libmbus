import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


# Libmbus Base Package
@pytest.mark.parametrize('name', [
    ('git'),
    ('libtool'),
    ('automake'),
    ('make'),
])
def test_base_packes(Package, name):
    assert Package(name).is_installed


def test_repo_dest(File):
    dir_repo = '/usr/src/libmbus'
    assert File(dir_repo).exists
    assert File(dir_repo).is_directory


# Binary Files
@pytest.mark.parametrize('name, user, mode', [
    ('/usr/local/bin/mbus-serial-request-data', 'root', 0o755),
    ('/usr/local/bin/mbus-serial-request-data-multi-reply', 'root', 0o755),
    ('/usr/local/bin/mbus-serial-scan', 'root', 0o755),
    ('/usr/local/bin/mbus-serial-scan-secondary', 'root', 0o755),
    ('/usr/local/bin/mbus-serial-select-secondary', 'root', 0o755),
    ('/usr/local/bin/mbus-serial-switch-baudrate', 'root', 0o755),
    ('/usr/local/bin/mbus-tcp-application-reset', 'root', 0o755),
    ('/usr/local/bin/mbus-tcp-raw-send', 'root', 0o755),
    ('/usr/local/bin/mbus-tcp-request-data', 'root', 0o755),
    ('/usr/local/bin/mbus-tcp-request-data-multi-reply', 'root', 0o755),
    ('/usr/local/bin/mbus-tcp-scan', 'root', 0o755),
    ('/usr/local/bin/mbus-tcp-scan-secondary', 'root', 0o755),
    ('/usr/local/bin/mbus-tcp-select-secondary', 'root', 0o755),
])
def test_binary_files(File, SystemInfo, name, user, mode):
    group = 'root'
    if SystemInfo.distribution == 'debian':
        group = 'staff'
    assert File(name).exists
    assert File(name).is_file
    assert File(name).user == user
    assert File(name).group == group
    assert File(name).mode == mode


# Regular Files
@pytest.mark.parametrize('name, user, group, mode', [
    ('/etc/ld.so.conf.d/libmbus_lib.conf', 'root', 'root', 0o644),
])
def test_lib_path_file(File, name, user, group, mode):
    assert File(name).exists
    assert File(name).is_file
    assert File(name).user == user
    assert File(name).group == group
    assert File(name).mode == mode


# Binary files
@pytest.mark.parametrize('name', [
    ('mbus-serial-request-data'),
    ('mbus-serial-request-data-multi-reply'),
    ('mbus-serial-scan'),
    ('mbus-serial-scan-secondary'),
    ('mbus-serial-select-secondary'),
    ('mbus-serial-switch-baudrate'),
    ('mbus-tcp-application-reset'),
    ('mbus-tcp-raw-send'),
    ('mbus-tcp-request-data'),
    ('mbus-tcp-request-data-multi-reply'),
    ('mbus-tcp-scan'),
    ('mbus-tcp-scan-secondary'),
    ('mbus-tcp-select-secondary'),
])
def test_run_binary(Command, name):
    assert 'usage: {}'.format(name) in Command(name).stderr
