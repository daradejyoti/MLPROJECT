# to find the folders and create packages  use -find_packages
# setup = for creating setup for your project 
from setuptools import find_packages,setup

def get_requirements(file_path:str)->list[str]:
    requirements =[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements=[i.replace("/n",'') for i in requirements]
    
    return requirements





setup(
    name= "ml_project",
    version= '0.1.1',
    author= "j",
    author_email= 'daradejyoti21@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
  )