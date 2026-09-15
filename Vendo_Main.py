from Vendo_Main import Container

def main():
    containers = {
        1: Container("500 mL Bottle", 10),
        2: Container("1 Liter Bottle", 15),
        3: Container("5 Liter Container", 40),
    }

    print("WATER REFILLING VENDO")
    for choice, container in containers.items():
        print(f"{choice}. {container.name} - P{container.price}")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid selection.")
        return

    if choice not in containers:
        print("Invalid selection.")
        return

    try:
        amount = int(input("Enter payment: "))
    except ValueError:
        print("Invalid payment.")
        return
 
    container = containers[choice]
    container.transaction(amount)
 
 
if __name__ == "__main__":
    main()