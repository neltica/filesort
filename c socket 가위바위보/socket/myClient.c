#include "stdio.h"
#include "sys/types.h"
#include "sys/socket.h"
#include "netinet/in.h"
#include <unistd.h>
#include <time.h>


#include <stdlib.h>
#include <string.h>
#include <sys/select.h>
#include <termios.h>

#define BUF_LEN 1024


static struct termios initial_settings, new_settings;
 
static int peek_character = -1;


int _kbhit()
{
    unsigned char ch;
    int nread;
 
    if (peek_character != -1) return 1;
    new_settings.c_cc[VMIN]=0;
    tcsetattr(0, TCSANOW, &new_settings);
    nread = read(0,&ch,1);
    new_settings.c_cc[VMIN]=1;
    tcsetattr(0, TCSANOW, &new_settings);
    if(nread == 1)
    {
        peek_character = ch;
        return 1;
    }
    return 0;
}
 
void main(int argc, char *argv[])
{
        int i;
        int s, n;
        char *haddr;
        struct sockaddr_in server_addr;
        //struct sockaddr_in server_addr : 서버의 소켓주소 구조체
        char buf[BUF_LEN+1];

        int playerSize;
        char action;
        time_t startTimer;
 
        if(argc != 3)
        {
                printf("usage : %s ip_Address port\n", argv[0]);
                exit(0);
        }
        haddr = argv[1];
 
        if((s = socket(PF_INET, SOCK_STREAM, 0)) < 0)
        {//소켓 생성과 동시에 소켓 생성 유효검사
                printf("can't create socket\n");
                exit(0);
        }
 
        bzero((char *)&server_addr, sizeof(server_addr));
        //서버의 소켓주소 구조체 server_addr을 NULL로 초기화
 
        server_addr.sin_family = AF_INET;
        //주소 체계를 AF_INET 로 선택
        server_addr.sin_addr.s_addr = inet_addr(argv[1]);
        //32비트의 IP주소로 변환
        server_addr.sin_port = htons(atoi(argv[2]));
        //daytime 서비스 포트 번호
 
        if(connect(s, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0)
        {//서버로 연결요청
                printf("can't connect.\n");
                exit(0);
        }
 
     
                read(s, buf, BUF_LEN);
                playerSize=(int)buf[0];
                printf("==========================================================\ntotal player is %d\n==========================================================\n",playerSize+1);
                for(i=0;i<=playerSize;i++)
                {
                        read(s, buf, BUF_LEN);
                        printf("player%d ip:",i+1);
                        printf("%s\n",buf);

                }


                while(1)
                {
                        printf("==========================================================\ngame ready\n==========================================================\n");
                        read(s,buf,BUF_LEN);  
                        printf("%s==========================================================\n",buf);

                        printf("'r':Rock 's':Scissors 'p':Paper\n==========================================================\n");

                        read(s,buf,BUF_LEN);  
                        printf("%s",buf);
                        
                        read(s,buf,BUF_LEN);  
                        printf("%s",buf);
                        
                        read(s,buf,BUF_LEN);  
                        printf("%s==========================================================\nplayer%d:",buf,playerSize+1);

                        /*
                        startTimer=time(NULL);
                        while(1)
                        {
                                
                                if(_kbhit()!=0)
                                {
                                        printf("key hit\n");
                                        action=getchar();
                                }
                                
                                if(time(NULL)-startTimer>2)
                                {
                                        printf("time over\n");
                                        srand(time(NULL));
                                        switch(rand()%3)
                                        {
                                                case 0:
                                                action='r';
                                                break;
                                                case 1:
                                                action='s';
                                                break;
                                                case 2:
                                                action='p';
                                                break;
                                        }
                                        break;
                                }
                        }

                        */

                        action=getchar();
                        getchar();
                        fflush(stdin);


                        printf("input loop end\n");

                        if(action=='r')
                        {
                                buf[0]='0';
                        }
                        else if(action=='s')
                        {
                                buf[0]='1';
                        }
                        else if(action=='p')
                        {
                                buf[0]='2';
                        }

                        write(s,buf,BUF_LEN);
                        printf("action send\n");

                        read(s,buf,BUF_LEN);
                        printf("%s\n==========================================================\n",buf);
                        read(s,buf,BUF_LEN);
                        printf("%s\n==========================================================\nround end\n==========================================================\n\n",buf);
                }
 
        close(s);
        //사용이 완료된 소켓을 닫기
}