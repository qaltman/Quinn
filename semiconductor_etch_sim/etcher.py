from wafer import MATERIAL, ETCHED


class InstantEtcher:
    """
    This OOP defines the etching for the 2D array. It essentially takes the defined wafer and mask.
    An exposed cell is one whose value is MATERIAL (1) (changing this to etched)
    Cells protected by the mask are left untouched.
    Cells etched (ETCHED = 0) are also left alone so we dont run into errors when running the code.
    """
    def etch(self, wafer):
        """
        This is the heart of the etching process where material is removed and the array value is changed to etched 
        I also included a part that tells you the number of cells that etched and percentage. 
        """
        cells_etched = 0 #set intial value
        total_cells  = wafer.rows * wafer.cols #total cells of the 2D array
        # Iterate through the entire 2D array and find material turning it into etched values
        for row in range(wafer.rows):
            for col in range(wafer.cols):
                if wafer.grid[row][col] == MATERIAL:
                    wafer.grid[row][col] = ETCHED  
                    cells_etched += 1 # keep count of cells etched
        # Calculate what percentage of the wafer was etched
        percent_etched = round(100 * cells_etched / total_cells, 2) #use round function so that we keep it to two values after the decimal place
        # Values for our dictionalry count at the end
        return {"cells_etched": cells_etched, "total_cells": total_cells, "percent_etched": percent_etched,}
