#include "lists.h"

int check_cycle(listint_t *list)
{
	int i = 0;

	if (!list)
		return (0);

	while (list)
	{
		list = list->next;
		i++;
		if (i > 100)
			return (1);
	}
	return (0);
}
