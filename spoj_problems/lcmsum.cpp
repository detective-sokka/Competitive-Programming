//getting time limit exceeded error inspite of the slution being correct


#include<stdio.h>
using namespace std;
long gcd(long i,long n);
int main()
{
  int j,tcases;
  long int i=1,sum=0,n;
  scanf("%d",&tcases);
  for(j=0;j<tcases;j++)
  {
    scanf("%ld",&n);
    i=1;
    sum=0;
    // calc the sum here
    while(i<=n)
    {
      sum+=(i*n)/gcd(i,n);
      i++;
    }
    printf("%ld\n",sum);
  }
  return 0;
}
long gcd(long a,long b)// to find gcd of 2 nos using euclids
{
  if(b==0) return a;
  return gcd(b,a%b);
}
