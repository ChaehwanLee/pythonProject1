import random
import time

def sendData(data):
    print('Send Data:', data);

while True:
    temp = 0;
    temp = random.randint(1,10);
    if temp == 5: # 온도가 5도면 전송하지 않는다
        break;
    sendData(temp);
    time.sleep(3); # 3s

print('Terminated ...'); # 끝나면 출력