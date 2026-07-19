from setuptools import setup

setup(
    name='GIT',
    py_modules=['commands'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        Hello=helloworld:sayHello
    ''',
)