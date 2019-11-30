def createWallet(balance, user):

    def deposite(amount):
        nonlocal balance
        balance = balance+amount
        print("--------------------")
        print(amount, " Amount deposited by " + user)
        print("Total balance " + str(balance))
        print("--------------------")

    def withdraw(amount):
        nonlocal balance
        balance = balance - amount
        print(amount, " Amount withdrawn by " + user)
        print("Total balance " + str(balance))
        print("--------------------")

    def showBalance():
        print("Total balance of " + user + str(balance))

    def fundsTransfer(amount, wallet, name):
        nonlocal balance
        balance = balance - amount
        print(amount, " is transferred to " + name)
        wallet[0](amount)
        print("--------------------")

    return [deposite, withdraw, showBalance, fundsTransfer]


w1 = createWallet(43000, " Ashmit ")
w2 = createWallet(50000, " Anand ")

w1[0](1000)
w1[1](500)
w1[2]()
