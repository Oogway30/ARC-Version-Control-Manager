from setuptools import setup

setup(
    name = "arc",
    version = "0.1.0",
    py_modules=["commands","repository","objects","temporary"],
    install_requires=[],
    entry_points={
        "console_scripts":[
            "arc=commands:main"
        ]
    }
)
