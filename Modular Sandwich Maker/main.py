import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True

    while is_on:
        user_choice = input("What would you like? (small/medium/large/ off/ report): ").strip().lower()

        if user_choice == "off":
            is_on = False
        elif user_choice == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounce(s)")
        elif user_choice in recipes:
            selected_sandwich = recipes[user_choice]
            if sandwich_maker_instance.check_resources(selected_sandwich["ingredients"]):
                inserted_money = cashier_instance.process_coins()
                if cashier_instance.transaction_result(inserted_money, selected_sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(user_choice, selected_sandwich["ingredients"])
        else:
            print("Invalid option selected. Please choose again.")


if __name__ == "__main__":
    main()
