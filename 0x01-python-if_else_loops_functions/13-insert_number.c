#include "lists.h"

/**
 * insert_node- funct in C that inserts a number in a sorted singly linked list
 * @head: array of structures
 * @number: number to inserts in to singly linked list
 * Return: 
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *actual = *head;
	listint_t *new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	printf("actuali: %d\n", actual->n);
	while (actual)
	{
		if (actual->n > number)
		{
			new_node->next = actual;
			tmp->next = new_node;
			printf("tmp1: %d\n", tmp->n);
			return (tmp);
		}
		tmp = actual;
		printf("tmp:%d\n", tmp->n);
		actual = actual->next;
	}
	return (NULL);
}
