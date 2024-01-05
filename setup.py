from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="autofl",
    version="0.0.34",
    description="Federated Learning Package which includes all the variations of FL and can write new simulations",
    package_dir={"": "auto-fl/"},
    packages=find_packages(where="auto-fl/"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sujaykumarmag/auto-fl",
    author="SujayKumar Reddy M",
    author_email="sujaykumarreddy.m2020@vitstudent.ac.in",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)