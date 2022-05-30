#include "lists.h"

/**
 * check_cycle - checks if a cycle exists in a linked list
 *
 * @list - input list
 *
 * Return: 1 if cycle exists
 * 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast  = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
