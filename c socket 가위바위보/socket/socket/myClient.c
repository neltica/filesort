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

#define BUF_LEN 1024  //버퍼사이즈입니다.


static struct termios initial_settings, new_settings;  //kbhit 용 변수들입니다.
 
static int peek_character = -1;  //khbit 용 변수들입니다.


int _kbhit()  //리눅스에 kbhit 가 없어서 구현해서 썼습니다.
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



////////////////////////////////////////////////////////////////////////////
/*
클라이언트가 서버로 접속하는 흐름은

소켓생성-> 서버정보 구조체에 대입 -> 커넥트함수호출하여연결 ->통신시작

입니다.

socket
*/
////////////////////////////////////////////////////////////////////////////
 
void main(int argc, char *argv[])
{
        int i;
        int s, n;
        char *haddr;
        struct sockaddr_in server_addr;  //서버관련 정보를 저장하고 있음.
        char buf[BUF_LEN+1];    //send read 용 배열

        int playerSize;   //서버에 현재 몇명이 접속해 있는지를 받아서 저장해놓는 변수
        char action;      //유저가 가위,바위,보를 선택할때 그 상태를 저장함
 
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
 
     
                read(s, buf, BUF_LEN);   //서버에 접속해 있는 클라이언트의 개수를 얻어옵니다.
                playerSize=(int)buf[0];  
                printf("==========================================================\ntotal player is %d\n==========================================================\n",playerSize+1);
                for(i=0;i<=playerSize;i++)   //클라이언트 개수만큼 반복
                {
                        read(s, buf, BUF_LEN);//서버에서 클라이언트들의 정보를 얻어옵니다.
                        printf("player%d ip:",i+1);   
                        printf("%s\n",buf);

                }


                while(1)
                {
                        printf("==========================================================\ngame ready\n==========================================================\n");
                        read(s,buf,BUF_LEN);  //game start를 수신
                        printf("%s==========================================================\n",buf);

                        printf("'r':Rock 's':Scissors 'p':Paper\n==========================================================\n");

                        read(s,buf,BUF_LEN);  //ROCK
                        printf("%s",buf);
                        
                        read(s,buf,BUF_LEN);  //SCISSORS
                        printf("%s",buf);
                        
                        read(s,buf,BUF_LEN);  //PAPER
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

                        action=getchar();   //사용자로 부터 입력을 받습니다.
                        getchar();          //버퍼문제 해결용입니다.
                        fflush(stdin);      //입력버퍼를 비웁니다.


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

                        write(s,buf,BUF_LEN);        //입력값을 서버로 전송합니다,
                        printf("action send\n");

                        read(s,buf,BUF_LEN);        //클라이언트들이 어떤 값을 냈는지 확인합니다.
                        printf("%s\n==========================================================\n",buf);
                        read(s,buf,BUF_LEN);       //누가 이겼는지 받아옵니다.
                        printf("%s\n==========================================================\nround end\n==========================================================\n\n",buf);
                }
 
        close(s);
        //사용이 완료된 소켓을 닫기
}
