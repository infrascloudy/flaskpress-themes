import os, sys
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

__version__ = '0.1.5'
__author__ = 'InfrasCloudy, @allanice001'
__email__ = 'support@linaccess.za.net'


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    if sys.version_info.major != 3:
        with open(fpath(fname), 'rb') as f:
            return f.read()
    else:
        with open(fpath(fname)) as f:
            return f.read()


def desc():
    return read('README.rst')


setup(
    name="flaskpress-themes",
    version=__version__,
    url='https://github.com/infrascloudy/flaskpress-themes',
    license='MIT',
    author=__author__,
    author_email=__email__,
    description='Provides infrastructure for theming FlaskPress applications',
    keywords="flask themes theming style",
    long_description=desc(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=["Flask>=0.6", "simplejson"],
    tests_require=["nose"],
    test_suite="nose.collector",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)