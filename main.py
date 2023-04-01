with open('recipes.txt','rt',encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        ingredients_counter = int(f.readline())
        ingredieents = []
        for i in range(ingredients_counter):
            ingr = f.readline().strip()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingredieents.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[dish] = ingredieents
#print(cook_book)
def get_shop_list_by_dishes(dishes, person_count):
    dict_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                dict_dishes[ingridient['ingredient_name']] = {
                    'quantity': int(ingridient['quantity']) * person_count,
                    'measure': ingridient['measure']}
    return dict_dishes
print(get_shop_list_by_dishes(['Запеченный картофель'],2))