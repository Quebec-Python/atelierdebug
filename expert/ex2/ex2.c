#include <Python.h>
#include <stdint.h>

static uint64_t _fib(uint64_t n) {
    if (n == 1 || n == 2) {
        return 1;
    }
    uint64_t prev1 = 1;
    uint64_t prev2 = 1;
    for (uint64_t i = 1; i < n; ++i) {
        uint64_t next = prev1 + prev2;
        prev2 = prev1;
        prev1 = next;
    }
    return prev1;
}

static PyObject* fib(PyObject* self, PyObject* args) {
    int64_t n;

    if (!PyArg_ParseTuple(args, "L", &n)) {
        return NULL;
    }
    if (n < 0) {
        return NULL;
    }
    uint64_t f = _fib(n);    
    return Py_BuildValue("L", f);
}

static PyMethodDef c_python_methods[] =
{
     {"fib", fib, METH_VARARGS, "Compute a fibonacci sequence value."},
     {NULL, NULL, 0, NULL}
};

static struct PyModuleDef c_python_module = {
    PyModuleDef_HEAD_INIT,
    "c_python_exaplme",
    "Example module",
    -1,
    c_python_methods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC
PyInit_ex2(void)
{
     return PyModule_Create(&c_python_module);
}
