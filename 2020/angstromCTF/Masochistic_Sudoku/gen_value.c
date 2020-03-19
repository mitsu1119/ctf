#include <stdio.h>
#include <stdlib.h>

int gen_value(int x, int y, int num) {
	srand(((num + x * 100 + y * 10 ^ 0x2aU) * 0xd) % 0x2753);
	return rand();
}

int main(int args, char *argv[]) {
	for(int i = 1; i < 10; i++) {
		printf("%d: %x\n", i, gen_value(atoi(argv[1]), atoi(argv[2]), i));
	}
	return 0;
}
