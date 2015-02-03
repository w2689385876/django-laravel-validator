from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='django-laravel-validator',
      version=version,
      description="a form validator for django inspired of validator of laravel framework",
      long_description="""\
      a form validator for django inspired of validator of laravel framework
      easy to use easy to validate every thing.
      """,
      classifiers=[],
      keywords='',
      author='younger shen',
      author_email='younger.x.shen@gmail.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
