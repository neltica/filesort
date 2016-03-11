#include <Adafruit_VC0706.h>
#include <SD.h>
#include <SoftwareSerial.h>   
#include <SPI.h>      //문제될시에 빼주세요. 제꺼에서는 없으면 안되드라구요
#define chipSelect 10
#if ARDUINO >= 100


  SoftwareSerial BTSerial(0,1);   //0,1
  SoftwareSerial cameraconnection = SoftwareSerial(2,3);//2,3

#else
NewSoftSerial cameraconnection = NewSoftSerial(2,3);  //2,3
#endif

Adafruit_VC0706 cam = Adafruit_VC0706(&cameraconnection);

  int pushButton = 7;
  int buttonStatePrevious = LOW;
  int buttonStateCurrent = LOW;




void setup() 
  {
    #if !defined(SOFTWARE_SPI)
      #if defined(__AVR_ATmega1280__) || defined(__AVR_ATmega2560__)
        if(chipSelect != 53) pinMode(53, OUTPUT); // SS on Mega
       #else
        if(chipSelect != 10) pinMode(10, OUTPUT); // SS on Uno, etc.
       #endif
      #endif
    //Serial.begin(115200);
    BTSerial.begin(115200);  //115200
    
    pinMode(8, OUTPUT);
    
    pinMode(pushButton, INPUT);

  
    if (!SD.begin(chipSelect)) {

    return;
    }  
  }

void loop() 
  {
    
    buttonStateCurrent = digitalRead(pushButton);
    if(buttonStateCurrent != buttonStatePrevious)
    {

    if (cam.begin()) {

    }
    else {
     
    return;
    }

    char *reply = cam.getVersion();
      if (reply == 0) {
    }
    else {
    }
          
     cam.setImageSize(VC0706_640x480);        // biggest
    //cam.setImageSize(VC0706_320x240);        // medium
    //cam.setImageSize(VC0706_160x120);          // small

    uint8_t imgsize = cam.getImageSize();
    if (imgsize == VC0706_640x480) //Serial.println("640x480");
    if (imgsize == VC0706_320x240) //Serial.println("320x240");
    if (imgsize == VC0706_160x120) //Serial.println("160x120");


    delay(3000); 

    if (! cam.takePicture()) {
 
    }
    else {

    }
  
    char filename[13];
    strcpy(filename, "IMAGE00.jpg");
    for (int i = 0; i < 100; i++) {
      filename[5] = '0' + i/10;
      filename[6] = '0' + i%10;
      if (! SD.exists(filename)) {
        break;
      }
      else
      {

        }
    }

    //Serial.println(filename);
    File imgFile = SD.open(filename, FILE_WRITE);

    uint16_t jpglen = cam.frameLength();
  
    byte wCount = 0; // For counting # of writes


    ///////////////////////////////////////
    //파일이름전송  끝은 null
    ///////////////////////////////////////
    for(int i=0;i<13;i++)
    {
        BTSerial.write(filename[i]);
        
        if(filename[i]==NULL)
       {
          break;
         }
      }
    ///////////////////////////////////////

    
    ///////////////////////////////////////
    // 사이즈 전송
    ///////////////////////////////////////
    uint16_t jpglen4Send=jpglen;
    while(1)
    {
     if(jpglen4Send==0)
      {
        BTSerial.write('\n');
       break;
       }
      BTSerial.write(jpglen4Send%10);
      jpglen4Send/=10;
      }
    ///////////////////////////////////////

    
    while (jpglen > 0) {
       //read 32 bytes at a time;
      uint8_t *buffer;
      uint8_t bytesToRead = min(32, jpglen); // change 32 to 64 for a speedup but may not work with all setups!
      buffer = cam.readPicture(bytesToRead);
      imgFile.write(buffer, bytesToRead);

      //////////////////////////////////////////
      //버퍼 전송
      //////////////////////////////////////////
      
      for(int i=0;i<bytesToRead;i++)
      {
        BTSerial.write(buffer[i]);
        //BTSerial.read();
        }
      //////////////////////////////////////////
      jpglen -= bytesToRead;
      BTSerial.flush();
      }
      
      imgFile.close();
            
      }
  }


  
