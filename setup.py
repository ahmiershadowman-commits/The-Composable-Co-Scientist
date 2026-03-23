from setuptools import setup, find_packages

setup(
    name="compositional-co-scientist",
    version="1.0.0",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "sentence-transformers>=2.2.0",
        "pydantic>=2.0",
    ],
    extras_require={
        "test": ["pytest>=7.0", "pytest-cov>=4.0"],
    },
)
