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
    for v in ('3.10', '3.9', '3.8', '3.7', '3.6', '2.7'):
        f = host.file('/opt/Python-' + v + '/bin/python' + v)
        assert f.exists
        assert f.user == 'python'
        assert f.group == 'python'

        assert v in host.check_output('/opt/Python-' + v + '/bin/python' + v +
                                      ' --version 2>&1')
