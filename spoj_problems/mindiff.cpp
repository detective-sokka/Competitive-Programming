//

#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
	int na,nb,nc,tcases,i,j,k,res;
	int a[1000],b[1000],c[1000],resl=32766;
	cin>>tcases;
	while(tcases>0)
	{
		cin>>na>>nb>>nc;
		for(i=0;i<na;i++)
			cin>>a[i];
		for(i=0;i<nb;i++)
			cin>>nb;
		for(i=0;i<nc;i++)
			cin>>nc;
		for(i=0;i<na;i++)
			for(j=0;j<nb;j++)
				for(k=0;k<nc;k++)
				{

					res=abs(a[i]-b[j])+abs(b[j]-c[k])+abs(c[k]-a[i]);
					if(res<resl)
						resl=res;	
				}
		cout<<resl<<endl;		
		tcases--;
	}	
	return 0;
}