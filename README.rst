================================================================================
moban-handlebars
================================================================================

.. image:: https://api.travis-ci.org/moremoban/moban-handlebars.svg
   :target: http://travis-ci.org/moremoban/moban-handlebars

.. image:: https://codecov.io/github/moremoban/moban-handlebars/coverage.png
   :target: https://codecov.io/github/moremoban/moban-handlebars
.. image:: https://badge.fury.io/py/moban-handlebars.svg
   :target: https://pypi.org/project/moban-handlebars

.. image:: https://pepy.tech/badge/moban-handlebars/month
   :target: https://pepy.tech/project/moban-handlebars/month

.. image:: https://img.shields.io/github/stars/moremoban/moban-handlebars.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/moremoban/moban-handlebars/stargazers


With `pybars3 <https://github.com/wbond/pybars3>`_, this library allow moban users to
have handlebars template in their next documentation endeavour.

Quick start
============


.. code-block:: bash

   $ moban "<p>{{firstname}} {{lastname}}</p>" -d firstname=hello lastname=world

Nested input objects
---------------------

Given a data.json file with the following content

.. code-block::

    {
      "person": {
        "firstname": "Yehuda",
        "lastname": "Katz",
      },
    }


.. code-block:: bash


   $ moban -c data.json  "{{person.firstname}} {{person.lastname}}"
   Templating {{person.f... to moban.output
   Templated 1 file.
   $ cat moban.output
   Yehuda Katz

For `handlebars.js` users, yes, the example was copied from handlebarjs.com. The
aim is to show off what we can do.

Let's continue with a bit more fancy feature:



.. code-block:: bash

   $ moban -c data.json "{{#with person}}{{firstname}} {{lastname}} {{/with}}"



Installation
================================================================================


You can install moban-handlebars via pip:

.. code-block:: bash

    $ pip install moban-handlebars


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/moban-handlebars.git
    $ cd moban-handlebars
    $ python setup.py install
