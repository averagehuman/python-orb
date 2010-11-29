# -*- coding: utf-8 -*-

import os
from distutils.core import setup

__version__ = '0.7.1'
projectdir = os.path.dirname(os.path.abspath(__file__))

requires = []

setup(
    name="orb",
    version=__version__,
    description="pip/virtualenv shell script wrapper",
    author="Walter Wefft",
    author_email = "walter@wefft.com",
    classifiers=[
                "Intended Audience :: Developers",
                "Programming Language :: Python",
                ],
    requires=requires,
    url="https://wefft.codebasehq.com/lib/orb",
    license="BSD",
    download_url="http://pypi.python.org/packages/source/o/orb/orb-%s.tar.gz" % __version__,
    scripts=[
        os.path.join(projectdir, 'orb'),
        ]
)
    

