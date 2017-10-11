***********
Async Actor
***********

A Python library for creating actors using asyncio.

Installation
============

To install the latest release on `PyPi <https://pypi.python.org/pypi/async-actor>`_,
simply run:

::

  pip install async-actor

Or to install the latest development version, run:

::

  git clone https://github.com/xinhuang/async-actor.git
  cd async-actor
  python setup.py install

Quick Tutorial
==============

.. code:: pycon

  >>> from async_actor import Actor
  >>>
  >>> class Foo(object):
  >>>     def bar(self):
  >>>         return 42
  >>>
  >>> foo = Actor(Foo(), loop=loop)
  >>> future = foo.bar()
  >>> print(future.result())

API Reference
=============

``Actor(obj, loop)``
  Create an Actor instance wrapping ``obj``. Calls to ``obj`` will be executed in ``loop``.

  :Args:
    * ``obj``: The object to be wrapped.
    * ``loop``: The event loop to execute calls to ``obj``.

Licensing
=========

This project is released under the terms of the MIT Open Source License. View
*LICENSE.txt* for more information.
