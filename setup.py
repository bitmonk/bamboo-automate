from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='bamboo_automate',
      version=version,
      description="atlassian bamboo rest api library in python",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Justin Alan Ryan',
      author_email='bitmonk@icloud.com',
      url='',
      license='Apache',
      packages=find_packages('src',),
      package_dir={'':'src'},
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'lxml',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
