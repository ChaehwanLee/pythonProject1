# account.py

# Class, 구현이 어려웠던 개념들을 현실에 그대로 옮길 수 있게 되었다.
# 1. 속성
# 2. 행위

# Account Class
# 1. 속성 : accno, balance, owner
# 2. 행위 : deposit, widthdraw, inquire
# UML(Unified Modeling Language) / db, modeling 을 잘하는 사람 but 둘 다 잘해야한다.
from ch153.bank import interest


class Account():
    # Constructor 생성, 역할을 초기화 시켜주는 것
    def __init__(self, accno, balance, owner):
        self.__accno = accno;
        if balance <= 0:
            self.__balance = 0;
        else:
            self.__balance = balance;
        self.__owner = owner;

    # def setowner(self, owner):  # getter 와 setter
    #     self.__owner = owner;

    @property
    def owner(self):
        return self.__owner;

    @owner.setter
    def owner(self, owner):
        self.__owner = owner;

    @property  # 규칙이 있도록 만드는 것
    def accno(self):
        return self.__accno;

    def deposite(self, money):
        self.__balance += money;

    def widthdraw(self, money):  # 잘못됐을 때
        if (money <= 0) or (money > self.__balance):
            raise Exception;
            return;
        self.__balance -= money;

    def inquire(self):
        return self.__balance;

    def __str__(self):
        return self.__accno + ":" + str(self.__balance) + ':' + self.__owner;


# IAccount
# 1. 속성 : accno, balance, name, interest
# 2. 행위 : deposite, widthdraw, inquire, calcinterest

# 3. Inheritance (상속)

# class IAccount(Account):
#     def __init__(self, accno, balance, name, interest):  # 속성정보세팅
#         super().__init__(accno, balance, name);
#         self.__interest = interest;
#
#     def __str__(self):  # 이자까지 표현
#         return super().__str__() + ' ' + str(self.__interest);  # float값이다
#
#     def calcinterest(self):  # 이자값 연산
#         return super().inquire() * (self.__interest / 100);
#
#     def getinterest(self):
#         return self.__interest;
#
#     def setinterest(self, interest):
#         self.__interest = interest;

class IAccount(Account):
    def __init__(self, accno, balance, name, interest):
        super().__init__(accno, balance, name);
        self.__interest = interest;

    def __str__(self):
        return super().__str__() + ' ' + str(self.__interest);

    def calcinterest(self):
        return super().inquire() * (self.__interest / 100);

    def getinterest(self):
        return self.__interest;

    def setinterest(self):
        return self.__interest = interest;
