#include "lists.h"

/**
 * insert_node - inserts a new node to list
 *
 * @head - beginning or end of node
 * @number - data to be inputted
 *
 * Return: nothing
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = malloc (sizeof(listint_t));

	temp->n = number;
	temp->next = NULL;
	if (*head != NULL)
	{
		temp->next = *head;
	}
	*head = temp;
	return (0);
}
