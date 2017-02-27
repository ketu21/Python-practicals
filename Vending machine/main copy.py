print("Welcome to the UB vending machine.")
quaters = int(input("Enter the number of quater's you wish to insert:"))
total_amount = float(quaters * 0.25)
amount_left = total_amount
print("You have entered ", total_amount, "dollars")

def drinks_menu():
    global amount_left
    print("--------------------------------------------------")
    print(" Water <$1>")
    print(" Juice <$3>")
    print(" Soda  <$1.5>")
    choice= input("Enter Your drink selection (x to exit)")
    if choice == 'x':
        main_menu()
    elif choice == 'Water':
        if amount_left < 1.0:
            print("You dont have enough money to buy water...")
        else:
            amount_left = amount_left - 1.0
            print("Vending Water.  You have ", amount_left,"left.")
        drinks_menu()
    elif choice== 'Juice':
        if amount_left < 3.0:
            print("You dont have enough money to buy juice...")
        else:
            amount_left = amount_left - 3.0
            print("Vending juice.  You have ", amount_left,"left.")
        drinks_menu()
    elif choice == 'Soda':
        if amount_left < 1.5:
            print("You dont have enough money to buy juice...")
        else:
            amount_left = amount_left - 1.5
            print("Vending juice.  You have ", amount_left,"left.")
        drinks_menu()
    else:
        print("Invalid Selection")
        drinks_menu()
def snacks_menu():
    global amount_left
    print("--------------------------------------------------")
    print(" Chips   <$1.25>")
    print(" Peanuts <$0.75>")
    print(" Cookies <$1>")
    choice= input("Enter Your drink selection (x to exit)")
    if choice == 'x':
        main_menu()
    elif choice == 'Chips':
        if amount_left < 1.25:
            print("You dont have enough money to buy Chips...")
        else:
            amount_left = amount_left - 1.25
            print("Vending Chips.  You have ", amount_left,"left.")
        snacks_menu()
    elif choice== 'Peanuts':
        if amount_left < 0.75:
            print("You dont have enough money to buy Peanuts...")
        else:
            amount_left = amount_left - 0.75
            print("Vending Peanuts.  You have ", amount_left,"left.")
        snacks_menu()
    elif choice == 'Cookies':
        if amount_left < 1:
            print("You dont have enough money to buy Cookies...")
        else:
            amount_left = amount_left - 1
            print("Vending Cookies.  You have ", amount_left,"left.")
        snacks_menu()
    else:
        print("Invalid Selection")
        snacks_menu()
def main_menu():
    print("--------------------------------------------------")
    print("Select Category :")
    print("1. Drinks")
    print("2. Snacks")
    print("3. Exit")
    choice=int(input("Select an option :"))
    if choice == 1:
        drinks_menu()
    elif choice == 2:
        snacks_menu()
    elif choice == 3:
        print("you Inserted $",total_amount," Purchase Amount $",total_amount-amount_left," Change $",amount_left)
        wait=input('Thank You')
        exit
    else:
        print("Enter valid Choice...")
        main_menu()
main_menu()