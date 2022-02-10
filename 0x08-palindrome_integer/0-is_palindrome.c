#include "palindrome.h"

/**
 * reverse - reverses a given integer into a reversed one
 * @n: The given integer
 * @reversed: the reversed version of n
 *
 * Return: The reversed number
 */
unsigned long reverse(unsigned long n, unsigned long reversed)
{
	if (n == 0)
		return (reversed);
	reversed = (reversed * 10) + (n % 10);
	return (reverse(n / 10, reversed));
}

/**
 * is_palindrome - Checks wheter an integer is palindrome or not
 * @n: the given integer
 *
 * Return: 1 if n is palindrome, 0 otherwise
 */
int is_palindrome(unsigned long n)
{
	unsigned long reversed;

	reversed = reverse(n, 0);
	if (n == reversed)
		return (1);
	return (0);
}
