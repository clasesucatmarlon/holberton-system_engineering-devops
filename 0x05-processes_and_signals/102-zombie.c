#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - loop infinite
 * Return: 0
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
 * main - craeted 5 zombie process
 * Return: 0 if loop infinite
 */

int main(void)
{
	pid_t pid;
	int x;

	for (x = 0; x < 5; x++)
	{
		pid = fork();
		if (pid < 1)
			return (0);
		printf("Zombie process created, PID: %d\n", pid);
	}
	return (infinite_while());
}
