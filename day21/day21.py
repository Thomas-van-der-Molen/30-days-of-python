#classes and objects

class Statistics():
    def __init__(self, input_list):
        self.data = input_list
        
    def count(self):
        return len(self.data)
    def sum(self):
        return sum(self.data)
    def min(self):
        return min(self.data)
    def max(self):
        return max(self.data)
    def range(self):
        return max(self.data) - min(self.data)
    def mean(self):
        return sum(self.data) / len(self.data)
    def median(self):
        temp = self.data
        temp.sort()
        return temp[len(temp)/2] if len(temp)%2==0 else (temp[len(temp)//2] + temp[1 + len(temp)//2]) / 2





ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29

class personAccount():
    def __init__(self, firstName = "none", lastName = "none", incomes = [], expenses = [], properties = []):
        self.firstName = firstName
        self.lastName = lastName
        self.incomes = incomes
        self.expenses = expenses
        self.properties = properties
    
    def totalIncome(self):
        return sum([income[1] for income in self.incomes])
    def totalExpense(self):
        return sum(expense[1] for expense in self.expenses)
    def accountInfo(self):
        return f'{self.firstName} {self.lastName} incomes{self.incomes} expenses{self.expenses}, properties{self.properties}'
    def addIncome(self, name, quantity):
        self.incomes.append((name, quantity))
    def addExpense(self, name, quantity):
        self.expenses.append((name, quantity))
    def accountBalance(self):
        return self.totalIncome() - self.totalExpense()

tom = personAccount("tom", "vdm")
print(tom.accountInfo())
tom.addIncome("work", 100000)
tom.addIncome("Investments", 1000000)
tom.addIncome("time", 1000000000000)
tom.addExpense("apartment", 10)
tom.addExpense("transportation", 20)
tom.addExpense("gym", 5)
tom.addExpense("school",10000)
print(tom.accountInfo())
print(tom.totalIncome())
print(tom.totalExpense())
print(tom.accountBalance())