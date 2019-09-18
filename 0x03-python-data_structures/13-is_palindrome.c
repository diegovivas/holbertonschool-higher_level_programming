#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: pointer to head of list
 * Return: 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ojo, *ojo2;
	int tama = 0;
	int ciclador = 0;
	int iterador = 0;
	int otra = 0;

	if (!*head)
		return (1);
	ojo = *head;
	ojo2 = *head;
	while (ojo->next)
	{
		ojo = ojo->next;
		tama++;
	}
	ojo = *head;
	ciclador = tama + 1;
	otra = (tama / 2) - 1;
	while (iterador < ciclador && tama != otra)
	{
		ojo2 = ojo2->next;
		iterador++;
		if (iterador == tama)
		{
			if (ojo->n == ojo2->n)
			{
				iterador = 0;
				tama--;
				ojo2 = ojo;
				ojo = ojo->next;
			}
			else
				return (0);
		}
	}
	return (1);
}