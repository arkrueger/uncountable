### IMPORTS
import os
import importer

input_dir = os.getcwd()+"/input/"
output_dir = os.getcwd()+"/output/"

try:
    importer.Import.import_folder(input_dir, output_dir)
    print("Conversion successful.")
except Exception as e:
    print("Something went wrong. ", e)
