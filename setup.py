# -*- coding: utf-8 -*-

import os
from distutils.core import setup

__version__ = '0.8'
projectdir = os.path.dirname(os.path.abspath(__file__))
readme = open("README").read()


setup(
    name="orb",
    version=__version__,
    description="pip/virtualenv shell script wrapper",
    long_description=readme,
    author="Djord Flanagan",
    author_email = "contact@devopsni.com",
    classifiers=[
                "Intended Audience :: Developers",
                "Programming Language :: Python",
                ],
    url="https://github.com/podados/python-orb",
    license="BSD",
    download_url="http://pypi.python.org/packages/source/o/orb/orb-%s.tar.gz" % __version__,
    scripts=[
        os.path.join(projectdir, 'orb'),
    ]
)
    

