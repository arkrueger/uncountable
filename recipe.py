from typing import Dict

class Recipe:
    class Section:
        def __init__(self, name: str, body: list):
            try:
                self.headers    = [] # the column headers (they are not the same as the column tags)
                self.columns    = [] # the key referring to the data in each cell, e.g. "name" or "quantity"
                self.lefthand   = "" # the column, if any, that will be placed on the furthest lefthand side
                self.rows       = body
                if name == "metadata":
                    self.headers = ["", ""]
                    self.columns = ["name", "quantity"]
                elif name == "steps":
                    self.headers = ["Step Number", "Ingredient", "Quantity"]
                    self.columns = ["number", "name", "quantity"]
                    self.lefthand = "number"
                elif name == "measurements":
                    self.headers = ["", "Completed?"]
                    self.columns = ["name", ""]
                else:
                    self.headers = ["",""]
                    self.columns = ["name", "quantity"]
                return
            except Exception as e:
                print("Something went wrong while creating a section. ", e)
                return

    def __init__(self, recipe: dict):
        try:
            self.name = recipe["recipe_name"]
            self.sections = []
            for s in recipe.keys():
                if s != "recipe_name": # handles the edge case where the steps are not in the expected order
                    self.sections.append(self.Section(s, recipe[s]))
            return
        except Exception as e:
            print("Something went wrong while initializing the recipe. ", e)
            return

