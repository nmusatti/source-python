import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/opt/Python-3.7/bin/python3.7')

    assert f.exists
    assert f.user == 'python'
    assert f.group == 'python'
