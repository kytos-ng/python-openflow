"""Setup script.

Run "python3 setup --help-commands" to list all available commands and their
descriptions.
"""
import sys
from abc import abstractmethod
# Disabling checks due to https://github.com/PyCQA/pylint/issues/73
# pylint: disable=import-error,no-name-in-module,unspecified-encoding
# pylint: disable=consider-using-with
# pylint: enable=import-error,no-name-in-module
from subprocess import CalledProcessError, call, check_call

from setuptools import Command, find_packages, setup

from pyof import __version__


class SimpleCommand(Command):
    """Make Command implementation simpler."""

    user_options = []

    def __init__(self, *args, **kwargs):
        """Store arguments so it's possible to call other commands later."""
        super().__init__(*args, **kwargs)
        self.__args = args
        self.__kwargs = kwargs

    @abstractmethod
    def run(self):
        """Run when command is invoked.

        Use *call* instead of *check_call* to ignore failures.
        """

    def run_command(self, command):
        """Run another command with same __init__ arguments."""
        command(*self.__args, **self.__kwargs).run()

    def initialize_options(self):
        """Set default values for options."""

    def finalize_options(self):
        """Post-process options."""


# pylint: disable=attribute-defined-outside-init, abstract-method
class TestCommand(Command):
    """Test tags decorators."""

    user_options = [
        ("k=", None, "Specify a pytest -k expression."),
    ]

    def get_args(self):
        """Return args to be used in test command."""
        if self.k:
            return f"-k '{self.k}'"
        return ""

    def initialize_options(self):
        """Set default size and type args."""
        self.k = ""

    def finalize_options(self):
        """Post-process."""
        pass


class Cleaner(SimpleCommand):
    """Custom clean command to tidy up the project root."""

    description = 'clean build, dist, pyc and egg from package and docs'

    def run(self):
        """Clean build, dist, pyc and egg from package and docs."""
        call('make clean', shell=True)


class Test(TestCommand):
    """Run all tests."""

    description = "run tests and display results"

    def run(self):
        """Run tests."""
        cmd = f"python3 -m pytest tests/ {self.get_args()}"
        try:
            check_call(cmd, shell=True)
        except CalledProcessError as exc:
            print(exc)
            print('Unit tests failed. Fix the errors above and try again.')
            sys.exit(-1)


class TestCoverage(Test):
    """Display test coverage."""

    description = "run tests and display code coverage"

    def run(self):
        """Run tests quietly and display coverage report."""
        cmd = f"python3 -m pytest --cov=. tests/ {self.get_args()}"
        try:
            check_call(cmd, shell=True)
        except CalledProcessError as exc:
            print(exc)
            print('Coverage tests failed. Fix the errors above and try again.')
            sys.exit(-1)


class DocTest(SimpleCommand):
    """Run documentation tests."""

    description = 'run documentation tests'

    def run(self):
        """Run doctests using Sphinx Makefile."""
        cmd = 'make -C docs/ default doctest'
        check_call(cmd, shell=True)


class Linter(SimpleCommand):
    """Lint Python source code."""

    description = 'Lint Python source code'

    def run(self):
        """Run yala."""
        print('Yala is running. It may take several seconds...')
        try:
            check_call('yala pyof setup.py', shell=True)
            print('No linter error found.')
        except CalledProcessError:
            print('Linter check failed. Fix the error(s) above and try again.')
            sys.exit(-1)


setup(name='python-openflow',
      version=__version__,
      description='Library to parse and generate OpenFlow messages',
      long_description=open("README.rst", "r").read(),
      url='http://github.com/kytos/python-openflow',
      author='Kytos Team',
      author_email='devel@lists.kytos.io',
      license='MIT',
      test_suite='tests',
      include_package_data=True,
      extras_require={'dev': [
          'pip-tools >= 2.0',
          'pytest==8.0.1',
          'pytest-cov==4.1.0',
          'pytest-asyncio==0.23.5',
          'black==24.2.0',
          'isort==5.13.2',
          'pylint==3.1.0',
          'pycodestyle==2.11.1',
          'yala==3.2.0',
          'tox==4.13.0',
          'virtualenv==20.25.1',
      ]},
      packages=find_packages(exclude=['tests']),
      cmdclass={
          'clean': Cleaner,
          'coverage': TestCoverage,
          'doctest': DocTest,
          'lint': Linter,
          'test': Test
      },
      zip_safe=False,
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.11',
          'Topic :: System :: Networking',
          'Topic :: Software Development :: Libraries'
      ])
