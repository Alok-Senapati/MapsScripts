from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='geom_converter',
    version='1.0',
    packages=['scripts'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'convert_geom = scripts.geom_converter:main',
        ],
    }
)
