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

   $ moban "<p>{{firstname}} {{lastname}}</p>" --template-type handlebars -d firstname=hello lastname=world

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


   $ moban --template-type handlebars -c data.json  "{{person.firstname}} {{person.lastname}}"
   Handlebars-ing <p>{{first... to moban.output
   Handlebarsed 1 file.
   $ cat moban.output
   Yehuda Katz

For `handlebars.js` users, yes, the example was copied from handlebarjs.com. The
aim is to show off what we can do.

Let's continue with a bit more fancy feature:



.. code-block:: bash

   $ moban --template-type handlebars -c data.json "{{#with person}}{{firstname}} {{lastname}} {{/with}}"


Moban way of `pybar3 usage <https://github.com/wbond/pybars3#usage>`_:

Let's save the following file a `script.py` under `helper_and_partial` folder:

.. code-block:: python

   from moban_handlebars.helpers import HandlebarHelper
   from moban_handlebars.partials import register_partial

   register_partial('header', '<h1>People</h1>')


   @HandlebarHelper('list')
   def _list(this, options, items):
       result = [u'<ul>']
       for thing in items:
           result.append(u'<li>')
           result.extend(options['fn'](thing))
           result.append(u'</li>')
       result.append(u'</ul>')
       return result


Let invoke handlebar template:


.. code-block: bash

   $ moban --template-type hbs -pd helper_and_partial -c data.json "{{>header}}{{#list people}}{{name}} {{age}}{{/list}}"
   Handlebars-ing {{>header}... to moban.output
   Handlebarsed 1 file.
   $ cat moban.output
   <h1>People</h1><ul><li>Bill 100</li><li>Bob 90</li><li>Mark 25</li></ul>



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
