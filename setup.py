# type: ignore
"""Package deployment script."""

import setuptools

with open('README.md') as readme:
    long_description = readme.read()


setuptools.setup(
    name="qgis-stubs",
    version='0.1.0',
    url="https://github.com/leonhard-s/qgis-stubs",
    author="Leonhard S.",
    maintainer_email="leonhard-sei@outlook.com",
    description="PEP561 stub files for the QGIS Python wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">= 3.6",
    package_data={"qgis-stubs": ['*.pyi']},
    packages=["qgis-stubs"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development"
    ]
)
