from book import Book
from recipe import Recipe
import datetime

salad = Recipe(name='Salad', cooking_lvl=1, cooking_time=10, ingredients=['avocado', 'tomato', 'ham'],
               description='This is salad.', recipe_type='starter')
cake = Recipe(name='cake', cooking_lvl=1, cooking_time=30, ingredients=['egg', 'milk', 'butter', 'flour'],
              description='This is cake.', recipe_type='dessert')
sandwich = Recipe(name='sandwich', cooking_lvl=5, cooking_time=15, ingredients=['bread', 'ham', 'tomato'],
                  description='This is sandwich.', recipe_type='lunch')

# ingredient is not a list
sandwich_miss = Recipe(name='sandwich', cooking_lvl=5, cooking_time=15, ingredients='bread',
                       description='This is sandwich.', recipe_type='lunch')
Shouldnotwork = 'Shouldnotwork'

rcp_dict = dict.fromkeys(['starter', 'lunch', 'dessert'])

# create cookbook
my_book = Book(name="cookbook", last_update=datetime.datetime.now(),
               creation_date=datetime.datetime.now(), recipes_list=rcp_dict)

# add recipes to my cookbook
my_book.add_recipe(salad)
my_book.add_recipe(cake)
my_book.add_recipe(sandwich)
print('Three recipes added. Next one wont work.')
# fault inputs
my_book.add_recipe(sandwich_miss)
my_book.add_recipe(Shouldnotwork)
print()

print('++ get_recipe_by_name ++\n')
flanbis = my_book.get_recipe_by_name(cake)
saladbis = my_book.get_recipe_by_name(salad)

print('++ get_recipes_by_types ++\n')
print('++ starter ++')
starter_list = my_book.get_recipes_by_types('starter')
if starter_list is not None:
    if isinstance(starter_list, list):
        for elem in starter_list:
            print(str(elem))
    else:
        print(str(starter_list))

print('++ Lunch ++')
lunch_list = my_book.get_recipes_by_types('lunch')
if lunch_list is not None:
    if isinstance(lunch_list, list):
        for elem in lunch_list:
            print(str(elem))
    else:
        print(str(lunch_list))

print('++ Dessert ++')
dessert_list = my_book.get_recipes_by_types('dessert')
if dessert_list is not None:
    if isinstance(dessert_list, list):
        for elem in dessert_list:
            print(str(elem))
    else:
        print(str(dessert_list))
