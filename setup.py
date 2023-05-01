import os
from setuptools import setup, find_packages
from pkg_resources import parse_requirements

module_name = 'marketparser'

def load_requirements(filename: str) -> list:
    requirements = []
    with open (filename, 'r') as f:
        for req in parse_requirements(f.read()):
            requirements.append(
                '{}{}'.format(req.name, req.specifier)
            )
        return requirements
    
setup(
    name=module_name,
    version='0.1.0',
    description='Rest-api app description',
    packages=find_packages(),
    install_requires=load_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            '{0}-api = {0}.api.__main__:main'.format(module_name),
            '{0}-db = {0}.db.__main__:main'.format(module_name)
        ]
    },
    include_package_data=True
)