#include "lists.h"

/**
 * check_cycle - checks if a list has a loop in it
 *
 * @list: pointer to head node
 *
 * Return: 1 if list has a loop, 0 if not
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list && list->next)
	{
		while (slow && fast && fast->next)
		{
			slow = slow->next;
			fast = fast->next->next;

			if (slow == fast)
				return (1);
		}
	}

	return (0);
}