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
      classifiers=['Development Status :: 1 - Planning',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 2.7',
                   ],
      keywords='form validator, django, django-laravel-validator',
      author='younger shen',
      author_email='younger.x.shen@gmail.com',
      url='https://github.com/youngershen/django-laravel-validator',
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
