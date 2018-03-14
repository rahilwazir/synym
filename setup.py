from setuptools import setup

setup(
    name='synym',
    version='0.1',
    py_modules=['synym'],
    install_requires=[
        'Click',
        'thesaurus==0.1'
    ],
    dependency_links=[
        'https://github.com/rahilwazir/thesaurus-api/tarball/master#egg=thesaurus-0.1'
    ],
    entry_points='''
        [console_scripts]
        synym=synym:cli
    ''',
)
