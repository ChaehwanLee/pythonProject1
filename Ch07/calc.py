def calc(n,*data):
    sum = 0;
    for i in data:
        sum += i;
    result = sum / n;
    return result;

def start():
    print('start application')
    while True:
        num = input('Input Num');
        if num == '0':
            break;
        result = calc(int(num),2,4,5,6,7,8);
        print('Result',result)
    print('stop application');

if __name__ == '__main__':
    start();