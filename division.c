#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
	if(argc!=2) return -1;
	int nb = atoi(argv[1]);
	return (nb%2==0)?0:-1;
}
