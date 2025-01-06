from setuptools import find_packages ,setup
from typing import List
HYPEN_E_DOT = '-e.'

def get_requirements(filepath : str) ->List[str]:
    requirements =[]
    with open(filepath) as file_Obj:
        requirements = file_Obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

    if(HYPEN_E_DOT) in requirements :
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='DemoProject1989',
    version='0.0.1',
    author='bbkingwarrio1989',
    author_email='bchander21@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)
