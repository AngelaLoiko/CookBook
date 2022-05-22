cook_book = {}
shop_list = {}
recipes_file='recipes.txt'

def get_dict_cook_book(recipes_file='recipes.txt'):
    with open(recipes_file, 'r', encoding='utf-8') as file:   
        listdish = file.read().split('\n\n')    
        for i in listdish:
            name_dish, count_ingredients, *ingredients = i.split('\n')
            list_ingredients = []
            for ingredient in ingredients:
                name_ingridient, quantity, measure = ingredient.split(' | ')
                list_ingredients.append({'ingredient_name': name_ingridient, 'quantity': quantity, 'measure': measure})
            cook_book[name_dish] = list_ingredients
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_ingredient = dict(ingredient)
            new_ingredient['quantity'] *= person_count
            if new_ingredient['ingredient_name'] not in shop_list:
                shop_list[new_ingredient['ingredient_name']] = new_ingredient
            else:
                shop_list[new_ingredient['ingredient_name']]['quantity'] += new_ingredient['quantity']
    return shop_list


cook_book = get_dict_cook_book()
print(f'{cook_book}\n')
shop_list = get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
print(shop_list)