Ansible role: source-python
===========================

[![Build Status](https://travis-ci.org/nmusatti/source-python.svg?branch=master)](https://travis-ci.org/nmusatti/source-python)

An Ansible role to download and install Python from source. Currently only CentOS 7 is supported.


Requirements
------------

None.

Role Variables
--------------

The variables that control the role behaviour are listed below with their respective defaults:

    python_install_dir: /opt

The base directory of the installation

    python_release: 3.7.1

The version of Python to be installed, in x.y.z form.

    python_user: python

The owner of the installation.

    python_group: python

The installation group.

    python_src_dir: /sw/python

The directory where the source archive is downloaded, extracted and built.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: nmusatti.source-python
           vars:
             python_release: 3.7.1

License
-------

GPLv3

Author Information
------------------

Nicola Musatti - https://github.com/nmusatti
