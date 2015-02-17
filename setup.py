from setuptools import setup


REQUIREMENTS = [
    'requests'
]


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    ]

setup(name='he-sdk-python',
      version='0.3',
      description='Python client for HackerEarth Code Checker API v3',
      url='https://github.com/HackerEarth/he-sdk-python',
      author='Praveen Kumar',
      author_email='praveen@hackerearth.com',
      license='MIT',
      packages=['hackerearth'],
      classifiers=CLASSIFIERS,
      keywords='hackerarth code cheker api python client'
      )
