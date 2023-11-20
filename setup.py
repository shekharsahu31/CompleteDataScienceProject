from setuptools import find_packages,setup
from typing import List

## HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
name='CompleteDataScienceProject',
version='0.0.1',
author='Shekhar Sahu',
author_email='shekharthe07@gmail.com',
packages=find_packages(), #it finds all packages in the project , find all folders having init file init, 
                         #it will treat it as a sub-package/ module to our main package.
install_requires=get_requirements('req.txt') #### = ['numpy','pandas'] instead giving list we are making a function to read req.txt and return a 
                                             #### a list + it ignores -e . which is in req.txt to make package as we do not want it in install
                                             ### requirements
)