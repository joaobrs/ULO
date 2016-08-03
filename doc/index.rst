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

Import some stuff::

    >>> from ulo import Circuit, BS, Swap, State, get_amplitudes

The easiest way to create a circuit is to subclass ``ulo.Circuit``.  
Let's define a class that represents the fusion gate::

    >>> class FusionII(Circuit):
    >>>     components = [BS(0, 1), BS(2, 3), Swap(1, 2), BS(0, 1), BS(2, 3)]
    >>> ...

Instatiate an instance::

    >>> circuit = FusionII()
    >>> print circuit
    FusionII ()
    .  Beamsplitter (0, 1), ratio = 1/2
    .  Beamsplitter (2, 3), ratio = 1/2
    .  Swap (1, 2)
    .  Beamsplitter (0, 1), ratio = 1/2
    .  Beamsplitter (2, 3), ratio = 1/2

Make the state vector :math:`|0, 1, 2, 3\rangle` : ::

    >>> state = State({(0, 1, 2, 3): 1})
    >>> print state
    | 0, 1, 2, 3 ❭ :	  √ 1	

And now simulate propagation thru the circuit::

    >>> u = circuit.get_unitary()
    >>> print u
    [[ 0.5+0.j   0.0+0.5j  0.0+0.5j -0.5+0.j ]
     [ 0.0+0.5j -0.5+0.j   0.5+0.j   0.0+0.5j]
     [ 0.0+0.5j  0.5+0.j  -0.5+0.j   0.0+0.5j]
     [-0.5+0.j   0.0+0.5j  0.0+0.5j  0.5+0.j ]]

    >>> get_amplitudes(state, u, ((0, 1, 2, 3),))
    | 0, 1, 2, 3 ❭ :	  √ 1/4	

.. todo::

    The above is going to get deprecated, fast


Using ``ulo``
-------------------------------

There are three key concepts -- ``Circuits``, ``States``, and ``Simulators``.

.. autoclass:: ulo.circuit.Circuit

    .. automethod:: ulo.circuit.Circuit.__init__

    .. automethod:: ulo.circuit.Circuit.decompose

    .. automethod:: ulo.circuit.Circuit.get_unitary

    .. automethod:: ulo.circuit.Circuit.show_decomposition

    .. automethod:: ulo.circuit.Circuit.set_parameter

    .. automethod:: ulo.circuit.Circuit.__str__

.. autoclass:: ulo.circuit.Component

    .. automethod:: ulo.circuit.Component.decompose

    .. automethod:: ulo.circuit.Component.set_parameter

.. autoclass:: ulo.state.State
    
    .. automethod:: ulo.state.State.__init__

    .. automethod:: ulo.state.State.__str__

    .. automethod:: ulo.state.State.__or__

    .. automethod:: ulo.state.State.__mul__


Reference
-------------------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

