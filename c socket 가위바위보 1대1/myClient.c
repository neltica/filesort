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




////////////////////////////////////////////////////////////////////////////
/*
클라이언트가 서버로 접속하는 흐름은

소켓생성-> 서버정보 구조체에 대입 -> 커넥트함수호출하여연결 ->통신시작

입니다.

socket
*/
////////////////////////////////////////////////////////////////////////////

void rspPrint(int number)
{
        switch(number)
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
}
 
void main(int argc, char *argv[])
{
        int i;
        int s;
        int number;
        int c_number;
        char *haddr;
        struct sockaddr_in server_addr;  //서버관련 정보를 저장하고 있음.
        char buf[BUF_LEN+1];    //send read 용 배열
 
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
        
        while(1)
        {
                printf("Rock Scissors Paper\n0: Rock\n1: Scissors\n2: Paper\n-1: end\nselect number:");
                scanf("%d",&number);
		fflush(stdin);

                if(number==-1)
                {
                        close(s);
                        break;
                }

                else if (number<-1 || 2<number)
                {
                        printf("\nrange out\n\n");
                        continue;
                }

                buf[0]=number;
                buf[1]='\0';
                write(s,buf,BUF_LEN);
                printf("====================result====================\n\n");
                read(s,buf,BUF_LEN);
                c_number=buf[0];
                printf("Computer: ");
                rspPrint(c_number);
                printf("User: ");
                rspPrint(number);


                if(number<c_number)
                {
                        if(number==0 && c_number==2)
                        {
                                printf("Computer win\n");
                        }
                        else
                        {
                                printf("User win\n");
                        }
                }
                else if(number==c_number)
                {
                        printf("draw\n");
                }
                else
                {
                        if(number==2 && c_number==0)
                        {
                                printf("User win\n");
                        }
                        else
                        {
                                printf("Computer win\n");
                        }
                }
                printf("==============================================\n\n");
        }

        close(s);
        //사용이 완료된 소켓을 닫기
}
