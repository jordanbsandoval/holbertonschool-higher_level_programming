#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *tmp = list->next;

	while (tmp)
	{
		printf("list: %d\ntmp: %d\n", list->n, tmp->n);
		if (tmp->n == list->n)
			return (1);
		tmp = tmp->next;
	}
	return (0);
}
