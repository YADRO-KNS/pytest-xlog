from io import open

from setuptools import setup, find_packages

setup(
    name="pytest-xlog",
    version='0.1.4',
    license="MIT",
    description="Extended loggind for test and decorators",
    entry_points={"pytest11": ["pytest_xlog = pytest_xlog.plugin"]},
    author="Sergey Kozlov",
    author_email="s.kozlov@yardo.com",
    url="https://github.com/YADRO-KNS/pytest-xlog",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    platforms="any",
    python_requires=">=3.6",
    install_requires=["pytest>=5.2", "pyyaml>=5.1"],
    long_description="Pytest xlog plugin reporting test results to YAML file",
    keywords="pytest yaml decorator log",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Testing",
    ],
)
