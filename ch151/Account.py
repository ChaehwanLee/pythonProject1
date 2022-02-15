# account.py

# Class
# 1. 속성
# 2. 행위

# Account Class
# 1. 속성 : balance
# 2. 행위 : deposit, widthdraw

class Account():
    # Constructor 생성, 역할을 초기화 시켜주는 것
    def __init__(self, balance):
        self.balance = balance;
    def deposite(self, money):
        self.balance += money;
    def widthdraw(self, money):
        self.balance -= money;
    def inquire(self):
        return self.balance;
    def __str__(self):
        return str(self.balance);