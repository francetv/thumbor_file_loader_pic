#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license

from distutils.core import setup

setup(
    name = "thumbor_file_loader_pic",
    packages = ["thumbor_file_loader_pic"],
    version = "1.0.1",
    description = "file loader",
    author = "Bertrand Thill",
    author_email = "bertrand.thill@francetv.fr",
    keywords = ["thumbor", "fallback", "images", "nfs"],
    license = 'MIT',
    url = 'https://github.com/francetv/thumbor_file_loader_pic',
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Multimedia :: Graphics :: Presentation'
    ],
    package_dir = {"thumbor_file_loader_pic": "thumbor_file_loader_pic"},
    install_requires=['thumbor>=6.5.0'],
    long_description = """\
This module test support for file.
"""
)
