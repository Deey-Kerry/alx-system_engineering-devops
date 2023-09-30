#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - A function that creates an infinite loop
 * Return: an infinite loop
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - A function tht creates five zomie processes
 * Return: five zombies
 */
int main(void)
{
	int a;
	pid_t zombie;

	for (a = 0; a < 5; a++)
	{
		zombie = fork();
		if (!zombie)
		{
			return (0);
		}
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return (0);
}
