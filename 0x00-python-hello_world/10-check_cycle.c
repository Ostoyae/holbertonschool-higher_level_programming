#include "lists.h"

/**
 * check_cycle - check if a given link list cycles on it's self
 * @list: pointer to a listint_t type node
 *
 * Return: 0 if no cycle is found else 1 if one is found.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	int val = 0;

	if (!list || !list->next || !list->next->next)
		return (0);
	slow = list;
	fast = list;

	while (fast)
	{	
		val++;
		fast = fast->next;
		if (val % 2 == 0)
			slow = slow->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
