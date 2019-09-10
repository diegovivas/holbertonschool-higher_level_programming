#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - check the code for Holberton School students.
 * @head:structure doble pointer
 * @number:index;
 * Return: head.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodo;
	listint_t *ojo;

	nodo = malloc(sizeof(listint_t));
	if (!nodo)
	{
		return (NULL);
	}
	nodo->n = number;
	nodo->next = NULL;
	if (*head == NULL)
		return (NULL);
	ojo = *head;
	while (ojo->next)
	{
		if (nodo->n >= ojo->next->n)
			ojo = ojo->next;
		else
			break;
	}
	if (ojo->next == NULL)
		return (NULL);

	nodo->next = ojo->next;
	ojo->next = nodo;
	return (nodo);
}
