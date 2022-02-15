balance = 0;
def deposit(money):
    global balance;
    balance += money;

def inquire():
    return balance;

balance2 = 0; # 2번째 사람
def deposit2(money):
    global balance2;
    balance2 += money;

def inquire2():
    return balance2;


result = inquire();
print(result)
deposit(1000)
result = inquire();
print(result)

result2 = inquire2()
print(result2)
deposit2(2000)
result2 = inquire2()
print(result2)