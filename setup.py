from setuptools import find_packages, setup
package_name = 'code_template'

# Read in the requirements.txt file
with open(f'{package_name}/requirements.txt') as f:
    requirements = f.read().splitlines()
    
setup(
	name=package_name,
    version="1.0",
	packages=find_packages(),
    install_requires=requirements,
)