from setuptools import setup, find_packages
from pathlib import Path

BASE_DIR = Path(__file__).absolute()

with open(BASE_DIR / "README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='qbodbc', 
    version='0.0.1', 
    author='William Ash', 
    author_email='bill@cloud9smart.com', 
    description='QuickBooks Desktop Library', 
    long_description=long_description, 
    long_description_content_type='text/markdown', 
    license='MIT',
    url='https://github.com/bill-ash/qbodbc', 
    packages=find_packages(), 
    python_requires='>=3.6', 
     classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires = [
        'pandas',
        'pyodbc' 
    ],
    # test_suite='tests', 
    # tests_require=[]
    )


