class Recipe:
    class Section:
        def __init__(self, section_format: dict, transposed: bool) -> bool:
            # transposed indicates whether the section is organized as default row-wise (like steps), or transposed col-wise (like metadata)
            try:
                return True
            except:
                print("Something went wrong while creating a section.")
                return False

    def __init__(self, raw_recipe: dict, format: dict) -> bool:
        try:
            data = raw_recipe["data"]
            # return True if no errors
            return True
        except:
            print("Something went wrong.")
            return False

