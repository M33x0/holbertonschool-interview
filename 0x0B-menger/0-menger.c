#include "menger.h"

/**
 * menger - draws a 2D Menger Sponge
 * @level: number of levels of the sponge
 *
 * Return: Nothing.
 */

void menger(int level)
{
	int r, c, size;

	if (level >= 0)
	{
		size = pow(3, level);
		for (r = 0; r < size; r++)
		{
			for (c = 0; c < size; c++)
				putchar(which_char(r, c));
			putchar('\n');
		}
	}
}

/**
 * which_char - Computes the needed char
 *
 * @r: rows
 * @c: columns
 *
 * Return: "#" or " "
 */

char which_char(int r, int c)
{
	while (r || c)
	{
		if (r % 3 == 1 && c % 3 == 1)
			return (' ');
		r = r / 3;
		c = c / 3;
	}
	return ('#');
}
