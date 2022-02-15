
from ch153.account import Account

accs = [];
accs.append(Account('111',1000,'lee'));
accs.append(Account('222',2000,'kim'));
accs.append(Account('333',3000,'han'));

for acc in accs:
    print('계좌번호: %s, 계좌주 : %s, 잔액: %d' % (acc.accno, acc.owner, acc.inquire()));