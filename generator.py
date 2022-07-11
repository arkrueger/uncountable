from recipe import Recipe
import openpyxl as op
import os

class Generator:
    def __init__(self):
        return
    
    def generate(self, name: str, recipes: list, destination: str) -> bool:
        # helper function
        def build_section(worksheet, section: Recipe.Section, start_row: int, start_col: int) -> int:
            try:
                row, col = start_row, start_col
                # fill in the section title
                worksheet.cell(row=row, column=col).value = "*** "+section.name.upper()+" ***"
                row += 1
                # fill in the lefthand header if applicable
                header_offset = 0
                if section.lefthand:
                    header_offset = 1 # skip over the "step number" heading for the regular headers
                    worksheet.cell(row=row, column=1).value = section.lefthand
                    # fill in the "step number" column
                    # this could be done under an if statement in the other for loop, but I find it more readable here  
                    for i,v in enumerate(section.rows):
                        worksheet.cell(row=header_offset+row+i, column=1).value = section.rows[i]["number"]
                    print("i ran")
                # fill in the normal headers
                for i,v in enumerate(section.headers):
                    if len(section.headers) == header_offset+i: break # avoids going out of range
                    worksheet.cell(row=row, column=col+i).value = section.headers[header_offset+i] # caveat: bad code, assumes that the lefthand header will be the first element. See the format document for ideas on building this information into the format itself to make the code more robust.
                # fill in the body of the table
                row += 1 if any(section.headers) else 0 # don't increment if all headers are empty strings
                print("hello")
                for i, v in enumerate(section.rows):
                    print(v)
                    for j,c in enumerate(section.columns):
                        if len(section.columns) == header_offset+j: break
                        worksheet.cell(row=row+i, column=col+j).value = section.rows[i][section.columns[header_offset+j]]
                        if section.rows[i][section.columns[header_offset+j]] == "Project Lead":
                            print("FOUND IT---------------------------------------------------")
                print("did a full section successfully")
                return row+i+2 # the next section will start 2 rows below the lowest row of this section
            except Exception as e:
                print("Something went wrong while building ", section.name, " section. ", e)
        
        # main function
        try:
            os.chdir(destination)
            workbook = op.Workbook()
            worksheet = workbook.active
            ### Set the recipe names for each recipe within the runsheet
            lowest_row = 1 # keep track of the lowest row so that we start all recipes' next sections on the same row
            offset = 1 # column offset for the recipe names
            step = 2 # formulation names are placed in 2 cells merged together, so to reach the next empty cell we need to step by 2
            i = 1 # beginning column because spreadsheets are 1-indexed
            for r in recipes:
                worksheet.cell(row=1, column=i+offset).value = r.name
                i += step
            # outdent

            ### Build the sections
            current_row = 3 # we know that the first section title begins at row 3, always
            num_of_sections = 3 # currently, we know of three sections: metadata, steps, and measurements
            for i in range(num_of_sections):
                current_col = 2
                for j,r in enumerate(recipes):
                    print("calling build section on row: ", current_row)
                    section_lowest_row = build_section(worksheet, r.sections[i], start_row=current_row, start_col=current_col)
                    print(j, " section lowest: ", section_lowest_row)
                    lowest_row = max(lowest_row, section_lowest_row)
                    current_col += step
                current_row = lowest_row
            
            workbook.save(name+".xlsx")

            return True
        except Exception as e:
            print("Something went wrong while generating the runsheet. ", e)
            return False