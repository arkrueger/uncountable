from recipe import Recipe

class Generator:
    def __init__(self):
        return
    
    def generate(recipe: Recipe, destination: str) -> bool:
        try:
            # return True if successful
            return True
        except:
            print("Something went wrong while generating the runsheet.")
            return False