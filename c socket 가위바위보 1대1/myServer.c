#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "time.h"
#include "sys/types.h"
#include "sys/socket.h"
#include "netinet/in.h"
#include <unistd.h>
//소켓 프로그래밍에 사용될 헤더파일 선언
 
#define BUF_LEN 1024
//메시지 송수신에 사용될 버퍼 크기를 선언

typedef struct socketInfo
{
    struct sockaddr_in client_addr;
    int client_fd;
    char buffer[BUF_LEN];
}socketInfo;                 //클라이언트 정보 구조체

socketInfo client;   //클라이언트 정보
  


//서버의 흐름은 다음과 같습니다.

// 소켓생성 ->서버 정보 초기화 -> 바인딩 ->리슨설정 -> 엑셉트(연결대기)  -> 통신

//본 소스에서는 연결대기를 3번하여 클라이언트를 3명 받을 때까지 게임이 시작되지 않도록 하였습니다.

//3명이 연결되면 게임이 시작됩니다.
int main(int argc, char *argv[])
{
    struct sockaddr_in server_addr;
    int server_fd;
    int number;

    char buffer[BUF_LEN];
    char temp[20];
    //server_fd, client_fd : 각 소켓 번호
    int len, msg_size;
    int i,j;

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
    printf("Server : wating connection request.\n");
    len = sizeof(client.client_addr);
    client.client_fd = accept(server_fd, (struct sockaddr *)&client.client_addr, &len);   //연결대기합니다.
    if(client.client_fd < 0)
    {
        printf("Server: accept failed.\n");
        exit(0);
    }
    inet_ntop(AF_INET, &client.client_addr.sin_addr.s_addr, temp, sizeof(temp));  
//클라이언트의 아이피를 char 배열값으로 변경해줍니다. 이 함수를 이용하지 않으면 client[i].client_addr.sin_addr.s_addr에 들어있는 값은 int 값으로 되어 있어 ip값이 어떤값인지 알기 어렵습니다.
    printf("Server : %s client connected.\n", temp);


    while(1)
    {
        read(client.client_fd,client.buffer,BUF_LEN);
        number=client.buffer[0];
        srand(time(NULL));

        number=rand()%3;
        client.buffer[0]=number;
        client.buffer[1]='\0';
        write(client.client_fd,client.buffer,BUF_LEN);
    }



    close(server_fd);
    return 0;
}
