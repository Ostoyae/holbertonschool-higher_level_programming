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

	if (!list || !list->next || !list->next->next)
		return (0);
	slow = list;
	fast = list->next->next;
	if (!slow->next || !fast)
		return (0);

	while (slow && fast)
	{
		if ((slow == fast) || (slow == fast->next))
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
