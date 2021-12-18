Ansible role: source-python
===========================

![build](https://github.com/nmusatti/source-python/actions/workflows/test.yml/badge.svg)

An Ansible role to download and install Python from source. Currently only Red Hat distributions are supported,
i.e. CentOS 7, CentOS 8 and Fedora.


Requirements
------------

None.

Role Variables
--------------

The variables that control the role behaviour are listed below with their respective defaults:

    python_install_dir: /opt

The base directory of the installation

    python_release: 3.9.0

The version of Python to be installed, in x.y.z form.

    python_user: python

The owner of the installation.

    python_group: python

The installation group.

    python_src_dir: /sw/python

The directory where the source archive is downloaded, extracted and built.

    python_force: false

When `true` installation is performed even if a bug fix release of the same minor version was already installed.
Useful to repeat installations after something went wrong or to perform upgrades. Note that setting `python_force`
to `true` breaks the role's idempotence.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: nmusatti.source_python
           vars:
             python_release: 3.9.0

Note the underscore in the name. Ansible Galaxy did not accept my submission otherwise.

License
-------

GPLv3

Author Information
------------------

Nicola Musatti - https://github.com/nmusatti
