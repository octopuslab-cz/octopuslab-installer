import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="micropython-octopuslab-installer",
    version="0.0.3",
    author="Vašek Chalupníček",
    author_email="",
    description="OctopusLab installer for MicroPython",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/octopusengine/octopuslab-installer",
    packages=setuptools.find_packages(),
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    # TODO dependency shutil
    python_requires='>=3.6',
)
