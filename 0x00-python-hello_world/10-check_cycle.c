#include "lists.h"

/**
 * check_cycle - Check if a list is a cycle.
 * @list: the list to check.
 * Return: 1 if is a cycle, 0 if doesn't.
 */

int check_cycle(listint_t *list)
{
	listint_t *advanced = list;
	listint_t *retraced = list;

	while (advanced != NULL && advanced->next != NULL)
	{
		retraced = retraced->next;
		advanced = advanced->next->next;
		
		if (advanced == retraced)
			return (1);
	}
	return (0);
}
