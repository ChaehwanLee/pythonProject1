# bank.py
from Account import Account;

# acc1 Object
acc1 = Account(1000);
print(acc1);
print(acc1.inquire());
acc1.deposite(15000);
print(acc1)

#acc2 Object
acc2 = Account(2000);
print(acc2);