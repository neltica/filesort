
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curses.h>


typedef struct node
{
	char* zipCode;
	char* cityName;
	char* state;
	struct node *next;
}NODE;

typedef struct token
{
	char * data;
	struct token *next;
}TOKEN;


TOKEN *token_list_head,*token_list_end;
NODE *node_list_head,*node_list_end;
int nodeSize=0;
int cityCount=0;
int crsX,crsY;




void create_NODE()
{
	node_list_head=(NODE*)malloc(sizeof(NODE));
	node_list_head->zipCode=NULL;
	node_list_head->cityName=NULL;
	node_list_head->state=NULL;

	node_list_end=node_list_head;
	nodeSize=1;
}

void insert_NODE(char* _zipcode,char* _cityName,char* _state)
{
    printf("1");
	NODE *new_node=(NODE*)malloc(sizeof(NODE));
	printf("2");
	new_node->zipCode=(char*)malloc(sizeof(char)*1024);
	printf("3");
	strcpy(new_node->zipCode,_zipcode);
	printf("4");
	new_node->cityName=(char*)malloc(sizeof(char)*1024);
	printf("5");
	strcpy(new_node->cityName,_cityName);
	printf("6");
	new_node->state=(char*)malloc(sizeof(char)*1024);
	printf("7");
	strcpy(new_node->state,_state);
	printf("8");
	new_node->next=NULL;
	printf("9");

	node_list_end->next=new_node;
	printf("a");
	node_list_end=new_node;
	printf("b");
	nodeSize++;
	printf("c");
}

void clear_NODE(NODE *_head)
{
	NODE * next_node;
	while(1)
	{
		if(_head->next!=NULL)
		{
			next_node=_head->next;
			free(_head);
			_head=next_node;
		}
		else
		{
			break;
		}
	}
}

void create_TOKEN()
{
	token_list_head=(TOKEN*)malloc(sizeof(TOKEN));
	token_list_head->data=NULL;

	token_list_end=token_list_head;
}

void insert_TOKEN(char *_data)
{
	//printf("1");
	TOKEN *new_node=(TOKEN*)malloc(sizeof(TOKEN));
	//printf("2");
	new_node->data=(char*)malloc(sizeof(char)*strlen(_data));
	strcpy(new_node->data,_data);
	//printf("3");
	new_node->next=NULL;
	//printf("4");
	token_list_end->next=new_node;
	//printf("5");
	token_list_end=new_node;
	//printf("6\n");
}

void clear_TOKEN(TOKEN *_head)
{
	TOKEN * next_node;
	while(1)
	{
		if(_head->next!=NULL)
		{
			next_node=_head->next;
			free(_head);
			_head=next_node;
		}
		else
		{
			break;
		}
	}
}


/*
void result_window_refresh(int scrX,int scrY,int ch_num,char * key)
{
	WINDOW *sub_win;
	NODE *now_node=node_list_head;
	int i;
	sub_win=newwin(nodeSize+2,scrX,5,0);
	refresh();
	box(sub_win,0,0);
	move(crsY,crsX);
	wrefresh(sub_win);
}
*/

void result_window_refresh(int scrX,int scrY,int ch_num,char * key)
{
    WINDOW *sub_win;
    char *Tags[]={"Show_x0020_All_x0020_ZIP_x0020_Codes","ZIP_x0020_Code","/ZIP_x0020_Code","City","/City","State_x0020_Abbreviation","/State_x0020_Abbreviation","/Show_x0020_All_x0020_ZIP_x0020_Codes"};
	char *string;
	char *token;
	int i;
	int flag=0;

	TOKEN * now_token;
	NODE *now_node;

	char *zipcode;
	char *cityName;
	char *state;

	FILE *file;
	file=fopen("zipcode.xml","rt");
	string=(char*)malloc(sizeof(char)*1024);
	//printf("file open\n");

	i=0;
	while(1)
	{
		//i++;
		if(fgets(string,1024,file)==NULL)
		{
			break;
		}
		//printf("%d %s\n",i++,string);
		while(1)
		{
			if(flag==0)
			{
				token=strtok(string,"<>");
				flag=1;
			}
			else
			{
				token=strtok(NULL,"<>");
			}
			if(token==NULL)
			{
				flag=0;
				break;
			}
			else
			{
				if(strstr(token,key)!=NULL)
				{
					//printf("%d zipcode: %s city: %s\n",i,zipcode,token);
					i++;
					cityName=(char*)malloc(sizeof(char)*1024);
					strcpy(cityName,token);
				}
				else if(strcmp(token,Tags[1])==0)
				{
					token=strtok(NULL,"<>");
					if(token==NULL)
					{
						flag=0;
						break;
					}
					zipcode=(char*)malloc(sizeof(char)*1024);
					strcpy(zipcode,token);

				}

				else if(strcmp(token,Tags[5])==0)
				{
                    token=strtok(NULL,"<>");
					if(token==NULL)
					{
						flag=0;
						break;
					}
					state=(char*)malloc(sizeof(char)*1024);
					strcpy(state,token);
					//i++;
					//printf("%d zipcode: %s city: %s state:%s\n",i,zipcode,cityName,state);
					//insert_NODE(zipcode,cityName,state);
				}

			}
		}
	}
	if(i+2<scrY)
	{
        sub_win=newwin(i+2,scrX,5,0);
    }
    else
    {
        sub_win=newwin(scrY,scrX,5,0);
    }
	refresh();
	box(sub_win,0,0);
	wrefresh(sub_win);
    mvprintw(2,1,"%d",i);
	i=0;
	fseek(file,0,0);
	while(1)
	{
		//i++;
		if(fgets(string,1024,file)==NULL)
		{
			break;
		}
		//printf("%d %s\n",i++,string);
		while(1)
		{
			if(flag==0)
			{
				token=strtok(string,"<>");
				flag=1;
			}
			else
			{
				token=strtok(NULL,"<>");
			}
			if(token==NULL)
			{
				flag=0;
				break;
			}
			else
			{
				if(strstr(token,key)!=NULL)
				{
					//printf("%d zipcode: %s city: %s\n",i,zipcode,token);
					i++;
					cityName=(char*)malloc(sizeof(char)*1024);
					strcpy(cityName,token);
					mvprintw(i+5,1,"%d zipcode: %s /city: %s",i,zipcode,cityName);
				}
				else if(strcmp(token,Tags[1])==0)
				{
					token=strtok(NULL,"<>");
					if(token==NULL)
					{
						flag=0;
						break;
					}
					zipcode=(char*)malloc(sizeof(char)*1024);
					strcpy(zipcode,token);

				}

				else if(strcmp(token,Tags[5])==0)
				{
                    token=strtok(NULL,"<>");
					if(token==NULL)
					{
						flag=0;
						break;
					}
					state=(char*)malloc(sizeof(char)*1024);
					strcpy(state,token);
					//mvprintw(i+6,1,"%d zipcode: %s /city: %s /state:%s",i,zipcode,cityName,state);
					//insert_NODE(zipcode,cityName,state);
				}

			}
		}
	}
	move(crsY,crsX);


	fclose(file);
}
void insert_window_refresh(WINDOW *my_win,int scrX,int scrY)
{
	char ch;
	char *string;
	int index=0;
	WINDOW *erase_win;

	string=(char*)malloc(sizeof(char)*1024);
	my_win=newwin(4,scrX,0,0);
	refresh();
	box(my_win,0,0);
	wprintw(my_win,"Search");
	wrefresh(my_win);

	mvprintw(1,1,"insert city name:");
	getyx(stdscr,crsY,crsX);


	while(1)
	{
		ch=getch();
		if (ch!='\n')
		{
			string[index]=ch;
			index++;
			string[index]='\0';
			crsX++;
			clear();

			my_win=newwin(4,scrX,0,0);
			refresh();
			box(my_win,0,0);
			wprintw(my_win,"Search");
			wrefresh(my_win);

			mvprintw(1,1,"insert city name: %s",string);
			getyx(stdscr,crsY,crsX);
			result_window_refresh(scrX,scrY,index,string);
		}
		else
		{
			index=0;
			//wclear(my_win);
			//box(my_win,0,0);
			//wprintw(my_win,"Search");
			//mvprintw(1,1,"insert city name:");
			//getyx(stdscr,crsY,crsX);
			//wrefresh(my_win);

			clear();


			my_win=newwin(4,scrX,0,0);
			refresh();
			box(my_win,0,0);
			wprintw(my_win,"Search");
			wrefresh(my_win);

			mvprintw(1,1,"insert city name:");
			getyx(stdscr,crsY,crsX);
		}

	}
}



void parsing(char * key,WINDOW *sub_win)
{
	char *Tags[]={"Show_x0020_All_x0020_ZIP_x0020_Codes","ZIP_x0020_Code","/ZIP_x0020_Code","City","/City","State_x0020_Abbreviation","/State_x0020_Abbreviation","/Show_x0020_All_x0020_ZIP_x0020_Codes"};
	char *string;
	char *token;
	int i;
	int flag=0;

	TOKEN * now_token;
	NODE *now_node;

	char *zipcode;
	char *cityName;
	char *state;

	FILE *file;
	file=fopen("zipcode.xml","rt");
	string=(char*)malloc(sizeof(char)*1024);
	//printf("file open\n");

	i=0;
	while(1)
	{
		i++;
		if(fgets(string,1024,file)==NULL)
		{
			break;
		}
		//printf("%d %s\n",i++,string);
		while(1)
		{
			if(flag==0)
			{
				token=strtok(string,"<>");
				flag=1;
			}
			else
			{
				token=strtok(NULL,"<>");
			}
			if(token==NULL)
			{
				flag=0;
				break;
			}
			else
			{
				if(strcmp(token,key)==0)
				{
					//printf("%d zipcode: %s city: %s\n",i,zipcode,token);
					cityName=(char*)malloc(sizeof(char)*1024);
					strcpy(cityName,token);
				}
				else if(strcmp(token,Tags[1])==0)
				{
					token=strtok(NULL,"<>");
					if(token==NULL)
					{
						flag=0;
						break;
					}
					zipcode=(char*)malloc(sizeof(char)*1024);
					strcpy(zipcode,token);

				}

				else if(strcmp(token,Tags[5])==0)
				{
                    token=strtok(NULL,"<>");
					if(token==NULL)
					{
						flag=0;
						break;
					}
					state=(char*)malloc(sizeof(char)*1024);
					strcpy(state,token);

					//printf("%d zipcode: %s city: %s state:%s\n",i,zipcode,cityName,state);
					//insert_NODE(zipcode,cityName,state);
				}

			}
		}
	}

	fclose(file);
}


main()
{
	int ch;
	char * c;
	int scrX,scrY;
	int cx,cy;
	int endX,endY;
	int i;
	WINDOW *my_win;
/*
	NODE *now_node;

	token_list_head=NULL;
	token_list_end=NULL;
	node_list_end=NULL;
	node_list_head=NULL;
	printf("create token list\n");
	create_TOKEN();
	printf("create node list\n");
	create_NODE();
	//printf("parsing\n");
	//parsing("NEW YORK");
	//printf("parsing end\n");
	getc(stdin);
	*/
	initscr();
	getmaxyx(stdscr,scrY,scrX);
	insert_window_refresh(my_win,scrX,scrY);
	endwin();
	exit(0);
}
