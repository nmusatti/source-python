import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_python(host):
    f = host.file('/opt/Python-3.13/bin/python3.13')
    assert f.exists
    assert f.user == 'python'
    assert f.group == 'python'

    assert '3.13.0' in host.check_output(
        '/opt/Python-3.13/bin/python3.13 --version')
