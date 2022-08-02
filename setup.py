import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="micropython-octopuslab-installer",
    version="0.2.4",
    author="OctopusLAB",
    author_email="info@octopuslab.cz",
    description="OctopusLab installer for MicroPython",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/octopusengine/octopuslab-installer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    install_requires=[
        'shutil',
    ],
    python_requires='>=3.6',
)
