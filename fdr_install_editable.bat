python -m pip uninstall fdr
python setup.py sdist bdist_wheel
python -m pip install -e .