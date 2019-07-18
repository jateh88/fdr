
:: Eric, the easiest way to install fdr to your computer is by running this batch file
:: You should be able to do this right in PyCharm by right-clicking the file and selecting "Run cmd script".
:: To see if the package is working, type `fdr` into the command line.
:: It shouldn't throw any errors if I've done it right...

python -m pip uninstall fdr
python setup.py sdist bdist_wheel
python -m pip install -e %HOMEPATH%\projects\fdr
python
import fdr
import fdr.fields as f