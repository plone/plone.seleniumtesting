from setuptools import setup, find_packages
import os

version = '4.2a1'

setup(name='plone.seleniumtesting',
      version=version,
      description="Selenium Testing infrastructure for Plone projects.",
      long_description=open("README.txt").read() + "\n\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        ],
      keywords='plone zope testing',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.seleniumtesting',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'unittest2',
          'plone.app.testing',
          'selenium',
      ],
      extras_require={
          'test': [
                  'plone.testing',
              ]
      },
      )
