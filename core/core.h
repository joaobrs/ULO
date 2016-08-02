#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>
#include <numpy/npy_math.h>
#include "complex.h"
#include "bithacks.h"

static PyObject *query(PyObject *self, PyObject *args);    

// Method list
static PyMethodDef methods[] = {                                
  { "query", query, METH_VARARGS, "Query the simulator"},
  { NULL, NULL, 0, NULL } // Sentinel
};


