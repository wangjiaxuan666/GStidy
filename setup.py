#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = [ ]

test_requirements = [ ]

setup(
    author="Wang jiaxuan",
    author_email='poormouse@126.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="the python Packages for the GWAS",
    entry_points={
        'console_scripts': [
            'gstidy=gstidy.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    package_data={"gstidy":["data/snp2maf.json","data/snp2chrpos.json","data/fake_table.GWAS.sumstats.tsv"]},
    keywords='gstidy',
    name='gstidy',
    packages=find_packages(include=['gstidy', 'gstidy.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/wangjiaxuan666/gstidy',
    version='0.1.0',
    zip_safe=False,
)
