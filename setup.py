"""
basic setup script
"""

from setuptools import setup

setup(
        name='multiDBApp',
        packages=['multidbapp'],
        include_package_data=True,
        install_requires=[
            'Flask',
            'Flask-Session',
            'mysqlclient',
            'psycopg2',
            'SQLAlchemy',
            'Flask-SQLAlchemy',
            'libsass',
        ],
)
