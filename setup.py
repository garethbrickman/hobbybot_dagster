from setuptools import find_packages, setup

setup(
    name="hobbybot_dagster",
    packages=find_packages(exclude=["hobbybot_dagster_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-components",
    ],
    extras_require={"dev": ["dagster-webserver"]},
)