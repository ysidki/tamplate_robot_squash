from setuptools import setup

setup(
    name='utest',
    version='0.1',
    py_modules=['cli'],  # Your CLI script file
    install_requires=[
        'click',  # Only if you use click
    ],
    entry_points={
        'console_scripts': [
            # or
            'utest=cli:cli',  # For `click`
        ],
    },
)