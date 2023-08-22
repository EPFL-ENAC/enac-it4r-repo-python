Documentation
====================

The project documentation is built using Sphinx. All documentation lives
in the ``docs/`` directory of the project repository.

The documentation can written in markdown or reStructuredText.

Getting started to generate the documentation locally
-----------------------------------------------------

Set the python environment
~~~~~~~~~~~~~~~~~~~~~~~~~~

Sphinx should be installed within your python environment. Use the
virtual environment of the disdrodb project.

Generate the documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command to generate the doc :

::

   sphinx-build -b html docs/source docs/build

The output of the previous command should be checked for warnings and
errors. In case of any changes made to the code such as adding new
classes or functions, it is necessary to regenerate the API
documentation files before running the command mentioned above :

::

   sphinx-apidoc -f -o docs/source project_name
