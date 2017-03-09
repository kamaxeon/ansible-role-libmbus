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
# def test_binary_files(File, name):
#     assert File(name).exists
#     assert File(name).is_file
#     assert File(name).user == 'root'
#     assert File(name).mode == 0o644
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
