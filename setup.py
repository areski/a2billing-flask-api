#
# SMS-Khomp-API License
# http://www.star2billing.com
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from setuptools import setup, find_packages
from setuptools.dist import Distribution
import pkg_resources
import sys

VERSION = '1.0'

install_flag=False

if sys.argv[1] == "install":
    install_flag = True

setup(
    name='sms-khomp-api',
    version=VERSION.replace(' ', '-'),
    description='HTTP API for Khomp SMS',
    long_description=open('README.rst').read(),
    author='Belaid Arezqui',
    author_email='areski@gmail.com',
    url='http://www.cdr-stats.org/',
    download_url='https://github.com/areski/sms-khomp-api',
    packages=find_packages(),
    include_package_data=True,
    license='MPL 2.0 License',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers, Users',
        'License :: OSI Approved :: MPL 2.0 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python, Javascript, HTML',
        'Topic :: Call Analytic Software'
    ],
    zip_safe=False,
    setup_requires=[
        "Flask == 0.8",
        "gevent == 0.13.7",
    ],
)
