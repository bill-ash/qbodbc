from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='qbodbc', 
    version='0.0.1', 
    author='William Ash', 
    author_email='bill@cloud9smart.com', 
    description='QuickBooks Library', 
    long_description=long_description, 
    long_description_content_type='text/markdown', 
    url='https://github.com/bill-ash/qbodbc', 
    packages=find_packages(), 
    python_requires='>=3.6'
    )


