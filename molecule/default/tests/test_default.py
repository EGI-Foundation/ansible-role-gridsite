import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_packages(host):
    p = host.package('httpd')
    assert p.is_installed


def test_http_config(host):
    http_conf_file = host.file('/etc/httpd/conf/httpd.conf')
    ssl_dir = host.file('/var/cache/mod_ssl')

    assert http_conf_file.exists
    assert http_conf_file.is_file
    assert http_conf_file.contains('GridSiteMethods	GET PUT DELETE MOVE')

    assert ssl_dir.is_directory