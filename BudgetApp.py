class Category:
    def __init__(self, name):
        self.ledger = []
        self.balance = 0
        self.name = name
        
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def get_percentage(self):
        total = 0
        for item in self.ledger:
            if item["amount"] > 0:
                total += item["amount"]

        withdrawn = total - self.get_balance()

        percentage = withdrawn * 100 / total

        return percentage

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": f"Transfer to {budget_category.name}"})
            budget_category.ledger.append({"amount": amount, "description": f"Transfer from {self.name}"})
            self.balance -= amount
            budget_category.balance += amount
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        bar_chart = f'{self.name:*^30}' + "\n"
        items = ""

        for item in self.ledger:
            items += f'{item["description"][0:23]:23}' + f'{item["amount"]:>7.2f}' + "\n"
        
        total = f'Total: {self.get_balance()}'

        return bar_chart + items + total

def create_spend_chart(categories):
    bar_chart = "Percentage spent by category\n"
    percentage = {}
    name_length = 0

    for item in categories:
        percentage[item.name] = item.get_percentage()

    x = 100
    for number in range(11):
        row = f"{x}".rjust(3) + "| "
        for name, percent in percentage.items():
            if percent >= (x):
                row += "o  "
            else:
                row += "   "
        bar_chart += row + '\n'
        x -= 10

    bar_chart += "    -"
    for category in categories:
        bar_chart += "---"
    bar_chart += "\n"

    for category in categories:
        if len(category.name) > name_length:
            name_length = len(category.name)
    
    y = 0
    while y <= name_length:
        rows = "     "
        for key, value in percentage.items():
            category_name = key
            try:    
                rows +=  category_name[y] + "  "
            except: 
                rows += "   "
        
        if y <= name_length -1:
            bar_chart += rows + '\n' 
        else:
            bar_chart += rows.strip(" ")
           
        y = y + 1
    bar_chart = bar_chart.rstrip("\n")

    return bar_chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))