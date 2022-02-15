# bank.py
from account import Account;

# acc1 Object
acc1 = Account('11112222', 1000, "James");
# print(acc1);
# acc1.deposite(23000);
# print(acc1.inquire());
# print(acc1);
# acc1.balance = -1000;
try:
    acc1.widthdraw(10000);
    print(acc1);
except:
    print("잔액부족");
print(acc1);

#이름좀 바꿔줘
acc1.setowner('kim')
print(acc1);
#계좌번호와 고객이름만 출력
print('계좌:%s, 이름:%s' % (acc1.accno, acc1.owner));