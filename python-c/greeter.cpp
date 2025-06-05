#include <python3.13/Python.h>
#include <iostream>

// The C++ function to be exposed
static PyObject* greeter_cpp(PyObject* self, PyObject* args) {
    std::cout << "hi" << std::endl;
    Py_RETURN_NONE; // Return None to Python
}

// Define the methods of the module
static PyMethodDef GreeterMethods[] = {
    {"greeter_c", greeter_cpp, METH_NOARGS, "A function that prints 'hi'"},
    {nullptr, nullptr, 0, nullptr} // Sentinel to indicate the end of the array
};

// Define the module
static struct PyModuleDef greeter_module = {
    PyModuleDef_HEAD_INIT,
    "greeter", // Name of the module
    "A simple Python module implemented in C++", // Module docstring
    -1, // Size of per-interpreter state or -1 if not needed
    GreeterMethods // Method definitions
};

// Initialize the module
PyMODINIT_FUNC PyInit_greeter(void) {
    return PyModule_Create(&greeter_module);
}
