# 서버에 전송을 하다 예외가 생기는 경우

import random
import time

def sendData(data):
    print('Send Data:', data);

def connect():
    print('Connected Server ... ');

def sendData(data):
    if data == 3:
        raise IOError;
    print('Send Dtat:', data);

def close():
    print('Closed Server');

while True:
    temp = 0;
    temp = random.randint(1, 11);
    try:
        connect();
        sendData(temp);
    except:
        print('Server Error...');
    finally:
        close();
    time.sleep(3);

print('Terminated ...');