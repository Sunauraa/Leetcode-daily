class Bank:

    def __init__(self, balance: List[int]):
        self.m = defaultdict(int)
        for i,x in enumerate(balance):
            self.m[i+1] = x

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in self.m.keys() or account2 not in self.m.keys():
            return False
        if self.m[account1] >= money:
            self.m[account1] -= money
            self.m[account2] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account not in self.m.keys():
            return False
        self.m[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.m.keys():
            return False
        if self.m[account] >= money:
            self.m[account] -=money
            return True
        else:
            return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)