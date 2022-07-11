from recipe import Recipe

class Generator:
    def __init__(self):
        return
    
    def generate(recipe: Recipe, destination: str) -> bool:
        try:
            
            return True
        except Exception as e:
            print("Something went wrong while generating the runsheet. ", e)
            return False