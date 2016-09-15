#include <stdio.h>

long int noofsqrs(int);

int main()
{
  int no;
  while(scanf("%d",&no))
  {
    if(no==0)
     break;
    printf("%ld\n",noofsqrs(no));
  }
  return 0;
}

long int noofsqrs(int n)
{
  long int sum=0;
  if(n==1)
    return 1;
  sum+=n*n+noofsqrs(n-1);
  return sum;
}
