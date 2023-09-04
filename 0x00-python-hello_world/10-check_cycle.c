#include "lists.h"

/**
 * check_cycle - Checks if a singly liinked list has a cycle
 *
 * @list: Pointer to the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *tortoise, *hare;

	if (list == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;

		if (tortoise == hare)
			return (1);
		i++;
	}

	return (0);
}
