#include <stdio.h>

int main()
{
	//question 1 & 7
	int numbers[5] = {1 ,2, 3, 4, 5}; // subscipt takes integer and the array object is initialized

	//question 2
	printf("%d\n", numbers[6]); // doesn't give a compile error, no range checking

	//question 3 & 4 (explained in the doc)
	static int staticArray[5]; 					//static array
	int nonStaticArray[5]; 	   					//fixed stack-dynamic
	int *heapArray = malloc(sizeof(int) * 100); //fixed heap-dynamic

	//question 5
	int *ragged[3];

	ragged[0] = malloc(sizeof(int) * 5);
	ragged[1] = malloc(sizeof(int) * 7);
	ragged[2] = malloc(sizeof(int) * 3); // this way you can create ragged arrays

	int recArray[5][7]; 	//this way you can create rectangular arrays

	//question 6
	int multArray[1][2][3][4][5][6][7][8][9];  // you can create multidimensional arrays in
											   // in any dimension , no limit

	//question 8
	//C does not support this, if the user wants to do it, they have to come up with their own solution

	free(heapArray);
	return 0;
}