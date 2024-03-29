#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    if (PyList_Check(p)) {
        size = PyList_Size(p);
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (i = 0; i < size; i++) {
            item = PyList_GetItem(p, i);
            printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
        }
    } else {
        printf("  [ERROR] Invalid List Object\n");
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *trying_str = NULL;

    printf("[.] bytes object info\n");
    if (PyBytes_Check(p)) {
        size = PyBytes_Size(p);
        trying_str = PyBytes_AsString(p);

        printf("  size: %zd\n", size);
        printf("  trying string: %s\n", trying_str);
        printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

        for (i = 0; i < size && i < 10; i++) {
            printf(" %02hhx", trying_str[i]);
        }

        printf("\n");
    } else {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}
