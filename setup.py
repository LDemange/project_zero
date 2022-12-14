from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='project_zero',
      version="1.0",
      description="Project Description",
      packages=find_packages(),
      install_requires=requirements,
      include_package_data=True,
      #scripts=['scripts/project_zero-run'],
      zip_safe=False)
