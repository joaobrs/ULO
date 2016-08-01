/* Functions to compute the permanent, given a numpy array */
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>
#include <numpy/npy_math.h>
#include "bithacks.h"

// Forward function declaration 
static PyObject *permanent(PyObject *self, PyObject *args);    

// Method list
static PyMethodDef methods[] = {                                
  { "permanent", permanent, METH_VARARGS, "Computes the permanent of a numpy using the most appropriate method available"},
  { NULL, NULL, 0, NULL } // Sentinel
};

// Module initialization
PyMODINIT_FUNC initpermanent(void) {                            
  (void) Py_InitModule("permanent", methods);
  import_array();
}

// This is a wrapper which chooses the optimal permanent function
static PyObject *permanent(PyObject *self, PyObject *args) {
  // Parse the input
  PyArrayObject *submatrix;
  if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &submatrix)) {return NULL;}
  if (!PyArray_ISCOMPLEX(submatrix)) {
      PyErr_SetString(PyExc_TypeError, "Array dtype must be `complex`.");
      return NULL;
  }

  // Compute the permanent
  npy_complex128 p = ryser(submatrix);
  return PyComplex_FromDoubles(p.real, p.imag);
}
