#-*- coding: utf-8 -*-
import socket
import cv2
import numpy

class SEP():

    class Convert:
        def cvImgtoStringImg(self,frame):
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            result, imgencode = cv2.imencode('.jpg', frame, encode_param)
            data = numpy.array(imgencode)
            stringData = data.tostring()
            return stringData

        def StringImgtoCvImg(self,stringData):
            data = numpy.fromstring(stringData, dtype='uint8')
            cvimg = cv2.imdecode(data, 1)
            return cvimg


    class start:
        def __init__(self,socket):
            self.convertor = SEP.Convert()
            self.socket = socket
            self.__file = None
            self.socket.settimeout(1)
            self.timeOutFlag = False

        def __del__(self):
            self.socket.close()

        def close(self):
            self.__del__()

        def getFile(self):
            return self.__file

        def recvall(self,count):
            buf = b''
            while count:
                newbuf = self.socket.recv(count)
                if not newbuf: return None
                buf += newbuf
                count -= len(newbuf)
            return buf

        def send(self,file):
            try:
                self.socket.sendall(str(len(file)).ljust(16))
                self.socket.sendall(file)
            except socket.timeout:
                if not self.timeOutFlag:
                    return True
                else:
                    return False
            except Exception as e:
                return False

            return True

        def recv(self):

            try:
                length = self.recvall(16)
                stringData = self.recvall(int(length))
            except socket.timeout:
                if not self.timeOutFlag:
                    return True
                else:
                    return False
            except Exception as e:
                return False

            self.__file = stringData
            return True

        def sendCVframe(self, frame):
            frame = self.convertor.cvImgtoStringImg(frame)
            return self.send(frame)

        def recvCVframe(self):
            if not self.recv():
                return False
            self.convertor.StringImgtoCvImg(self.__file)
            return True
