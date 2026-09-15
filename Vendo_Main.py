from Vendo_Price import Container


def main():
    containers = {
        1: Container("500 mL Bottle", 10),
        2: Container("1 Liter Bottle", 15),
        3: Container("5 Liter Container", 40),
    }
    print("==============================")


    while True:
        print("--- Water Refilling Vendo ---")
        for choice, container in containers.items():
            print(f"{choice}. {container.name} - P{container.price}")
        print("0. Exit")
        print("==============================")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid selection.")
            continue

        if choice == 0:
            print("Thank you for running!")
            break

        if choice not in containers:
            print("Invalid selection.")
            continue

        try:
            amount = int(input("Enter payment: "))
        except ValueError:
            print("Invalid payment.")
            continue

        container = containers[choice]
        container.transaction(amount)
        print()


if __name__ == "__main__":
    main()