#include "lists.h"

/**
 * is_palindrome- function that checks if a singly linked list is a palindrome.
 * @head: pointer array to nodes
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *inicial = *head;
	listint_t *actual = *head;

	if (*head)
	{
		while (inicial)
		{
			actual = inicial->next;
			while (actual)
			{
				if (actual->n == inicial->n && actual->next == NULL)
					return (1);
				actual = actual->next;
			}
			inicial = inicial->next;
		}

	}
	return (0);
}
