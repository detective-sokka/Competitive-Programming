#include<stdio.h>
int main()
{
	int no;
	while(scanf("%d",&no))
	{
		if(no==0 || no==1)
		{
			printf("%d",no);
		}
		else
		{
			printf("%d\n",((2*no)-2));
		}
	}
	return 0;
}