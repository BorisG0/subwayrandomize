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

