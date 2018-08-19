source_python
=============

Download and install Python from source.

Requirements
------------

None. This role installs all the required system packages.

Role Variables
--------------

python_version: the version of Python to be installed, in x.y.z form. The default is "3.7.0"
build_dir: the directory in which the Python source will be downloaded and build. The default is "/tmp"
install_dir: the base of the directory in which Python will be installed. The default is "/opt"
user: the user that will own the installation. The default is "python"
group: the installation owner's primary group. The default is "python"

Dependencies
------------

None.

Example Playbook
----------------

This role can be used as follows:

- name: install Python
  hosts: all
  tasks:
  - include_role:
       name: source_python
    vars:
      python_version: "3.7.0"

License
-------

GPLv3

Author Information
------------------

Nicola Musatti
nicola.musatti@gmail.com
