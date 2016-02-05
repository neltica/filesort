#include <stdio.h>


int mininum(int a,int b)
{
	if(a>=b)
	{
		if(b!=0)
		{
			return b;
		}
		else
		{
			return a;
		}
	}
	else
	{
		if(a!=0)
		{
			return a;
		}
		else
		{
			return b;
		}
	}
}
int main()
{
	int coin_num,chang_money;
	int coin[11];
	int table[11][64001];
	int i,j;
	int temp;
	int min=-1;

	scanf("%d",&coin_num);

	for(i=0;i<coin_num;i++)
	{
		scanf("%d",&coin[i]);
	}
	scanf("%d",&chang_money);


	for(i=0;i<=coin_num;i++)
	{
		table[i][0]=0;
	}

	for(i=0;i<=chang_money;i++)
	{
		table[0][i]=0;
	}


	for(i=1;i<=coin_num;i++)
	{
		for(j=1;j<=chang_money;j++)
		{
			temp=((j/coin[i-1])*coin[i-1]);
			if(temp+((j-temp)*table[i-1][j-temp])==j)
			{
				table[i][j]=mininum((j/coin[i-1])+table[i-1][j-temp],table[i-1][j]);
			}
			else
			{
				table[i][j]=table[i-1][j];
			}
		}
	}
/*
	for(i=0;i<=coin_num;i++)
	{
		for(j=0;j<=chang_money;j++)
		{
			printf("%d ",table[i][j]);
		}
		printf("\n");
	}
	*/

	for(i=0;i<=coin_num;i++)
	{
		printf("%d\n",table[i][chang_money]);
	}

	for(i=1;i<=coin_num;i++)
	{
		if(min!=-1)
		{
			if(table[i][chang_money]<min)
			{
				min=table[i][chang_money];
			}
		}
		else
		{
			if(table[i][chang_money]!=0)
			{
				min=table[i][chang_money];
			}
		}
	}

	if(min!=-1)
	{
		printf("%d",min);
	}
	else
	{
		printf("impossible");
	}


	return 0;
}
