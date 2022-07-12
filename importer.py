### IMPORTS
import os
import json
from recipe import Recipe
from generator import Generator

class Import:    
    def import_folder(input_dir: str, output_dir: str) -> bool: 
        try:
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

            gen = Generator()
            for name in runsheets.keys():
                gen.generate(name, runsheets[name], output_dir)
            return True
        except Exception as e:
            print("Something went wrong while importing. ", e)
            return False
