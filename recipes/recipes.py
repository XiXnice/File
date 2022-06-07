RECIPES_INTERPRETER = 'recipes/Recipes.txt'
cook_book = {}
def  recipes_worker(recipes_name):
    with open(recipes_name, encoding='UTF-8') as recipes:
        for line in recipes.read().split('\n\n'):
            name, ingre, *args = line.lower().split('\n')
            ingredients = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
                cook_book[name] = ingredients
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new = dict(ingredient)
            new['quantity'] *= person_count
            if new['ingredient_name'] not in shop_list:
                shop_list[new['ingredient_name']] = new
            else:
                shop_list[new['ingredient_name']]['quantity'] += new['quantity']
    return shop_list

def create_shop_list():
    person_count = int(input('Введите нужное количество человек: '))
    dishes = input('Введите требуемые блюда в расчете на одного человека (через запятую"*, *"): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

def print_shop_list(shop_list):
    for item in shop_list.values():
        print("ingredient_name: '{}', measure: '{}', quantity: '{}'".format(item['ingredient_name'], item['measure'], item['quantity']))

recipes_worker(RECIPES_INTERPRETER)
create_shop_list()
