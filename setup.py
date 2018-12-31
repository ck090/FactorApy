from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

def requirements():
    with open('requirements.txt') as r:
        reqs = r.read()
    reqs = reqs.split("\n")
    return reqs[:-1]

setup(
    name="factorapy",
    version="0.0.1",
    description="A Python package to for performing Factor analysis on any given data.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ck090/FactorApy",
    author="Chandra Kanth N",
    author_email="canfindck@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["src"],
    include_package_data=True,
    install_requires=requirements(),
    entry_points={
        "console_scripts": [
            "weather-reporter=weather_reporter.cli:main",
        ]
    },
)
