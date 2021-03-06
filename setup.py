# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages

from codecs import open  # To use a consistent encoding


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames),
                encoding='utf-8').read()


setup(
    name='pyramid_marrowmailer',
    version='0.4',
    description='Pyramid integration package for marrow.mailer,'
                ' formerly known as TurboMail',
    long_description=read('README.rst') + read('HISTORY.rst'),
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
    ],
    keywords='web wsgi pylons pyramid',
    author='',
    author_email='domen@dev.si',
    url='https://github.com/iElectric/pyramid_marrowmailer',
    license='BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.7',
    install_requires=[
        'pyramid>=1.10',
        'pyramid_tm>=2.4',
        'marrow.mailer>=4.0',
        'setuptools',
        'transaction>=3.0',
    ],
    extras_require={
        'test': [
            'nose',
            'coverage',
            'setuptools-flakes',
            'pep8',
        ],
    },
    entry_points="""
      """,
    include_package_data=True,
    zip_safe=False,
)
