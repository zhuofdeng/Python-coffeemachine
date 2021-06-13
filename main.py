MENU = [
    {
        "name": "espresso",
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    {
        "name": "latte",
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    {
        "name": "cappuccino",
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
]

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
machine_running = True

def checkResources(recipe):
    """Check to make sure the machine has enough resources for the recipe"""
    if recipe['water'] < resources['water'] and recipe['coffee'] < resources['coffee'] and recipe['milk'] < resources['milk']:
        return True
    return False

def printReport():
    print("Water: " + str(resources['water']) + "ml")
    print("milk: " + str(resources['milk']) + "ml")
    print("coffee: " + str(resources['coffee']) + "g")
    print("profit: $" + str(float(profit)))

def requestMoney():
    """Ask the user for coins in USD denomination"""
    print("Please insert coins.")
    quarters = int(input("Please insert Quarters: ")) * 0.25
    dimes = int(input("Please insert Dimes: ")) * 0.10
    nickles = int(input("Please insert Nickles: ")) * 0.5
    pennies = int(input("Please insert Pennies: ")) * 0.01
    return quarters + dimes + nickles + pennies

def calculateChange(money, cost):
    return cost - money

def makeCoffee(recipe, name):
    resources['water'] -= recipe['water']
    resources['coffee'] -= recipe['coffee']
    resources['milk'] -= recipe['milk']
    print("Enjoy your" + name)

while machine_running == True:
    request = input("What would you like? \n 1 (espresso)\n 2 (latte)\n 3 (cappuccino)\n 4 (report)\n 5 (off)\n")
    if request == 5:
        print("Goodbye!")
        machine_running = False
    elif request == 4:
        printReport()
    elif request >= 1 and request <= 3:
        if checkResources(MENU[request-1]['ingredients']):
            total = requestMoney()
            if total >= MENU[request-1]['cost']:
                makeCoffee(MENU[request-1]['ingredients'], MENU[request-1]['name'])
                profit += total
                print("Here is your change: $" + str(calculateChange(total, MENU[request-1]['cost'])))
            else:
                print("Sorry, you didn't pay enough, money refunded...")
        else:
            print("Sorry, we ran out of resources for" + MENU[request-1]['name'])
    else:
        print('Invalid Response, pleae choose from the menu above!')

