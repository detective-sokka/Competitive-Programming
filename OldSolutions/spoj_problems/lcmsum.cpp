//TLE 
//refered link : http://abhisharlives.blogspot.in/2012/06/really-fast-io-methods-for-programming.html 
//Alternate more mathematical solution : http://blog.forthright48.com/2015/08/spoj-lcmsum-lcm-sum.html

#include<stdio.h>
#include<cstdio>
//#define gc getchar_unlocked     //fast-io : faster input compared to scanf
//using namespace std;

//int gcd(int i,int n);
/*void scanint(int &x)        //***to be used only online judges as "getchar_unlocked is thread unsafe as it locks the screen while getting the input" ***
{
  register int c=gc();
  x=0; 
  int neg=0; 
  for(;(c<48 || c>57);c=gc());        //48= ascii for '0' ad 57 ascii for '9'
  if(c=='-'){neg=1;c=gc();}
  for(;c>48 && c<57;c=gc()){x=x*10+(c-48);}
} 
*/

int main()
{
  int j,tcases;
  int i=1,sum=0,n,minmultiple;
  scanf("%d",&tcases);
  for(j=0;j<tcases;j++)
  {
    scanf("%d",&n);
    i=1;
    sum=0;
    //calc the sum here
    while(i<=n)
    {
      minmultiple=i;
      while(minmultiple%i==0 && minmultiple%n==0)
      {
        minmultiple++;
      }
      sum+=minmultiple;
      i++;
    }
    printf("%d\n",sum);
  }
  return 0; 
}



/*int gcd(int a,int b)// to find gcd of 2 nos using euclids
{
  if(b==0) return a;
  return gcd(b,a%b);
}*/
