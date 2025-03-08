import setuptools

 
setuptools.setup(
    name="ingestion",
    version="0.0.1",
    author="Sagar Lad",
    author_email="azuretutorials@gmail.com",
    description="Package to create data ingestion",
    long_description="sample description",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)