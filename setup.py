# type: ignore
"""Package deployment script."""

import setuptools

with open('README.md', encoding='utf-8') as readme:
    long_description = readme.read()

with open('requirements.txt', encoding='utf-8') as requirements:
    install_requires = requirements.read().splitlines()

setuptools.setup(
    name='qgis-stubs',
    version='0.2.0',
    url='https://github.com/leonhard-s/qgis-stubs',
    author='Leonhard S.',
    maintainer_email='leonhard-sei@outlook.com',
    description='PEP561 type stub files for the QGIS Python wrapper',
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
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development'
    ],
    install_requires=install_requires,
)
