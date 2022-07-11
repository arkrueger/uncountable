### IMPORTS
import os
import json
from recipe import Recipe
from generator import Generator

# Get all recipe files from the input folder.
recipes = []
for file in os.listdir(os.getcwd()+"/input"):
    recipes = Recipe(json.loads(file))

for r in recipes:
    pass




