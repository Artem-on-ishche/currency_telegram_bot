from setuptools import find_packages, setup

setup(
    name='enrolment_test',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
