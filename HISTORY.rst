=======
History
=======

1.0 (2020-07-8)
------------------

* The first release of ``JSONManipulator``.


1.1 (2020-07-12)
------------------

* Added docstrings to the package and the ``examples`` directory.


2.0 (2020-07-12)
------------------

* Made more out-of-the-box functionality of the package.
* Minor optimization of the core module.


3.0 (2020-07-17)
------------------

* Added Pytests.
* Added documentation (using sphinx-documentation).
* Added Tox support.
* Tested code coverage - 92%.
* Enabled Travis CI.
* Resolved 1 bug with the deletion of one book.
* Optimized ``cap_sentence()``, making it non-static.
* Shortened the relevant lines of code by applying the knowledge of the copy function.
* Deployed ``__slots__``, saving RAM when using the package.


3.0.1 (2020-07-18)
------------------

* Created more tests which resulted in code coverage of 97.3%.
* Minor optimization of the core module.


3.0.2 (2020-07-20)
------------------

* Resolved date misprint in HISTORY.rst.
* Created more advanced structure for requirements.
* Made requirements for installations the package more rigorous.
* Deployed EditorConfig for better code consistency.
* Added Makefile in the root directory.
* Made use of the pyup bot (checks dependencies).


3.1 (2020-08-07)
------------------

* Used try/except in ``tests`` instead of ``sys.exit(0)`` in ``core`` module.
* The package is now easy-to-use in Python terminal (the programme will not be aborted).


3.1.1 (2020-09-04)
------------------

* Split ``core`` module to separate files, which resulted in a better readable code.
