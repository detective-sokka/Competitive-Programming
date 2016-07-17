#include <stdio.h>

int main()
{
	//const long int index=1000000;
 	//long int no,array[index],i=0;
	long int no;

 	while(1)
 	{
 		scanf("%ld",&no);
 		if (no==42) break;
		printf("\n%ld",no);
 		//array[i]=no;
 		//i++;
 	}
 	/* for(no=0;no<i;no++)
 			printf("\n%ld",array[no]);
	*/
 	return 0;
}
