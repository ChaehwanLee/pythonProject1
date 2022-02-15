# bank.py
from ch153.account import Account, IAccount

# acc1 Object
iacc1 = Account('11112222', 1000, "James",);
print(iacc1)
try:
    iacc1.widthdraw(900);
    print(iacc1);
except:
    print("잔액부족");
interest = iacc1.calcinterest();
print(interest);
print(iacc1.accno+''+iacc1.owner);
print(iacc1.accno+''+iacc1.owner+''+iacc1.getinterest());