===========
fdr
===========


.. image:: https://img.shields.io/pypi/v/fdr.svg
        :target: https://pypi.python.org/pypi/fdr

.. image:: https://img.shields.io/travis/jonathanchukinas/fdr.svg
        :target: https://travis-ci.org/jonathanchukinas/fdr

.. image:: https://readthedocs.org/projects/fdr/badge/?version=latest
        :target: https://fdr.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Validate a Function & Design Requirements document.

* Free software: MIT license
* Documentation: https://fdr.readthedocs.io.


Quick Start
------------

J&J Quick Start
''''''''''''''''''''''
1. **Install Python**
    a. Navigate to J&J App Store. You may need to use Internet Explorer. Users have had difficulty with Chrome.
    #. Search ``Python``. You should see something similar to ``Python 3.6``. Add it to cart and install.
    #. No restart is required.
#. **Run Command Prompt with Elevated Privileges**
    a. Do not call IRIS.
    #. Hit the ``Windows Key`` and type ``cmd`` to search for the Windows command prompt
    #. Right-click ``cmd`` and select ``open file location``. This opens File Explorer.
    #. Right-click on the ``cmd`` icon and select ``Run with elevated privileges``.
#. **Install** ``fdr``
    a. In Command Prompt, type ``pip install fdr``
    #. If this throws an error, try instead: ``python -m pip install fdr``. Hint: the up-arrow accesses previous commands to reduce the amount of typing you need to do.
    #. Note: You might see a note about ``pip`` being out of date. This is ok, but feel free to update it as suggested.
#. **Run** ``fdr``
    a. In Command Prompt, type ``fdr``

Validation Rules
-----------------
General Notes
'''''''''''''
- The FDR sheet must have the title 'Procedure Based Requirements'
- If multiples headers share the same name, only the first will be used.