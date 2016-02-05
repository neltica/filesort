#include <stdio.h>

int main()
{
	unsigned int n;
	int top=-1;
	unsigned int stack[80000];
	int i,j;
	long long result=0;
	unsigned int height;

	scanf("%d",&n);

	for(i=n-1;i>=0;i--)
	{
		scanf("%d",&height);
		if(top!=-1)
		{
			for(top;top>=0;top--)
			{
				if(height<stack[top])
				{
					top++;
					stack[top]=height;
					//stack[top][1]=0;
					for(j=0;j<top;j++)
					{
						//stack[j][1]+=1;
						result+=1;
					}
					break;
				}
				else
				{
					//result+=stack[top][1];
					if(top==0)
					{
						stack[top]=height;
						//stack[top][1]=0;
						break;
					}
				}
			}
		}
		else
		{
			top++;
			stack[top]=height;
			//stack[top][1]=0;
		}
	}
	/*for(i=top-1;i>=0;i--)
	{
		result+=stack[i][1];
	}*/
	printf("%Ild",result);
	return 0;
}