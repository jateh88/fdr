import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rtm",
    description="Validate Requirements Trace Matrix.",
    long_description=long_description,
    version="0.1.8",
    author='Jonathan Chukinas',
    author_email='chukinas@gmail.com',
    url='https://github.com/jonathanchukinas/fdr',
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["click", "openpyxl"],
    entry_points="""
        [console_scripts]
        rtm=rtm.cli:rtm_cli
    """,
)

# PyPA tutorial: https://packaging.python.org/tutorials/packaging-projects/
# To distribute the next version:
#   Build the sdist and wheel:
#       python setup.py sdist bdist_wheel
#   Upload to PyPI:
#       twine upload dist/*
