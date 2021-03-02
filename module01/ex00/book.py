import datetime
from recipe import Recipe


class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        """
        • name (str)
        • last_update (datetime)
        • creation_date (datetime)
        • recipes_list (dict) : a dictionnary why 3 keys: “starter”, “lunch”, “dessert”.
        """

        if isinstance(name, str):
            self.name = name
        else:
            print('name must be string')

        if isinstance(last_update, datetime.datetime):
            self.last_update = last_update
        else:
            print('last_update must be datetime')

        if isinstance(last_update, datetime.datetime):
            self.creation_date = creation_date
        else:
            print('creation_date must be datetime')

        test_dict = {'starter': 1, 'lunch': 2, 'dessert': 3}
        if isinstance(recipes_list, dict):
            if test_dict.keys() == recipes_list.keys():
                self.recipes_list = recipes_list
            else:
                print('recipes_list must contain "starter", "lunch" and "dessert"')
        else:
            print('recipes_list must be a dictionary')

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        if isinstance(name, Recipe):
            for elem in self.recipes_list.values():
                if elem and isinstance(elem, list):
                    for obj in elem:
                        if obj == name:
                            print(obj)
                elif elem and name == elem:
                    print(elem)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list.keys():
            return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            if self.recipes_list[recipe.recipe_type] is None:
                self.recipes_list[recipe.recipe_type] = [recipe]
            else:
                self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
        else:
            print(f'{recipe} is not an instance of class Recipe! No update has been done.')
