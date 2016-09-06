# -*- coding: utf8 -*-

import cashcard as cashcard_module

def chk_bal(message, account):
    """
    print message and value
    :param message:
    :param account:
    :return:
    """
    print("%s : %d" % (message, account.check_balance()))

chk_bal("CashCard_moudule 잔액 확인", cashcard_module)

print "10000원 입금"

cashcard_module.deposit(10000)

chk_bal("입금 후 잔고 확인", cashcard_module)

print ("1000원 출금")

cashcard_module.withdraw(1000)

chk_bal("출금 후 잔고 확인", cashcard_module)

import cashcard as mysisterscard_module

chk_bal("cashcard_module 잔액 확인", cashcard_module)
chk_bal("mysistercard_module 잔액 확인", mysisterscard_module)

import cashcard as mysistercard_module

chk_bal("cashcard_module : %s" % cashcard_module)
chk_bal("mysistercard_module : %s" % mysisterscard_module)

class simplecashcard:
    def __init__(self):
        print "simplecashcard __init__()"
        self.balance_won = 0

