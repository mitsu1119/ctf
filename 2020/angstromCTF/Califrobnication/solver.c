#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
	FILE *f;
	char flag[50] = "i8_4a5_}fdlo91oaeci12c{dcm6atfo4inrncrb0aafftd5_";
	strtok(flag, "\n");
	// memfrob(&flag, strlen(flag));
	size_t len = strlen(flag);

	// srand(atoi(argv[1]));
	static int init;
	static struct random_data rdata;
	if(!init) {
		static char state[32];
		rdata.state = NULL;
		initstate_r (atoi(argv[1]), state, sizeof (state), &rdata);
		init = 1;
	}

	int32_t rands[len - 1];
	for(size_t i = 0; i < len - 1; i++) {
		random_r(&rdata, &rands[i]);
		// rands[i] = rand();
	}

	for(int i = len - 2; i >= 0; i--) {
		int32_t j = rands[i];
		j = j % (len - i) + i;
		printf("%d\n", j);

		char c = flag[i];
		flag[i] = flag[j];
		flag[j] = c;
	}

	printf("Here's your encrypted flag: %s\n", &flag);
}
