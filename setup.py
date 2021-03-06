#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path
import platform


def package_env(file_name, strict=False):
    file_path = path.join(path.dirname(__file__), file_name)
    if path.exists(file_path) or strict:
        return open(file_path).read()
    else:
        return ''

if __name__ == '__main__':
    required = ['comtypes', 'retrying==1.3.3']
    if platform.system() == 'Darwin':
        required.append('atomac')
    setup(
        name='uisoup-yandex',
        version='2.5.0',
        description='Cross Platform GUI Test Automation tool.',
        long_description=package_env('README.rst'),
        author='Max Beloborodko, Sergey Chipiga',
        author_email='f1ashhimself@gmail.com, svchipiga@yandex-team.ru',
        packages=['uisoup'] + ['.'.join(('uisoup', p)) for p in
                               find_packages('uisoup')],
        include_package_data=True,
        install_requires=required,
        zip_safe=False,
        entry_points={
            'console_scripts': [
                'ui-inspector = uisoup.ui_inspector:main'
            ]
        }
    )
