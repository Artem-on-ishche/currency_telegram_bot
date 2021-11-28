from setuptools import find_packages, setup

setup(
    name='currency_telegram_bot',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
