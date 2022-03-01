#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: pointer to the head of the singly linked list
 * @number: the given integer number
 *
 * Return: A pointer to the new node, NULL otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;
	listint_t *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (number < (*head)->n)
	{
		new->next = (*head);
		(*head) = new;
		return (new);
	}

	while (current->next && number >= current->next->n)
	{
		current = current->next;
	}

	temp = current->next;
	current->next = new;
	new->next = temp;
	return (new);
}