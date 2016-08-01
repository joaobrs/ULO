/* Core functionality of ulo */
#include "core.h"

// Module initialization
PyMODINIT_FUNC initcore(void) {                            
  (void) Py_InitModule("core", methods);
  import_array();
}

// This is a wrapper which chooses the optimal permanent function
static PyObject *query(PyObject *self, PyObject *args) {
  // Parse the arguments
  PyArrayObject *unitary;
  if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &unitary)) {return NULL;}
  /*if (!PyArray_ISCOMPLEX(unitary)) {*/
      /*PyErr_SetString(PyExc_TypeError, "Array dtype must be `complex`.");*/
      /*return NULL;*/
  /*}*/

  /*npy_complex128 c = npy_csqrt(a);*/
  /*return PyComplex_FromDoubles(c.real, c.imag);*/

  PyObject *output = PyDict_New();
  return output;
}
