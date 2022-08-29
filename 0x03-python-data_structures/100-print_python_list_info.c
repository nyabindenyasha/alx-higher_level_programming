#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Display basic information about a list.
 * @p: List.
 *
 */

void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: %s\n", i, PyList_GetItem(p, i)->ob_type->tp_name);
	}
}
