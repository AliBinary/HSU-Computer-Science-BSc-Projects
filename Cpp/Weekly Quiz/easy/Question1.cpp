#include <stdio.h>

int main()
{
	printf("Question 1: show size of data types(in Bytes).\n\n");
	printf("size of %s: %d\n", "char", sizeof(char));
	printf("size of %s: %d\n", "short int", sizeof(short int));
	printf("size of %s: %d\n", "int", sizeof(int));
	printf("size of %s: %d\n", "long int", sizeof(long int));
	printf("size of %s: %d\n", "float", sizeof(float));
	printf("size of %s: %d\n", "double", sizeof(double));

	return 0;
}
