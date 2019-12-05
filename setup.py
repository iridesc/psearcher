import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="psearcher",
    version="0.2",
    author="Irid Zhang",
    author_email="irid.zzy@gmail.com",
    description="psearcher is a web search interface for python3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iridesc/psearcher",
    packages=setuptools.find_packages(),
    install_requires=['bs4>=0.0.1', 'requests>=2.0.0','retry>=0.8.0','loger>=0.1.0'],
    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)