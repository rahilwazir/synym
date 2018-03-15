from setuptools import setup

setup(
    name='synym',
    version='0.1',
    description='CLI tool to list synonyms for a word from thesaurus.com',
    author='Rahil Wazir',
    author_email='rahilwazirali@gmail.com',
    url='https://github.com/rahilwazir/synym',
    py_modules=['synym'],
    install_requires=[
        'Click',
        'thesaurus==0.1'
    ],
    dependency_links=[
        'https://github.com/rahilwazir/thesaurus-api/tarball/master#egg=thesaurus-0.1'
    ],
    download_url='https://github.com/rahilwazir/synym/archive/0.1.tar.gz',
    entry_points='''
        [console_scripts]
        synym=synym:cli
    ''',
)
