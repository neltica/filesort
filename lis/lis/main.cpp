#include <stdio.h>

int main()
{
	int num;
	int arr[200];
	int count[200];
	int i,j;
	int max=0;

	scanf("%d",&num);

	for (i=0;i<num;i++)
	{
		scanf("%d",&arr[i]);
		count[i]=1;
		for(j=0;j<i;j++)
		{
			if(arr[j]<arr[i] && count[j]+1>count[i])
			{
				count[i]=count[j]+1;
				if(count[i]>max)
				{
					max=count[i];
				}
			}
		}
	}

	/*for(i=0;i<num;i++)
	{
		printf("%d ",count[i]);
	}*/
	printf("%d",num-max);


	return 0;
}