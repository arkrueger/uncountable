### IMPORTS
import os
import json
from recipe import Recipe
from generator import Generator

# get all recipe files from the input folder
runsheets = {} # dict of lists, where the key is the filename and the list value is the recipes, e.g. [formulation1, formulation2]
input_dir = os.getcwd()+"/input/"
output_dir = os.getcwd()+"/output/"
os.chdir(input_dir)
for file in os.listdir(input_dir):
    name = file[:len(file)-5] # this will be our dict key
    # read in the .json file
    with open(file, 'r') as f:
        runsheets[name] = json.load(f)["data"] # returns a dict representing the json
        # since each file can have multiple recipes, unpack these and create individual recipes for them
        recipe = runsheets[name]
        for i in range(len(recipe)):
            recipe[i] = Recipe(recipe[i])
            print(vars(recipe[i].sections[2]))
print(runsheets)

gen = Generator()
for sheet in runsheets:
    gen.generate(sheet, output_dir)




