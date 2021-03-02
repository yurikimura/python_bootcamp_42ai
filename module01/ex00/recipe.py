class Recipe:

    def __init__(self, name: str = None, cooking_lvl: int = None,
                 cooking_time: int = None, ingredients: list = None,
                 description: str = None, recipe_type: str = None):
        """
        • name (str)
        • cooking_lvl (int) : range 1 to 5
        • cooking_time (int) : in minutes (no negative numbers)
        • ingredients (list) : list of all ingredients each represented by a string • description (str) : description of the recipe
        • description (str) : description of the recipe
        • recipe_type (str) : can be “starter”, “lunch” or “dessert”.
        """

        if isinstance(name, str):
            self.name = name
        else:
            print("neme must be string")

        if isinstance(cooking_lvl, int) and cooking_lvl in range(1, 6):
            self.cooking_lvl = cooking_lvl
        else:
            print("cooking level must be int [1, 5]")

        if isinstance(cooking_time, int) and cooking_time > 0:
            self.cooking_time = cooking_time
        else:
            print("cooking time must be int > 0")

        if isinstance(ingredients, list):
            self.ingredients = ingredients
        else:
            print("ingredients must be list")

        if isinstance(description, str):
            self.description = description
        else:
            print("description must be string")

        if (recipe_type == "starter") or (recipe_type == "lunch") or (recipe_type == "dessert"):
            self.recipe_type = recipe_type
        else:
            print("recipe type must be “starter”, “lunch” or “dessert”")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt = f"name: {self.name}\n"\
            + f"level: {self.cooking_lvl}\n"\
            + f"time: {self.cooking_time}\n"\
            + f"ingredients: {self.ingredients}\n"\
            + f"recipe_type: {self.recipe_type}"

        return txt
