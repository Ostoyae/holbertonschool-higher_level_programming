#include "lists.h"

int rec_pal(listint_t **head, listint_t *tail);

/**
 * is_palindrome - check if a link list is a palindrome
 * @head: double pointer to head
 *
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	return (rec_pal(head, (*head)->next));
}

/**
 * rec_pal - recusivly go through a link like to determin if it's an palindrome
 * @head: double pointer to head
 * @tail: pointer to node in a link list
 *
 * Return: 1 if palindrome else 0
 */
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
