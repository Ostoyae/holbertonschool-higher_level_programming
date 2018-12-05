#include <stdlib.h>
#include "lists.h"

static listint_t *new_node(int number, listint_t **tail);

/**
 * insert_node - insert a node in a sorted list
 * @head: pointer to a pointer of head
 * @number: int of value for new node to insert with.
 *
 * Return: pointer to new Node or NULL if fail.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	if (!head || !(*head))
		return (NULL);
	temp = *head;

	while (temp)
	{
		if (number < temp->n)
		{
			new = new_node(number, head);
			if (new)
				*head = new;
			return (new);
		}
		else if (number == temp->n)
			return (temp);
		else if (temp->next && number < temp->next->n)
		{
			new = new_node(number, &temp->next);
			if (new)
				temp->next = new;
			return (new);
		}
		else if (!temp->next)
		{
			new = new_node(number, NULL);
			if (new)
				temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	return (NULL);
}

/**
 * new_node - create a new node.
 * @number: value to set the new node 'n' to
 * @tail: value to set node->next to
 *
 * Return: pointer to new node.
 */

static listint_t *new_node(int number, listint_t **tail)
{
	listint_t *node;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	if (tail)
		node->next = *tail;
	else
		node->next = NULL;

	return (node);
}
