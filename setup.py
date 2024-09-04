from setuptools import setup, find_packages

setup(
    name="voice_api",
    version="1.1.0",
    author="Chichieh Huang",
    author_email="cch.chichieh@gmail.com",
    description="A Python wrapper for the Voice API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wsxqaza12/voice_api",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
        "pydub==0.25.1",
    ],
)