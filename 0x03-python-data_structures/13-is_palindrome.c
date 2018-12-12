#include "lists.h"

int rec_pal(listint_t **head, listint_t *tail);

int is_palindrome(listint_t **head)
{
	return (rec_pal(head, (*head)->next));
}

int rec_pal(listint_t **head, listint_t *tail)
{
	int status = 0;
	if (tail)
	{
		status = rec_pal(head, tail->next);
		if ((*head)->n == tail->n)
			status = 1;
		*head = (*head)->next;
	}

	return (status);
}
