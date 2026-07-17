# Part A - Spot the Bug

def add_item(item, cart=[]):
    cart.append(item)
    return cart


print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", ["bread"]))
print(add_item("eggs"))

print("--------------------------------")


# Part B - Correct Function

def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


print(add_item("apple"))
print(add_item("banana"))

print("--------------------------------")


# Part C - Shopping Cart

# Create Cart
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Add Items
def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }
    cart["items"].append(item)


# Update Tuple
def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError:
        print("Tuple is immutable. We cannot change its values.")


# Calculate Total
def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total = total + (item["price"] * item["qty"])

    discount = (total * cart["discount"]) / 100
    final_total = total - discount

    return final_total


# Customer 1
cart1 = create_cart("Lakshmi", 10)
add_to_cart(cart1, "Book", 500, 2)
add_to_cart(cart1, "Pen", 20, 3)

# Customer 2
cart2 = create_cart("Rahul")
add_to_cart(cart2, "Bag", 800)

print("Customer 1 Cart:", cart1)
print("Total:", calculate_total(cart1))

print()

print("Customer 2 Cart:", cart2)
print("Total:", calculate_total(cart2))

print("--------------------------------")

price = (500,)
update_price(price, 600)


# Discussion Answers

# 1. discount=0 is safe because integer is immutable.
#    cart=[] is dangerous because list is mutable.

# 2. Rebinding means assigning a new object.
#    Mutating means changing the existing object.

# 3. Mutable: list, dict, set
#    Immutable: tuple, str, int

# 4. Yes. If we modify a list inside a function,
#    the changes are reflected outside because
#    lists are mutable.
