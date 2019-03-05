import os
from setuptools import setup, find_packages

setup(
    name='i2c-snap',
    version='1.0',
    description='i2c lm75 snap',
    author_email=' ' ,
    url=' ',
    packages=['mqtt-broker'],
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    install_requires=[
        'pycryptodomex>=3.3',
        'requests>=2.4',
        'six>=1.10',
	'pubnub>=4.1.2',
	'smbus2>=0.2.1'
    ],
    zip_safe=True,
    scripts=['mqtt-broker/mqtt.py']
)
