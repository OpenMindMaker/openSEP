#openSEP
##먼저 openSEP란  
__지속적인 파일전송을 하는도중 대상들의 접속이 끊겼을 경우 양측모두 리턴값으로 확인이 가능하여 예외처리에 용이하다.__

<!-- ##보내는 소켓이 파일 보내는중 사망 -> 배드섹터를 통해 검출
##보내는 소켓이 파일 안전하게 전송후 사망 -> 마지막통신이라는 값을 받는다. timeout사용
**sdkfnjlsd** 굵게
__ㄴㅁㅇ__     굵게
*sadfc*  이텔릭
#제목 제목
***
횡선
sd
\*
한글자
***

송신자 : 수신자  
마지막여부   <-     마지막여부  
play    <-     play  

-->
###객체 생성
###server.py
__서버측 SEP 생성__
```
serv, id = cctvsock.accept()
obj = SEP.start(serv)
```
__스트리밍 코드__
```
def foo():
  while True:
    if not obj.recvCVImg():
      obj.close()
    frame = obj.getFile()
    cv2.imshow("SEP",frame)
```
###client.py
__서버측 SEP 생성__
```
serv, id = cctvsock.accept()
obj = SEP.start(serv)
```
__스트리밍 코드__
```
obj = SEP.start(socket)
def foo():
  while True:
    if not obj.sendCVImg(frame)
      obj.close()
```
