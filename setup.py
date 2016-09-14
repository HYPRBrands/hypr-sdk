import os
import re
import sys
from codecs import open

from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'sdk'
]

requires = ['requests>=2.11.1']
test_requirements = ['nose', 'requests', 'responses', 'mock']

with open('sdk/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='hypr-sdk',
    version=version,
    description='SDK for HYPR\'s API.',
    long_description=readme + '\n\n' + history,
    author='Daniel Dubovski',
    author_email='daniel@hyprbrands.com',
    url='http://developers.hyprbrands.com',
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    license='Proprietary',
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Proprietary',
        'Programming Language :: Python :: 2.7',
    ),
    test_suite='nose.collector',
    tests_require=test_requirements,
    extras_require={
    },
)
