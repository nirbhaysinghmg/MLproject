from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Read the requirements from a file and return a list of requirements.
    """
    HYPHEN_E_DOT = '-e .'
    requirements = []
    
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace("\n","") for req in requirements]  # Use strip() to remove all leading/trailing whitespace

            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. No requirements loaded.")
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Nirbhay Pratap Singh',
    author_email='nirbhaysinghfr@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
