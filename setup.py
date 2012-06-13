# -*- coding: utf-8 -*-
from distutils.core import setup

import bitbucket

setup(
  name='bitbucket',
  version=bitbucket.__version__,
  description='Bitbucket API',
  long_description=open('README').read(),
  author='Baptiste Millou',
  author_email='baptiste@smoothie-creative.com',
  url='https://github.com/Sheeprider/Py-BitBucket',
  packages=['bitbucket'],
  license=open('LICENSE').read(),
  # install_requires=open('requirements.txt').readlines(),
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: ISC License (ISCL)',
    'Programming Language :: Python',
    'Natural Language :: English',
  ],
)