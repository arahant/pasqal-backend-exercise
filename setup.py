import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="exercise",
    version="0.0.1",
    maintainer="Pasqal",
    maintainer_email="pcs@pasqal.io",
    description="Backend dev interview exercise",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["pytest"],
    python_requires=">=3.8.0",
)
