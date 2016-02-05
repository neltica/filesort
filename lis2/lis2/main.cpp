#include <stdio.h>

int main()
{
	int n;
	int i,j;
	int arr[100][2];
	int lis[100];
	int temp;
	int max=0;

	scanf("%d",&n);
	for (i=0;i<n;i++)
	{
		scanf("%d%d",&arr[i][0],&arr[i][1]);
		for(j=i;j>0;j--)
		{
			if(arr[j][0]*arr[j][1]>arr[j-1][0]*arr[j-1][1])
			{
				temp=arr[j][0];
				arr[j][0]=arr[j-1][0];
				arr[j-1][0]=temp;

				temp=arr[j][1];
				arr[j][1]=arr[j-1][1];
				arr[j-1][1]=temp;
			}
		}
	}

	for(i=0;i<n;i++)
	{
		lis[i]=1;
		for(j=0;j<i;j++)
		{
			if( ((arr[i][0]<=arr[j][0]&&arr[i][1]<=arr[j][1]) && ((lis[j]+1)>lis[i])) || ((arr[i][0]<=arr[j][1]&&arr[i][1]<=arr[j][0]) && ((lis[j]+1)>lis[i])))
			{
				lis[i]=lis[j]+1;
				if(lis[i]>max)
				{
					max=lis[i];
				}
			}
		}
	}
	printf("%d",max);
	return 0;
}