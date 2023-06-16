"""E-commerce system with functionalities such as product management,\
user registration and authentication, shopping cart, and order processing."""
import uuid

# Product Class
class Product:
    """Create the class for product broughtup"""
    def __init__(self, name, price, description):
        self.id_ = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - ${self.price}"

    def get_id(self):
        """Get the product id"""
        return self.id_

# User Class
class User:
    """user class for creating details"""
    def __init__(self, name, email, password):
        self.id_ = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = password
        self.cart = []

    def add_to_cart(self, product):
        """For add product to the cart"""
        self.cart.append(product)

    def remove_from_cart(self, product):
        """For remove the product from cart"""
        if product in self.cart:
            self.cart.remove(product)

    def checkout(self):
        """For checking the product price"""
        total_price = sum([product.price for product in self.cart])
        order = Order(self, self.cart, total_price)
        self.cart = []
        return order

# Order Class
class Order:
    """order class for entering the product details"""
    def __init__(self, user, products, total_price):
        self.id_ = str(uuid.uuid4())
        self.user = user
        self.products = products
        self.total_price = total_price

    def __str__(self):
        product_names = [product.name for product in self.products]
        return f"Order ID: {self.id_}\nUser: {self.user.name}\nProducts:\
                {', '.join(product_names)}\nTotal Price: ${self.total_price}"

    def get_id(self):
        """get the order id"""
        return self.id_

    def get_total_price(self):
        """get the total product price"""
        return self.total_price

# Main Program
def main():
    """Main programm method"""
    products = [
        Product("iPhone", 999, "Latest iPhone model"),
        Product("MacBook Pro", 1999, "Powerful laptop for professionals"),
        Product("AirPods", 199, "Wireless earbuds")
    ]

    users = [
        User("John Doe", "john@example.com", "password123"),
        User("Jane Smith", "jane@example.com", "secret456")
    ]

    # User registration and login
    print("Welcome to our E-commerce system!")
    print("Please register to start shopping.")

    while True:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        user = User(name, email, password)
        users.append(user)

        choice = input("Registration successful! Login now? (yes/no): ")
        if choice.lower() == "yes":
            break

    print("Login to your account.")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = next((user for user in users if user.email == email and user.password == password), None)

    if user:
        print("Login successful!")
        print(f"Welcome, {user.name}!")

        # Product browsing and cart management
        print("Here are some available products:")
        for product in products:
            print(product)

        while True:
            choice = input("Enter the product name to add to cart (or 'checkout'\
                            to proceed to checkout): ")

            if choice.lower() == "checkout":
                order = user.checkout()
                print("Order placed successfully!")
                print(order)
                break

            product = next((product for product in products if product.name.lower()\
                      == choice.lower()), None)

            if product:
                user.add_to_cart(product)
                print(f"{product.name} added to cart.")
            else:
                print("Invalid product name. Please try again.")

    else:
        print("Invalid email or password. Please try again.")

    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()
