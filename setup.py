#!/usr/bin/env python3
"""Setup script for easy3d package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="easy3d",
    version="0.1.1",
    author="Chen Wang",
    author_email="chwangthu@gmail.com",
    description="3D development made easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cwchenwang/easy3d",  # Update this with your actual repo
    project_urls={
        "Bug Reports": "https://github.com/cwchenwang/easy3d/issues",
        "Source": "https://github.com/cwchenwang/easy3d",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Graphics :: 3D Modeling",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
) 