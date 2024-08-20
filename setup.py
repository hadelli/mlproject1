from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

#this function will return a list. it will accept a file path that is a string
def get_requirements(file_path:str)->List[str]:
    '''
    This fucntion will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        #readding each line from that .txt file. but we need to replace \n with blank
        requirements = file_obj.readlines()
        #replacing \n by usiong in-built function 'replace'
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Haryanka',
    author_email = 'haryanka1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)