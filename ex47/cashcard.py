balance_won = 0

def deposit(amount_won):
    global balance_won
    balance_won += amount_won

def withdraw(amount_won):
    global blance_won
    blance_won += (-amount_won)

def check_balance():
    return balance_won


