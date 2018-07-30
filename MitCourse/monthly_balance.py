# Test Case 1:
# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

def mir(rate):
    return rate/12
def mmp(rate, balance):
    return rate * balance
def mub(prev, mmp):
    return prev - mmp
def ubem(mub, mir, mmp):
    return mub + (mir * mmp)
def mplb(balance):
    return balance/12
def mpub(balance,rate):
    return (balance * (1 + mir(rate))**12)/12

#Problem 1
# for i in range(0,12):
#     balance = (ubem(mub(balance, mmp(monthlyPaymentRate, balance)), mir(annualInterestRate), mub(balance, mmp(monthlyPaymentRate, balance))))
# print(round(balance,2))


#Problem 2

# # Test
# # Case
# # 1:
# balance = 3329
# annualInterestRate = 0.2
# #
# # Result
# # Your
# # Code
# # Should
# # Generate:
# # -------------------
# # Lowest
# # Payment: 310
#
#
# saveBalance = balance
# init = 0
#
# while True:
#     for i in range(0, 12):
#         balance = ubem(mub(balance, init), mir(annualInterestRate), mub(balance, init))
#     if balance < 0:
#         break
#     else:
#         init += 10
#         balance = saveBalance
# print('Lowest Payment: ' + str(init))

# Problem 3

# Test Case 1:
balance = 320000
annualInterestRate = 0.2
#
# 	      Result Your Code Should Generate:
# 	      -------------------
# 	      Lowest Payment: 29157.09
#
lower = balance / 12
upper = (balance * (1 + mir(annualInterestRate))**12)/12
guess = 0
eps = 0.01
saveBalance = balance
while True:
    guess = lower + ((upper - lower) / 2)

    for i in range(0, 12):
        balance = ubem(mub(balance, guess), mir(annualInterestRate), mub(balance, guess))

    if abs(balance) > eps:
        if balance < 0:
            balance = saveBalance
            upper = guess
        elif balance > -1:
            balance = saveBalance
            lower = guess
    elif abs(balance) <= eps:
        break
print('Lowest Payment: ' + str(round(guess, 2)))
