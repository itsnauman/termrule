from setuptools import setup

setup(
    name='termrule',
    version='0.13',
    py_modules=['termrule'],
    description='Coloured Horizontal Rule For Terminal',
    url='http://github.com/itsnauman/termrule',
    author='Nauman Ahmad',
    author_email='nauman-ahmad@outlook.com',
    license='MIT',
    include_package_data=True,
    packages=['tr'],
    install_requires=[
        'termcolor',
        'future',
    ],
    entry_points='''
        [console_scripts]
        rl=tr.termrule:main
    ''',
)
