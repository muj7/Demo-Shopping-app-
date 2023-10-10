users = {
    "user1": {
        "password": "123456789",
        "cart": [],
        "sessionID": 1,
        "userType": "user"
    },
    "user2": {
        "password": "123456789",
        "cart": [],
        "sessionID": 1,
        "userType": "user"
    },

    "admin1": {
        "password": "123456789",
        "sessionID": 1,
        "userType": "admin"
    }
}

categories = {"1": "footwear", "2": "clothing", "3": "Electronics"}

p1 = {"name": "Boots", "id": 1, "price": 50, "catID": "1"}
p2 = {"name": "Coats", "id": 2, "price": 150, "catID": "2"}
p3 = {"name": "caps", "id": 3, "price": 12, "catID": "2"}
p4 = {"name": "iphone", "id": 4, "price": 1500, "catID": "3"}
products = [p1, p2, p3, p4]

username = ""


# login func for both user and admin
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if users.get(username) is not None:
        if users[username]["password"] == password:
            if users[username]["userType"] == "user":
                # welcome back the user
                print("\nWelcome back", username, "to T5 store!\n")

            else:
                # welcome back the admin
                print("\nWelcome back", username,
                      "to T5 store! You longed in as an admin\n")

            return username
    print("Wrong username or password")
    return None


def signUp():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    repassword = input("Rewrite your password: ")
    if password == repassword:
        users.update({username: {"password": password,
                     "userType": "user", "sessionID": 1, "cart": []}})
        print("\nyou have been signed up successfully")
        print("Welcome", username, "to T5 store!\n")

        return username
    else:

        return None


def logout():
    global username
    username = ""
    print("\nyou have been logged out successfully")
    print("Visit us again soon!\n")
    return None


# View Catalog "the available products and categories in the store" for both user and admin
def viewCatalog():
    print("\nWe have", len(categories), "Categories:")
    for i in categories.keys():
        print(i + ".", categories[i])

    print("\nWe have", len(products), "Products:")

    for i in products:
        print(str(i['id']) + ".", i["name"], "- category:", categories[i["catID"]], ", Price: " + str(i["price"]),
              "SAR.")
    print("-----------\n")


# user functions:
# View the user cart, only user can view it
def viewCart():
    if users[username]["userType"] == "admin":  # type: ignore
        print("you are admin cannot add to the user cart")
        return
    print("Your cart contain", len(
        users[username]["cart"]), "items: ")  # type: ignore
    for i in users[username]["cart"]:  # type: ignore
        print(str(i['id']) + ".", i["name"], "| Category:",
              categories[i["catID"]], ", Price: Rs." + str(i["price"]))


# Add Items to the user's cart (the admin cannot add)
def addItemsToCart():
    if users[username]["userType"] == "admin":  # type: ignore
        print("you are admin cannot add to the user cart")
        return None
    item = None
    itemId = int(input("\nEnter the product id: "))
    for i in products:
        if i["id"] == itemId:
            item = i
            break
    qty = int(input("How many quantity you want to add? "))
    j = qty
    while j != 0:
        users[username]["cart"].append(item)  # type: ignore
        j = j - 1
    print("The items has been add successfully")


# Remove Items to the user's cart (the admin cannot )
def removeItemsFromCart():
    if users[username]["userType"] == "admin":  # type: ignore
        print("you are admin cannot remove to the user cart")
        return
    itemId = int(input("\nEnter the product id: "))
    item = None
    for i in products:
        if i["id"] == itemId:
            item = i
            break
    qty = int(input("How many quantity you want to remove? "))
    j = qty
    while j != 0:
        users[username]["cart"].remove(item)  # type: ignore
        j = j - 1

    print("The items has been removed successfully")


def paymentCheckout():
    # Create a list of demo payment options.
    paymentOptions = ["Net banking", "PayPal", "UPI"]

    # Display the list of payment options to the user.
    print("Please select a payment option:")
    for i in range(len(paymentOptions)):
        print(f"{i + 1}. {paymentOptions[i]}")

    # Allow the user to select a payment option from the list.
    selectedOption = int(input("Your choice: "))

    total = calculateCartPrice(users[username]["cart"])  # type: ignore

    # Display a checkout message that is specific to the selected payment option.
    print("You will be shortly redirected to your", paymentOptions[selectedOption - 1], "to make a payment of ", total,
          "SAR.")
    # Display a success message.
    print("Your payment has been successfully processed.")


def calculateCartPrice(cart):
    totalPrice = 0
    for item in cart:
        totalPrice += item["price"]

    return totalPrice


def userMenu():
    viewCatalog()
    while True:
        choice = int(input(
            "To view your cart enter 1\nTo add items to your cart enter 2\nTo remove items from your cart enter 3\nTo checkout enter 4\nTo logout enter 5\nEnter your choice: "))
        if choice == 1:
            viewCart()
        elif choice == 2:
            addItemsToCart()
        elif choice == 3:
            removeItemsFromCart()
        elif choice == 4:
            paymentCheckout()
        elif choice == 5:
            logout()
            break
        print()


# admin functions:
def addCategory():
    if users[username]["userType"] == "admin":  # type: ignore
        CategoryName = input("Enter CategoryName: ")
        CategoryID = input("Enter ID: ")
        categories.update({CategoryID: CategoryName})
        print("The Category has been added successfully!")
    else:
        print("access denied")


def x(t):
    # remove all products with catID = t
    for i in products:
        if i["catID"] == t:
            print("removed", i, "from products", t)
            products.remove(i)


def removeCategory():
    if users[username]["userType"] == "admin":  # type: ignore
        CategoryID = input("Enter the Category ID: ")
        del categories[CategoryID]
        print("The Category has been removed successfully!")
        x(CategoryID)
    else:
        print("access denied")


def addProductToCatalog():
    # Get the product name, price, and category from the user.
    product_name = input("Enter the product name: ")
    product_id = int(input('Enter the product ID: '))
    product_price = float(input("Enter the product price: "))
    product_category = input("Enter the product category: ")

    # Create a new product dictionary.
    new_product = {
        "name": product_name,
        "id": product_id,
        "price": product_price,
        "catID": product_category,
    }

    # Add the new product to the list of products.
    products.append(new_product)
    print("The product has been added successfully!")


def removeProductFromCatalog():
    # Get the product ID of the product to be removed.
    product_id = int(input("Enter the ID of the product to be removed: "))

    # Find the product in the list of products.
    product_to_remove = None
    for product in products:
        if product["id"] == product_id:
            product_to_remove = product
            break

    # If the product was not found, print an error message.
    if product_to_remove is None:
        print("Product not found.")
        return

    # Remove the product from the list of products.
    products.remove(product_to_remove)
    print("The product has been removed successfully!")


def editProduct():
    # Get the product ID of the product to be edited.
    product_id = int(input("Enter the ID of the product to be edited: "))

    # Find the product in the list of products.
    product_to_edit = None
    for product in products:
        if product["id"] == product_id:
            product_to_edit = product
            break

    # If the product was not found, print an error message and return.
    if product_to_edit is None:
        print("Product not found.")
        return

    # Ask the user what they want to edit (name or price).
    edit_choice = input("What do you want to edit (name or price): ")

    # If the user chooses to edit the name, update the product name.
    if edit_choice == "name":
        updated_product_name = input("Enter the updated product name: ")
        product_to_edit["name"] = updated_product_name

    # If the user chooses to edit the price, update the product price.
    elif edit_choice == "price":
        updated_product_price = float(
            input("Enter the updated product price: "))
        product_to_edit["price"] = updated_product_price

    # Otherwise, print an error message.
    else:
        print("Invalid edit choice.")
        return

    # Print a confirmation message.
    print("Product updated successfully.")


def adminMenu():
    while True:
        choice = int(input(
            "To view the catalog enter 1.\nTo add new category enter 2. \nTo remove category enter 3. \nTo add product to the catalog enter 4.\nTo remove product from the catalog enter 5.\nTo edit product in the catalog enter 6.\nTo add items to the cart enter 7.\nTo remove items from the cart enter 8.\nTo log out enter 9.\nEnter your choice:"))
        print()
        if choice == 1:
            viewCatalog()
        elif choice == 2:
            addCategory()
        elif choice == 3:
            removeCategory()
        elif choice == 4:
            addProductToCatalog()
        elif choice == 5:
            removeProductFromCatalog()
        elif choice == 6:
            editProduct()
        elif choice == 7:
            addItemsToCart()
        elif choice == 8:
            removeItemsFromCart()
        elif choice == 9:
            logout()
            break
        print()


def start():
    global username
    print("""
 █   █ █▀▀ █   █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 ▀▀█▀▀ █  █ █▀▀ 　 ▀▀█▀▀ █▀▀ 　 █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀ 
 █ █ █ █▀▀ █   █   █  █ █ ▀ █ █▀▀ 　   █   █  █ 　   █   █▀▀█ █▀▀ 　   █   ▀▀█ 　 ▀▀▄   █   █  █ █▄▄▀ █▀▀ 
 ▀▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀   ▀ ▀▀▀ 　   ▀   ▀▀▀▀ 　   ▀   ▀  ▀ ▀▀▀ 　   ▀   ▀▀▀ 　 ▀▀▀   ▀   ▀▀▀▀ ▀ ▀▀ ▀▀▀""")
    while True:
        try:
            # welcome to the demo marketplace

            choice = int(
                input("To login enter 1.\nTo sign up enter 2.\nEnter your choice: "))
            if choice == 1:
                username = login()
            elif choice == 2:
                username = signUp()

            if users[username]['userType'] == 'user':  # type: ignore
                userMenu()
            else:
                adminMenu()

        except:
            # somthing went wrong
            print("Something went wrong, try again")


start()
