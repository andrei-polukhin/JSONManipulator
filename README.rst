JSONManipulator
===============

.. image:: https://api.codacy.com/project/badge/Grade/eca03080aafd456e8321e3d7909d2458
   :alt: Codacy Badge
   :target: https://app.codacy.com/gh/pandrey2003/JSONManipulator?utm_source=github.com&utm_medium=referral&utm_content=pandrey2003/JSONManipulator&utm_campaign=Badge_Grade
.. image:: https://travis-ci.com/pandrey2003/JSONManipulator.svg?branch=master
    :target: https://travis-ci.com/pandrey2003/JSONManipulator
.. image:: https://coveralls.io/repos/github/pandrey2003/JSONManipulator/badge.svg?branch=master
    :target: https://coveralls.io/github/pandrey2003/JSONManipulator?branch=master
    :alt: Coveralls
.. image:: https://www.codefactor.io/repository/github/pandrey2003/jsonmanipulator/badge
    :target: https://www.codefactor.io/repository/github/pandrey2003/jsonmanipulator
    :alt: CodeFactor
.. image:: https://pyup.io/repos/github/pandrey2003/JSONManipulator/shield.svg
    :target: https://pyup.io/repos/github/pandrey2003/JSONManipulator/
    :alt: Updates
.. image:: https://pyup.io/repos/github/pandrey2003/JSONManipulator/python-3-shield.svg
    :target: https://pyup.io/repos/github/pandrey2003/JSONManipulator/
    :alt: Python 3
.. image:: https://readthedocs.org/projects/jsonmanipulator/badge/?version=latest
    :target: https://jsonmanipulator.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://pepy.tech/badge/jsonmanipulator
    :target: https://pepy.tech/project/jsonmanipulator


JSONManipulator is a Python package to retrieve, add, delete, change and store objects in JSON files.

Installation
------------

Use the package manager `pip <https://pip.pypa.io/en/stable/>`_ to install JSONManipulator.

.. code-block:: bash

   pip install JSONManipulator

Usage
-----

Firstly, you need to set up your initial JSON file.

.. code-block:: python

   from JSONManipulator import set_up

   set_up(
       full_path="enter/full/path/to/your/file/here"
   )

Functionality
-------------

As soon as you set up your file, you can use classes of the package:

#. **GetInformation** (retrieve information about particular objects in the file).
#. **ChangeValue** (change values of particular objects in the file).
#. **ChangeAllValues** (change values of all objects in the file).
#. **DeleteObject** (delete particular objects in the file).
#. **AddObject** (add a new object to the file).
#. **AddKey** (add a new key to each object in the file).

More detailed information about the usage of the package can be found in the ``examples`` and ``docs`` folders.

Contributing
------------

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
-------

`MIT <https://choosealicense.com/licenses/mit/>`_
