def calcscore(name,*score,**option):
    result = {};

    sum = 0;
    for s in score:
        sum += s;

    result['name'] = name;
    result['sum'] = sum;

    if option['avg'] == True:
        result['avg'] = sum/len(score);

    return result;

def calc(n,*data):
    sum = 0;
    for i in data:
        sum += i;
    result = sum / n;
    return result;

def start():
    # print(result['name']);
    # print(result['sum']);
    # print(result['avg']);
    print('Name:'+result['name']);
    print('Sum:' + str(result['sum']));
    print('Avg:' + str(result['avg']));
    result2 = calc.calc(9,4,5,6,7,8);
    print(result2);


if __name__ == '__main__':
    result = calcscore('kim',90, 80, 99, avg=True);
    start();