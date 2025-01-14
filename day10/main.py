from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "🚫 Error: Division by zero!"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    print("🎉 Welcome to the Python Calculator! 🎉")

    while True:
        num1 = float(input("\n🔢 What is the first number? "))
        should_continue = True

        while should_continue:
            print("\n📜 Available operations:")
            for symbol in operations:
                print(f"  {symbol}")

            operation_symbol = input("\n🧐 Pick an operation: ")
            if operation_symbol not in operations:
                print("⚠️ Invalid operation. Please try again.")
                continue

            num2 = float(input("🔢 What is the next number? "))
            result = operations[operation_symbol](num1, num2)

            print(f"\n💡 {num1} {operation_symbol} {num2} = {result}")

            next_step = input(
                "\n🔁 Type 'y' to continue with this result, 'n' to start fresh, or 'exit' to quit: ").lower()
            if next_step == "y":
                num1 = result
            elif next_step == "n":
                should_continue = False
            elif next_step == "exit":
                print("\n👋 Goodbye! Thanks for using the calculator!")
                return
            else:
                print("⚠️ Invalid input. Exiting calculator.")
                return
calculator()