from setuptools import setup, find_packages

setup(
    name="treasure_hunter",
    version="0.1.0",
    packages = find_packages(exclude=['test']),
    install_requires = ['argparse', 'copy', 'random']
)
