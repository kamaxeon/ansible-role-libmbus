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


# Binary files
@pytest.mark.parametrize('name', [
    ('/usr/local/bin/mbus-serial-request-data'),
    ('/usr/local/bin/mbus-serial-request-data-multi-reply'),
    ('/usr/local/bin/mbus-serial-scan'),
    ('/usr/local/bin/mbus-serial-scan-secondary'),
    ('/usr/local/bin/mbus-serial-select-secondary'),
    ('/usr/local/bin/mbus-serial-switch-baudrate'),
    ('/usr/local/bin/mbus-tcp-application-reset'),
    ('/usr/local/bin/mbus-tcp-raw-send'),
    ('/usr/local/bin/mbus-tcp-request-data'),
    ('/usr/local/bin/mbus-tcp-request-data-multi-reply'),
    ('/usr/local/bin/mbus-tcp-scan'),
    ('/usr/local/bin/mbus-tcp-scan-secondary'),
    ('/usr/local/bin/mbus-tcp-select-secondary'),
])
def test_binary_files(File, name):
    assert File(name).exists
    assert File(name).is_file
    assert File(name).user == 'root'
    assert File(name).mode == 0o755
# # Binary files
# @pytest.mark.parametrize('name', [
#     ('mbus-serial-request-data'),
#     ('mbus-serial-request-data-multi-reply'),
#     ('mbus-serial-scan'),
#     ('mbus-serial-scan-secondary'),
#     ('mbus-serial-select-secondary'),
#     ('mbus-serial-set-address'),
#     ('mbus-serial-switch-baudrate'),
#     ('mbus-tcp-application-reset'),
#     ('mbus-tcp-raw-send'),
#     ('mbus-tcp-request-data'),
#     ('mbus-tcp-request-data-multi-reply'),
#     ('mbus-tcp-scan'),
#     ('mbus-tcp-scan-secondary'),
#     ('mbus-tcp-select-secondary'),
# ])
# def test_run_binary(Command, name):
#     cmd = (Command(name))
#     assert 'mbus-serial' in cmd.stdout
