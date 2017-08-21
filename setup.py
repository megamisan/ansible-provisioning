#!/usr/bin/env python

import os
import sys
from glob import glob

sys.path.insert(0, os.path.abspath('lib'))
from ansible import __version__, __author__
from distutils.core import setup

# find library modules
data_files = [ ('/usr/share/ansible', glob('./library/*')) ]

print "DATA FILES=%s" % data_files

setup(name='ansible-provisioning',
      version=open('./VERSION').read(1000),
      description='Minimal SSH command and control',
      author=__author__,
      author_email=__author_email__,
      url='http://github.com/megamisan/ansible-provisioning',
      license='GPLv3',
#      install_requires=['ansible'],
      package_dir={ 'ansible': 'lib/ansible' },
#      packages=[
#         'ansible.runner.action_plugins',
#      ],
      data_files=data_files
)
