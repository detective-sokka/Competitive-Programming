#include <stdio.h>

int main()
{
	const long int index=1000000;
 	long int no,array[index],i=0;

 	while(1)
 	{
 		scanf("%ld",&no);
 		if (no==42) break;
 		array[i]=no;
 		i++;
 	}
 	for(no=0;no<i;no++)
 			printf("\n%ld",array[no]);
 	return 0;
}
