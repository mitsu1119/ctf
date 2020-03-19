#include <stdio.h>
#include <time.h>

int main() {
	printf("%d\n", time(NULL));
	printf("%d\n", getpid());
	return 0;
}
