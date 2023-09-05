#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to head of list
 * @number: The number to insert
 * Return: Address of inserted node else Null if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *holder, *new;

	holder = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (holder == NULL || holder->n >= number)
	{
		new->next = holder;
		*head = new;
		return(new);
	}

	while (holder != NULL && holder->next != NULL && holder->next->n < number)
		holder = holder->next;

	new->next = holder->next;
	holder->next = new;

	return (new);
}
