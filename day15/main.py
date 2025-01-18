# Coffee Machine Project
# This project simulates a coffee vending machine, allowing users to purchase drinks, check resources, and make payments.

# Initialize coffee machine resources and drink recipes
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initial resources available in the coffee machine
resources = {
    "water": 300,  # ml
    "milk": 200,  # ml
    "coffee": 100,  # g
    "money": 0  # dollars
}

# Function to print a report of the current resources in the machine
def print_report():
    """Prints the current status of coffee machine resources"""
    print("\n=== MACHINE STATUS ===")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    print("====================\n")

# Function to display the drink menu and prices
def display_menu():
    """Displays the menu with drink options and prices"""
    print("\n=== MENU ===")
    for drink, details in MENU.items():
        print(f"{drink.capitalize()}: ${details['cost']:.2f}")
    print("===========\n")

# Function to check if there are sufficient resources to make the chosen drink
def check_resources(drink_ingredients):
    """
    Check if there are enough resources to make the drink.
    Returns True if enough resources, otherwise False.
    """
    for item, amount in drink_ingredients.items():
        if resources[item] < amount:
            print(f"\nSorry, there is not enough {item}.")
            return False
    return True

# Function to process quick payment by collecting all coins at once
def quick_payment(drink_cost):
    """
    Process all coins at once for faster payment.
    Returns the total amount inserted by the user or None if invalid.
    """
    print(f"\nThe cost is ${drink_cost:.2f}")
    print("Please insert all coins at once:")

    try:
        quarters = int(input("Number of quarters ($0.25): "))
        dimes = int(input("Number of dimes ($0.10): "))
        nickles = int(input("Number of nickles ($0.05): "))
        pennies = int(input("Number of pennies ($0.01): "))

        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        return round(total, 2)
    except ValueError:
        print("Please enter valid numbers.")
        return None

# Function to process coin insertion individually
def process_coins_individually(drink_cost):
    """
    Prompt user for coins and calculate total value one by one.
    Returns the total amount inserted by the user or None if canceled.
    """
    print(f"\nThe cost is ${drink_cost:.2f}")
    print("Please insert coins:")
    print("(Quarters = $0.25, Dimes = $0.10, Nickles = $0.05, Pennies = $0.01)")

    total = 0
    while total < drink_cost:
        remaining = drink_cost - total
        print(f"\nAmount still needed: ${remaining:.2f}")
        print(f"Current amount inserted: ${total:.2f}")

        coin_type = input("\nInsert coin (quarter/dime/nickel/penny) or type 'cancel' to refund: ").lower()

        if coin_type == 'cancel':
            if total > 0:
                print(f"\nRefunding ${total:.2f}")
            return None

        coin_values = {
            'quarter': 0.25,
            'dime': 0.10,
            'nickel': 0.05,
            'penny': 0.01
        }

        if coin_type not in coin_values:
            print("Invalid coin type. Please try again.")
            continue

        try:
            count = int(input(f"How many {coin_type}s?: "))
            if count < 0:
                print("Please enter a valid number.")
                continue
            total += coin_values[coin_type] * count
        except ValueError:
            print("Please enter a valid number.")

    return round(total, 2)

# Function to prepare the coffee and deduct resources
def make_coffee(drink_name, drink_ingredients):
    """
    Deduct the required ingredients from the resources to make the drink.
    Displays a success message after preparation.
    """
    for item, amount in drink_ingredients.items():
        resources[item] -= amount
    print(f"\n☕ Here is your {drink_name}. Enjoy! ☕")

# Function to handle the payment process
def process_payment(drink_cost):
    """
    Handle payment method selection and process payment.
    Returns the total payment amount or None if canceled.
    """
    while True:
        payment_method = input(
            "\nChoose payment method:\n1. Quick payment (all coins at once)\n2. Individual coins\nEnter (1 or 2): ")

        if payment_method == "1":
            return quick_payment(drink_cost)
        elif payment_method == "2":
            return process_coins_individually(drink_cost)
        else:
            print("Invalid selection. Please choose 1 or 2.")

# Main function that runs the coffee machine
def coffee_machine():
    """
    Main function to run the coffee machine program.
    Handles user inputs, drink preparation, and resource management.
    """
    print("Welcome to the Coffee Machine!")
    machine_on = True

    while machine_on:
        display_menu()
        choice = input("What would you like? (espresso/latte/cappuccino) or type 'off' for maintenance: ").lower()

        if choice == "off":
            print("\nShutting down for maintenance. Goodbye!")
            machine_on = False
            continue

        if choice == "report":
            print_report()
            continue

        if choice not in MENU:
            print("\nInvalid selection. Please choose from the menu.")
            continue

        drink = MENU[choice]

        if not check_resources(drink["ingredients"]):
            continue

        payment = process_payment(drink["cost"])

        if payment is None:  # User canceled or invalid input
            continue

        if payment < drink["cost"]:
            print(f"\nSorry that's not enough money. ${payment:.2f} refunded.")
            continue

        if payment >= drink["cost"]:
            change = round(payment - drink["cost"], 2)
            if change > 0:
                print(f"\nHere is ${change:.2f} in change.")

            resources["money"] += drink["cost"]
            make_coffee(choice, drink["ingredients"])

        print("\nThank you for using our coffee machine!")


# Start the coffee machine program
if __name__ == "__main__":
    coffee_machine()
