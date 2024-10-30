print("--------------------- Welcome to GoGreen Store ---------------------")

# Global variables to store user credentials
global password
global username

def auth():
    global password
    global username
    username = input("Enter your User name: ")
    password = input("Please set your password: ")
    conpwd = input("Confirm your password: ")
    
    if conpwd == password:
        print("Please login to the dashboard")
        login()
    else:
        print("Your password has mismatched, please check your password again")
        auth()  # Prompt the user to set the password again

# Login dashboard function
def login():
    attempts = 3  # Set the maximum number of attempts
    while attempts > 0:
        loginpwd = input("Enter your password for the account: ")  # Get user input
        if loginpwd == password:
            dashBoard()
            return 
        else:
            attempts -= 1  # Decrease the number of attempts
            print(f"Your password is incorrect. You have {attempts} attempts left.")
    
    print("You have exceeded the maximum number of attempts.")
    reset_password() 

# Function to reset the password
def reset_password():
    global password
    password = input("Please set a new password: ")
    print("Your password has been reset successfully.")
    login()

# Dashboard function 
def dashBoard():
    print("---------- Welcome back ", username, " ----------")
    print("\n---------- Dashboard Menu ----------")
    print("1. View Products")
    print("2. View Orders")
    print("3. Account Settings")
    print("4. Logout")

    choice = input("Select an option (1-4): ")
    if choice == '1':
        view_Products()
    elif choice == '2':
        view_orders()
    elif choice == '3':
        account_settings()
    elif choice == '4':
        print("You have logged out.")
        return  # Exit the dashboard
    else:
        print("Invalid choice")
        dashBoard()  # Return to the dashboard

def view_Products():
    products = [
        {"id": 1, "name": "Eco-Friendly T-Shirt", "price": 500, "discount": 3},
        {"id": 2, "name": "Biodegradable Phone Case", "price": 200, "discount": 2},
        {"id": 3, "name": "Reusable Water Bottle", "price": 300, "discount": 1},
        {"id": 4, "name": "Organic Cotton Tote Bag", "price": 1200, "discount": 9},
        {"id": 5, "name": "Compostable Trash Bags", "price": 780, "discount": 7}
    ]

    print("\n---------- Available Products ----------")
    print(f"{'ID':<5} {'Name':<30} {'Price (Ksh.)':<15} {'Discount (%)':<15}")
    print("-" * 70)  # Separator line

    for product in products:
        # Calculate the price after discount if any
        discounted_price = product['price'] * (1 - product['discount'] / 100)
        print(f"{product['id']:<5} {product['name']:<30} {discounted_price:<15.2f} {product['discount']}")

    # Allow user to select products
    selected_products = []
    total_cost = 0.0

    while True:
        product_id = input("\nEnter the product ID to add to your cart (or type 'done' to finish): ")
        if product_id.lower() == 'done':
            break

        try:
            product_id = int(product_id)
            product = next((p for p in products if p["id"] == product_id), None)
            if product:
                quantity = input(f"Enter the quantity for {product['name']} (available at {product['price']} Ksh.): ")
                quantity = int(quantity)  # Convert quantity to integer
                if quantity > 0:
                    # Calculate total for the selected product
                    discounted_price = product['price'] * (1 - product['discount'] / 100)
                    total_product_cost = discounted_price * quantity
                    total_cost += total_product_cost
                    selected_products.append({"product": product, "quantity": quantity, "total_cost": total_product_cost})
                    print(f"{quantity} x {product['name']} has been added to your cart. Current total: {total_cost:.2f} Ksh.")
                else:
                    print("Quantity must be greater than zero.")
            else:
                print("Product not found. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid product ID.")

    # Download the receipt
    if selected_products:
        download_receipt(selected_products, total_cost)
    else:
        print("No products selected.")

def download_receipt(selected_products, total_cost):
    print("-"*70,"Receipt","-"*70)
    print(f"{'ID':<5} {'Name':<30} {'Quantity':<10} {'Price (Ksh.)':<15}")
    print("-" * 70)  # Separator line
    for item in selected_products:
        product = item["product"]
        print(f"{product['id']:<5} {product['name']:<30} {item['quantity']:<10} {item['total_cost']:.2f}")

    print(f"\nTotal Cost: {total_cost:.2f} Ksh.")
    print("Thank you for your purchase!")

# Placeholder functions
def view_orders():
    print("Here are your recent orders:")
    # You can add order details here

def account_settings():
    print("Account Settings:")
    # Here you can add more options related to account settings

# Start the authentication process
auth()
