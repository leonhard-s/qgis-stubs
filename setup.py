# type: ignore
"""Package deployment script."""

import setuptools

with open('README.md', encoding='utf-8') as readme:
    long_description = readme.read()

setuptools.setup(
    name='qgis-stubs',
    version='0.2.0',
    url='https://github.com/leonhard-s/qgis-stubs',
    author='Leonhard S.',
    maintainer_email='leonhard-sei@outlook.com',
    description='PEP561 type stubs for PyQGIS',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>= 3.6',
    package_data={
        'qgis-stubs': ['*.pyi'],
        'qgis-stubs.core': ['*.pyi'],
        'qgis-stubs.processing': ['*.pyi'],
    },
    packages=[
        'qgis-stubs',
        'qgis-stubs.core',
        'qgis-stubs.processing',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development'
    ],
    install_requires=[
        'PyQt5-stubs >= 5.14',
    ],
)
