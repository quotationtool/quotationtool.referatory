# -*- coding: utf-8 -*-
"""Setup for quotationtool.referatory package

$Id$
"""
from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

name='quotationtool.referatory'

setup(
    name = name,
    version='0.1.0',
    description="Referatory related components for the quotationtool application",
    long_description=(
        read('README')
        + '\n' +
        'Detailed Documentation\n'
        '**********************\n'
        + '\n' +
        read('src', 'quotationtool', 'referatory', 'README.txt')
        + '\n' +
        'Download\n'
        '********\n'
        ),
    keywords='quotationtool, blue bream',
    author=u"Christian Luck",
    author_email='cluecksbox@googlemail.com',
    url='',
    license='ZPL 2.1',
    # Get more from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Programming Language :: Python',
                 'Environment :: Web Environment',
                 'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                 'Framework :: Zope3',
                 ],
    packages = find_packages('src'),
    namespace_packages = ['quotationtool',],
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires = [
        'setuptools',
        'ZODB3',
        'zope.interface',
        'zope.schema',
        'zope.component',
        'zope.container',
        'zope.catalog',
        'zc.catalog',
        'zc.relation',
        'zope.i18nmessageid',
        'zope.security',
        'zope.securitypolicy',
        'zope.annotation',
        'zope.dublincore',
        'zope.app.schema',
        'zope.app.content',
        'z3c.i18n',
        
        'quotationtool.security',
        'quotationtool.relation',
        'quotationtool.site',
        ],
    extras_require = dict(
        test = [
            'zope.testing',
            'zope.configuration',
            ],
        ),
    )
