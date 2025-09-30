from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.readlines()
    
setup(
    name="multi_ai_agents",
    version="0.1.0",
    author="Vijay Kumar Reddy Bommireddy",
    packages=find_packages(),
    install_requires=requirements,
)