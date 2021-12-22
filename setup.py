from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='nmigen-tool',
    version='0.0.1',
    author="Hans Baier",
    author_email="hansfbaier@gmail.com",
    description="nmigen command line tool for generating verilog, rtlil, cxxrtl and showing design diagrams",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license_files = ('LICENSE.txt',),
    platforms='linux',
    url="https://github.com/hansfbaier/nmigen-tool/",
    project_urls={
        "Bug Tracker": "https://github.com/hansfbaier/nmigen-tool/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        nmigen=nmigen_tool:cli
    ''',
)