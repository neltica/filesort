#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "time.h"
#include "sys/types.h"
#include "sys/socket.h"
#include "netinet/in.h"
#include <unistd.h>
#include <pthread.h>
//소켓 프로그래밍에 사용될 헤더파일 선언
 
#define BUF_LEN 1024
//메시지 송수신에 사용될 버퍼 크기를 선언

typedef struct socketInfo
{
    struct sockaddr_in client_addr;
    int client_fd;
    int rank;
    pthread_t p_thread;
    char buffer[BUF_LEN];
}socketInfo;

socketInfo client[3];

int table[3]={0,};

int tN0=0,tN1=1,tN2=2;


void *t_function(void *data)
{
    int num=(*(int*)data);
    int flag;
    
    printf("%d thread recv ready\n",num);
    read(client[num].client_fd,client[num].buffer,1024);
    
    flag=atoi(client[num].buffer);
    switch(flag)
    {
        case 0:
            table[0]+=1;
        break;
        case 1:
            table[1]+=1;
        break;
        case 2:
            table[2]+=1;
        break;
    }
    printf("==========================================================\n");
    printf("client%d recv success\n",num);
    printf("player%d:",num);
    switch(flag)
    {
        case 0:
        printf("ROCK\n");
        break;
        case 1:
        printf("SCISSORS\n");
        break;
        case 2:
        printf("PAPER\n");
        break;
    }
    printf("==========================================================\n");
    
    
    
}

int whoiswinner()
{
    int i;
    int count=0;
    int p1=0,p2=0;
    int flag;
    int rp1=0,rp2=0;

    printf("0:%d 1:%d 2:%d\n",table[0],table[1],table[2]);

    for(i=0;i<3;i++)
    {
        if(table[i]==2)
        {
            p2=i;
        }
        else if(table[i]==1)
        {
            p1=i;
        }
    }

    if(table[p2]==2)
    {
        if(p2==0 && p1==1)
        {
            rp2=1;
            for(i=0;i<3;i++)
            {
                if((flag=atoi(client[i].buffer))==p2)
                {
                    client[i].rank+=1;
                }
            }
        }
        else if(p2==0 && p1==2)
        {
            rp1=1;
            for(i=0;i<3;i++)
            {
                if((flag=atoi(client[i].buffer))==p1)
                {
                    client[i].rank+=1;
                }
            }
        }
        else if(p2==1 && p1==0)
        {
            rp1=1;
            for(i=0;i<3;i++)
            {
                if((flag=atoi(client[i].buffer))==p1)
                {
                    client[i].rank+=1;
                }
            }

        }
        else if(p2==1 && p1==2)
        {
            rp2=1;
            for(i=0;i<3;i++)
            {
                if((flag=atoi(client[i].buffer))==p2)
                {
                    client[i].rank+=1;
                }
            }
        }
        else if(p2==2 && p1==0)
        {
            rp2=1;
            for(i=0;i<3;i++)
            {
                if((flag=atoi(client[i].buffer))==p2)
                {
                    client[i].rank+=1;
                }
            }
        }
        else if(p2==2 && p1==1)
        {
            rp1=1;
            for(i=0;i<3;i++)
            {
                if((flag=atoi(client[i].buffer))==p1)
                {
                    client[i].rank+=1;
                }
            }
        }
        if(rp1==1)
        {
            return 1;
        }
        else if(rp2==1)
        {
            return 2;
        }
    }
    else
    {
        return -1;
    }
}

 
int main(int argc, char *argv[])
{
    struct sockaddr_in server_addr;
    int server_fd;

    int thr_id;
    int tempRSP;

    char buffer[BUF_LEN];
    char temp[20];
    //server_fd, client_fd : 각 소켓 번호
    int len, msg_size;
    int i,j;
    int status;
    int winner=0;
    int winnerFlag=0;

    if(argc != 2)
    {
            printf("usage : %s port\n", argv[0]);
            exit(0);
    }
        
 
    if((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    {// 소켓 생성
        printf("Server : Can't open stream socket\n");
        exit(0);
    }
    memset(&server_addr, 0x00, sizeof(server_addr));
    //server_Addr 을 NULL로 초기화
 
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    server_addr.sin_port = htons(atoi(argv[1]));
    //server_addr 셋팅
 
    if(bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) <0)
    {//bind() 호출
        printf("Server : Can't bind local address.\n");
        exit(0);
    }
 
    if(listen(server_fd, 5) < 0)
    {//소켓을 수동 대기모드로 설정
        printf("Server : Can't listening connect.\n");
        exit(0);
    }
 
    memset(buffer, 0x00, sizeof(buffer));
    for(i=0;i<3;i++)
    {
        printf("Server : wating connection request.\n");
        len = sizeof(client[i].client_addr);
        client[i].client_fd = accept(server_fd, (struct sockaddr *)&client[i].client_addr, &len);
        if(client[i].client_fd < 0)
        {
            printf("Server: accept failed.\n");
            exit(0);
        }
        inet_ntop(AF_INET, &client[i].client_addr.sin_addr.s_addr, temp, sizeof(temp));  //client ip into temp
        printf("Server : %s client connected.\n", temp);


        //client member transfer start

        printf("start client Info transfer\n");

        buffer[0]=i;
        write(client[i].client_fd,buffer,1024);  //size transfer

        for(j=0;j<=i;j++)
        {
            inet_ntop(AF_INET, &client[j].client_addr.sin_addr.s_addr, temp, sizeof(temp));  //client ip into temp
            strcpy(buffer,temp);
            write(client[i].client_fd,buffer,1024);
        }
        //client member transfer end
        printf("end client Info transfer\n");
    }

    while(1)
    {
        for(i=0;i<3;i++)
        {
            if(client[i].rank>=20)
            {
                printf("winner is player%d.\n",i);
                winnerFlag=1;
            }
        }
        if(winnerFlag)
        {
            exit(0);
        }

        sprintf(buffer,"game start\nplayer Rank\nplayer1:%d\nplayer2:%d\nplayer3:%d\n",client[0].rank,client[1].rank,client[2].rank);
        for(i=0;i<3;i++)
        {
            write(client[i].client_fd,buffer,1024);
        }

        printf("==========================================================\ngame start\n");
        sleep(3);
        printf("ROCK\n");
        sprintf(buffer,"Rock ");
        for(i=0;i<3;i++)
        {
            write(client[i].client_fd,buffer,1024);
        }
        sleep(1);

        printf("SCISSORS\n");
        sprintf(buffer,"Scissors ");
        for(i=0;i<3;i++)
        {
            write(client[i].client_fd,buffer,1024);
        }
        sleep(1);

        printf("PAPER\n");
        sprintf(buffer,"Paper\n");
        for(i=0;i<3;i++)
        {
            write(client[i].client_fd,buffer,1024);
        }
        sleep(1);

        printf("==========================================================\nrecv\n");

        
            printf("%d thread create\n",0);
            thr_id = pthread_create(&client[0].p_thread, NULL, t_function, (void *)&tN0);
            if (thr_id < 0)
            {
                perror("thread create error : ");
                exit(0);
            }

            printf("%d thread create\n",1);
            thr_id = pthread_create(&client[1].p_thread, NULL, t_function, (void *)&tN1);
            if (thr_id < 0)
            {
                perror("thread create error : ");
                exit(0);
            }

            printf("%d thread create\n==========================================================\n",2);

            thr_id = pthread_create(&client[2].p_thread, NULL, t_function, (void *)&tN2);
            if (thr_id < 0)
            {
                perror("thread create error : ");
                exit(0);
            }
        

    
        pthread_join(client[0].p_thread, (void **)&status);
        printf("thread%d end\n==========================================================\n",0);
        pthread_join(client[1].p_thread, (void **)&status);
        printf("thread%d end\n==========================================================\n",1);
        pthread_join(client[2].p_thread, (void **)&status);
        printf("thread%d end\n==========================================================\n",2);
        printf("all success\n==========================================================\n");


        sprintf(buffer,"player1: ");
        switch(atoi(client[0].buffer))
        {
            case 0:
            strcat(buffer,"Rock ");
            break;
            case 1:
            strcat(buffer,"Scissors ");
            break;
            case 2:
            strcat(buffer,"Paper ");
            break;
        }

        strcat(buffer,"player2: ");
        switch(atoi(client[1].buffer))
        {
            case 0:
            strcat(buffer,"Rock ");
            break;
            case 1:
            strcat(buffer,"Scissors ");
            break;
            case 2:
            strcat(buffer,"Paper ");
            break;
        }

        strcat(buffer,"player3: ");
        switch(atoi(client[2].buffer))
        {
            case 0:
            strcat(buffer,"Rock ");
            break;
            case 1:
            strcat(buffer,"Scissors ");
            break;
            case 2:
            strcat(buffer,"Paper ");
            break;
        }

        for(i=0;i<3;i++)
        {
            write(client[i].client_fd,buffer,1024);
        }


        printf("============================================================\nwinner\n");
        if((winner=whoiswinner())!=-1)
        {

            for(i=0;i<3;i++)
            {
                if(table[i]==winner)
                {
                    for(j=0;j<3;j++)
                    {
                        if((tempRSP=atoi(client[j].buffer))==i)
                        {
                            printf("player%d win.\n",j+1);
                            sprintf(buffer,"player%d win.\n",j+1);
                            write(client[j].client_fd,buffer,1024);
                        }
                        else
                        {
                            printf("player%d lose.\n",j+1);
                            sprintf(buffer,"player%d lose.\n",j+1);
                            write(client[j].client_fd,buffer,1024);
                        }
                    }
                    break;
                }
            }
        }
        else
        {
            printf("draw\n");
            for(i=0;i<3;i++)
            {
                sprintf(buffer,"player%d draw.\n",i+1);
                write(client[i].client_fd,buffer,1024);
            }

        }

        printf("============================================================\n");
        for(i=0;i<3;i++)
        {
            table[i]=0;
        }
        printf("round end\n==========================================================\n");
        sleep(5);



    }


    close(server_fd);
    return 0;
}
