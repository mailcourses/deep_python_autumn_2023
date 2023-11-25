#include <stdlib.h>
#include <stdio.h>

#include <Python.h>

PyObject* cutils_sum(PyObject* self, PyObject* args)
{
    PyObject* list_obj;
    long int elem_count;
    if (!PyArg_ParseTuple(args, "Ol", &list_obj, &elem_count))
    {
        printf("Failed to parse arguments");
        return NULL;
    }

    long int list_len = PyList_Size(list_obj);
    int res = 0;
    for (int i = 0; i < list_len && i < elem_count; ++i)
    {
        PyObject* tmp = PyList_GetItem(list_obj, i);
        int elem = PyLong_AsLong(tmp);
        res += elem;
    }
    return Py_BuildValue("i", res);
}

int fibonacci(int n)
{
    if (n < 2)
    {
        return 1;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}

PyObject* cutils_fibonacci(PyObject* self, PyObject* args)
{
    int n = 0;
    if (!PyArg_ParseTuple(args, "i", &n))
    {
        printf("Failed to parse arguments");
        return NULL;
    }
    int res = fibonacci(n);
    return Py_BuildValue("i", res);
}

static PyMethodDef methods[] = {
    {"sum", cutils_sum, METH_VARARGS, "sum of first n elements of our array"},
    {"fibonacci", cutils_fibonacci, METH_VARARGS, "returns i'th element of fibonacci sequance"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module_cutils = {
    PyModuleDef_HEAD_INIT, "cutils", NULL, -1, methods
};

PyMODINIT_FUNC PyInit_cutils()
{
    return PyModule_Create( &module_cutils );
}
