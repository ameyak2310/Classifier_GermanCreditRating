from setuptools import setup,find_packages
from typing import List

# Declaring Variables for Project
PROJECT_NAME = "German_Credit_Classifier"
VERSION = '0.0.1'
AUTHOR = 'Ameya Kulkarni'
DESCRIPTION = "Housing price prediction"
PACKAGES = ['project_hppp']
REQUIRMENTS_FILE_NAME = 'requirments.txt'
HYPHEN_E_DOT = "-e ."

def get_requirments_list()->List[str]:
    """
    Description: Return list of requirments
    """
    with open(REQUIRMENTS_FILE_NAME) as requirment_file:
        return requirment_file.readlines()

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirments_list(),
    )