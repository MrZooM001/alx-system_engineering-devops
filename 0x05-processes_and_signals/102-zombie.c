#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * main - Start point of the program.
 *
 * Return: 0 if success, otherwise if failed.
*/
int main(void)
{
pid_t zombie_pid;
char c;

for (c = 0; c < 5; c++)
{
zombie_pid = fork();
if (zombie_pid > 0)
{
printf("Zombie process created, PID: %d\n", zombie_pid);
sleep(1);
}
else
{
exit(EXIT_SUCCESS);
}
}

while (1)
{
sleep(1);
}

return (EXIT_SUCCESS);
}
