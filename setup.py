from setuptools import find_packages, setup
from typing import List 

HYPEN_E_DOT = '-e .'
def get_requirements(path : str) -> List[str]:
    
    requirements = []
    with open(path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = 'ml package',
    version = '0.0.1',
    author = 'Ivan Klimcak',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
