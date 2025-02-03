import random

ingredients_path = 'ingredients.txt'

def read_ingredients(path):
    with open(path, 'r') as file:
        content = file.read()
        categories = content.split('\n\n')

    ingredients = {}
    for category in categories:
        category_name, *items = category.split('\n')
        ingredients[category_name] = items
    
    return ingredients

ingredients = read_ingredients(ingredients_path)

sandwich = 'I will get a '

# sub size
size = random.choice(['6-inch', 'footlong'])
sandwich += size + ' '

# bread
bread = random.choice(ingredients['Bread'])
sandwich += bread + ' with '

# meat
meat = random.choice(ingredients['Meat'])
double_meat = random.choice([True, False])
if double_meat:
    sandwich += 'double '

sandwich += meat

# bacon
plus_bacon = random.choice([True, False])
if plus_bacon:
    sandwich += ' plus bacon'

# cheese
cheese = random.choice(ingredients['Cheese'])
sandwich += ' and ' + cheese + ' cheese'

# toast
toasted = random.choice([True, False])
if toasted:
    sandwich += ', toasted'

# vegetables
vegetables = random.sample(ingredients['Vegetables'], random.randint(0, len(ingredients['Vegetables'])))
if vegetables:
    sandwich += ' with '
    for i, vegetable in enumerate(vegetables):
        if i == len(vegetables) - 1:
            sandwich += 'and ' + vegetable
        else:
            sandwich += vegetable + ', '

# sauce
sauce = random.choice(ingredients['Sauce'])
sandwich += ' and ' + sauce + ' sauce'

print(sandwich)