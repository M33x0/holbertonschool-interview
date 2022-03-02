#include "lists.h"

/**
 * _is_palindrome - Checks if a singly linked list is palindrome
 * @left: the head pointer of the given linked list.
 * @right: the head pointer of the given linked list.
 *
 * Return: 1 if the list is palindrome, 0 otherwise
 */

int _is_palindrome(listint_t **left, listint_t *right)
{
	int value;

	if (right == NULL)
	{
		return (1);
	}

	value = _is_palindrome(left, right->next) && ((*left)->n == right->n);

	*left = (*left)->next;
	return (value);
}

/**
 * is_palindrome - Checks if a singly linked list is palindrome
 * @head: the head pointer of the given linked list.
 *
 * Return: 1 if the list is palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	return (_is_palindrome(head, *head));
}
