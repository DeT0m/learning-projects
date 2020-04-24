import pyinputplus as pyip

PRICES = {
    'wheat': 1.0,
    'white': 0.7,
    'sourdough': 1.2,
    'chicken': 2.0,
    'turkey': 2.4,
    'ham': 1.5,
    'tofu': 1.3,
    'cheese': 0.5,
    'cheddar': 1.0,
    'Swiss': 1.3,
    'mozzarella': 1.0,
    'mayo': 0.3,
    'mustard': 0.2,
    'lettuce': 0.1,
    'tomato': 0.3,
}


def add_to_order(product):
    """Choose from option and add to order."""
    question = pyip.inputYesNo(f'Do you want {product}?\n')
    if question == 'yes':
        order.append(product)


order = []
check = []
order.append(pyip.inputMenu(['wheat', 'white', 'sourdough']))
order.append(pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu']))
cheese = pyip.inputYesNo(prompt='Do you want cheese? y/n\n')
if cheese == 'yes':
    order.append(pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella']))
add_to_order('mayo')
add_to_order('mustard')
add_to_order('lettuce')
add_to_order('tomato')
number = pyip.inputInt(prompt='How many sandwiches?\n', min=1)

for item in order:
    check.append(PRICES[item])
    print(f'Product: {item.title()}, Price: {PRICES[item]}')

print(f'Number of sandwiches: {number}')
print(f'Order total: {sum(check) * number}')
