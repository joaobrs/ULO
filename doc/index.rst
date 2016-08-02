.. toctree::
   :maxdepth: 2


``ulo``
===============================

This is the documentation for ``ulo``. It's a work in progress.

``ulo`` is a Python package to simulate linear optical circuits. It's based on a chunk of optimized C code that computes a lot of permanents.

Installing
-------------------------------

You can install from ``pip``:

.. code-block:: bash

   $ pip install --user ulo

Alternatively, clone from the `github repo <https://github.com/peteshadbolt/ulo>`_ and run ``setup.py``:

.. code-block:: bash

   $ git clone https://github.com/peteshadbolt/ulo
   $ cd ulo
   $ python setup.py install --user

If you want to modify and test ``ulo`` without having to re-install, switch into ``develop`` mode:

.. code-block:: bash

   $ python setup.py develop --user  


Quickstart
-------------------------------

The easiest way to create a circuit is to subclass ``ulo.Circuit``::

    >>> from ulo import Circuit, BS, Swap
    >>> class FusionII(Circuit):
    >>>     components = [BS(0, 1), BS(2, 3), Swap(1, 2), BS(0, 1), BS(2, 3)]
    >>> ...
    >>> circuit = FusionII()
    >>> print circuit



Using ``ulo``
-------------------------------

.. automodule:: ulo.circuit


Reference
-------------------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

