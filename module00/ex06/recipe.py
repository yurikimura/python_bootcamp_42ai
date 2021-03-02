cookbook = {'cake': {'ingr': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'time': 60},
            'sandwich': {'ingr': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'time': 10},
            'Salad': {'ingr': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'time': 15}
            }


def add_recipe(key: str):
    # put ingredient
    ingr = []
    count = 1
    elem = ""
    while True:
        elem = input(f"Put ingredient{count} or 'quit' to exit: ")
        if "quit" in elem:
            break
        else:
            ingr.append(elem)
            count += 1

    # put meal
    meal = input("meal (type of meal): ")

    # put prep_time
    try:
        time = int(input("prep_time (preparation time in minutes): "))
    except:
        print("prep_time must be integer.\n")
        time = int(input("prep_time (preparation time in minutes): "))
    cookbook[key] = {'ingr': ingr, 'meal': meal, 'time': time}

    print(f"the recipe of '{key}' have been uploaded.")
    print("")
    return


def del_recipe(key: str):
    try:
        removed_value = cookbook.pop(key)
        print(f"\n{key} have been deleted from cook book.")
    except:
        print(f"\n{key} have NOT been deleted. Please try again.")
    print("")
    return


def print_recipe(key: str):
    try:
        print(f"\n{key}\n"
              + f"Ingredients list: {cookbook[key]['ingr']}\n"
                + f"To be eaten for {cookbook[key]['meal']}\n"
                + f"Takes {cookbook[key]['time']} minutes of cooking.")
    except:
        print(f"\n{key} was not found")
    print("")
    return


def print_cookbook():
    for i in cookbook:
        print(f"\n{i}\n"
              + f"Ingredients list: {cookbook[i]['ingr']}\n"
                + f"To be eaten for {cookbook[i]['meal']}\n"
                + f"Takes {cookbook[i]['time']} minutes of cooking.")
    print("")


def main():
    while True:
        command = input(
            "Please select an option by typing the corresponding number:\n"
            + "1: Add a recipe\n"
            + "2: Delete a recipe\n"
            + "3: Print a recipe\n"
            + "4: Print the cookbook\n"
            + "5: Quit\n"
            + ">> "
        )

        if command == "1":
            key = input("What to meke: ")
            add_recipe(key)

        elif command == "2":
            key = input("Please enter the recipe's name to get its Delete: ")
            del_recipe(key)

        elif command == "3":
            key = input("Please enter the recipe's name to get its details: ")
            print_recipe(key)

        elif command == "4":
            print_cookbook()

        elif command == "5":
            print("\nCookbook closed.")
            break

        else:
            print("\nThis option does not exist, please type the corresponding number.\n"
                  + "To exit, enter 5.\n")


if __name__ == "__main__":
    main()
