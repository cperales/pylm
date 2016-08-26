Pylm
====

Pylm is the Python implementation of PALM, a framework to build
clusters of high performance microservices. It is presented in two
different levels of abstraction. In the high level API you will find
servers and clients that are functional *out of the box*. Use the high
level API if you are interested in simple communication patterns like
client-server, master-slave or a streaming pipeline. In the low level
API there are a variety of small components that, once combined
appropiately, they can be used to implement almost any kind of
microservice. It's what the high level API uses under the hood. Choose
the low level API if you are interested in creating your custom
microservice and your custom communication pattern.

.. important::

    Pylm requires a version of Python equal or higher than 3.4, and it is more
    thoroughly tested with Python 3.5.

Installing **pylm** is as easy as:

.. code-block:: bash

   $> pip install pylm

* `PIPY package page <https://pypi.python.org/pypi/pylm/>`_

* `Documentation <http://pythonhosted.org/pylm/>`_


Pylm is a project developed by `Guillem Borrell <http://guillemborrell.es>`_ for `NFQ Solutions
<http://nfqsolutions.com>`_.
