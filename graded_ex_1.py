# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    pass


def display_products(products_list):
    pass


def display_categories():
    i = 0
    for key in products.keys():
        i += 1
        print(f'{i}. {key}')


def add_to_cart(cart, product, quantity):
    pass


def display_cart(cart):
    pass


def generate_receipt(name, email, cart, total_cost, address):
    pass


def validate_name(name: str) -> bool:
    if ' ' not in name:
        print('Invalid name')
        return False
    res = True
    first, last = name.split(' ')
    if not first.isalpha() or not last.isalpha():
        print('Invalid')
        res = False
    return res


def validate_email(email: str) -> bool:
    if '@' not in email:
        print('Invalid email')
        return False
    else:
        return True


def main():
    # name
    while True:
        username = input('Please enter your firstname and lastname seperated by blank with only alphabets >> ')
        if validate_name(username):
            break
    # email
    while True:
        user_email = input('Please enter your email >> ')
        if validate_email(user_email):
            break
    # show categories
    display_categories()
    category = input('Please enter the number corresponding with the category >> ')
    while not category.isdigit():
        print('Invalid category')
        category = input('Please enter the number corresponding with the category >> ')
    category = int(category)
    # show products


""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
