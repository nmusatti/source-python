Ansible role: source-python
===========================

![test](https://github.com/nmusatti/source-python/actions/workflows/test.yml/badge.svg)

An Ansible role to download and install Python from source. Supported
distributions are the currently maintained releases of the Red Hat family and
derivatives, and Ubuntu LTS. At this time tests are run on Rocky Linux 9, 
CentOS Stream 10, CentOS Stream 9, Fedora 41, Fedora 40, Fedora 39,
Ubuntu 24.04, Ubuntu 22.04 and Ubuntu 20.04.


Requirements
------------

None.

Role Variables
--------------

The variables that control the role behaviour are listed below with their respective defaults:

    python_install_dir: /opt

The base directory of the installation

    python_release: 3.13.0

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
             python_release: 3.13.0

Note the underscore in the name.

License
-------

GPLv3

Author Information
------------------

Nicola Musatti - https://github.com/nmusatti
