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

  npy_complex a = npy_cpack(0, 1);
  

  PyObject *output = PyDict_New();
  return output;
}
