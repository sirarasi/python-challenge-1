1# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = [
                {
                    "Item name": "string",
                    "Price": float,
                    "Quantity": int
                },

                {   
                    "Item name": "string",
                    "Price": float,
                    "Quantity": int
                },
] 

order_list = []
#Variable to calculate the number of orders
number_of_orders = 0
# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Type menu item number: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                if int(menu_selection) in menu_items.keys():

                # 4. Check if the menu selection is in the menu items

                    # Store the item name as a variable
                    menu_selection_name = menu_items[int(menu_selection)]
                    # Print out the menu category name they selected
                    print(f"You selected {menu_selection_name}")

                    # Ask the customer for the quantity of the menu item
                    quantity = input("Type the quantity for your selection : ")
                    # Check if the quantity is a number, default to 1 if not
                    #if (quantity.isdigit()) and (int(quantity) > 0):
                    if (quantity.isdigit()):
                        if (int(quantity) < 1):
                            quantity = 1
                            print("Quantity entered is invalid and will default to 1")
                        
                    # Add the item name, price, and quantity to the order list
                        order_list.append(menu_selection_name)
                        order_list[-1]["Quantity"] = int(quantity) 
                        print(order_list)

                    # # Below code personal experimenting with various list_dictionary appends    
                    #      order_list[number_of_orders] = {
                    #           "Item name": menu_selection_name['Item name'],
                    #           "Price": menu_selection_name['Price'],
                    #           "Quantity": int(quantity)
                    #      } 
                    # Below code personal experimenting with various list_dictionary appends 
                    #    order_list.append(menu_selection_name)
                    #    order_list[-1]["Quantity"] = int(quantity) 
                    #    print(order_list)
                    #  for items_append in order_list:
                    #      items_append['Item name'] = menu_selection_name['Item name']
                    #      items_append['Price'] = menu_selection_name['Price']
                    #      items_append['Quantity'] = int(quantity)

                    #    order_list[number_of_orders]['Item name'].append(menu_selection_name['Item name'])
                    #    order_list.append(menu_selection_name['Item name'])
                    #    order_list["Price"].append(menu_selection_name['Price'])
                    #    order_list["Quantity"].append(int(quantity))
                    #    
                    #    order_list['Price'] = menu_items[(menu_selection)]
                    #    order_list[0] = menu_selection_name['Price']
                    #    order_list['Quantity'] = int(quantity)

                    #    

                    #     print(f"Quantity is {quantity}")
                    ##     print(order_list)

                   
                    else:
                        print("Quantity entered is invalid and not a digit")
                                                
                    # Tell the customer that their input isn't valid
                else:
                    # Tell the customer they didn't select a menu option
                    print(f"{menu_selection} was not a menu option.")
            else:
                # Tell the customer they didn't select a number option
                print("You didn't select a number")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        
        match keep_ordering.lower():
            # Customer chose yes
            case 'y':
                # Keep ordering
                place_order = True
                # Exit the keep ordering question loop
                break
            # Customer chose no
            case 'n':
                # Complete the order
                place_order = False
                # Since the customer decided to stop ordering, thank them for their order
                print("Thank you for your order.")
                # Exit the keep ordering question loop
                break
            # Customer typed an invalid input
            case _:
                # Tell the customer to try again
                print("I didn't understand your response. Please try again.")
        
        
                
# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
# print(order_list)

print("Item name                 | Price   | Quantity")
print("--------------------------|---------|----------")

# 6. Loop through the items in the customer's order
for orders in order_list:

    # 7. Store the dictionary items as variables
    item_name = orders["Item name"]
    price = orders["Price"]
    quantity = orders["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    number_of_spaces_print = 24 - len(item_name)

    # 9. Create space strings
    space_strings = " " * number_of_spaces_print

    # 10. Print the item name, price, and quantity
    if orders.values():
     print(f"{item_name} {space_strings} | {price}    | {quantity}")
    

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
#total_price = sum(orders["Price"] for orders in order_list)

total_price = sum(order["Price"] * order["Quantity"] for order in order_list)
print(f"Total Price : ${total_price : ,.2f}")

