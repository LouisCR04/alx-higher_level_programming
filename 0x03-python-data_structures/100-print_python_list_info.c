#include <stdlib.h>
#include <stdio.h>
#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: Python Object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	size_t s;
	size_t x = 0;
	PyObject *obj;

	s = PyList_Size(p);
	printf("[*] Size of the Python List = %zu\n", s);
	printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);
	while (x < s)
	{
		obj = PyList_GET_ITEM(p, x);
		printf("Element %zu: %s\n", x, Py_TYPE(obj)->tp_name);
		x++;
	}
}
