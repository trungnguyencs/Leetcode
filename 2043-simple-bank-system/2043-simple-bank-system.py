class Bank:

    #This question could be framed as a multithreading problem. For that, see this solution:
    #https://leetcode.com/problems/simple-bank-system/solutions/4824513/python-with-locks-rlock/

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not 1 <= account1 <= len(self.balance) or not 1 <= account2 <= len(self.balance) or self.balance[account1 - 1] < money: return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not 1 <= account <= len(self.balance): return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not 1 <= account <= len(self.balance) or self.balance[account - 1] < money: return False
        self.balance[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)