import numpy as np

ETCHED   = 0   # the material has been removed
MATERIAL = 1   # silicon material
MASK     = 2   # protected by photoresist mask 

class Wafer:
    """
    This OOP shows the 2D semiconductor wafer.
    Each cell in the grid holds one of three values: etched, material, and mask
    The grid is stored as a NumPy 2D array so that matplotlib can display it in a diagram later using visualizer.
    """
    def __init__(self, rows=100, cols=100):
        #Save the dimensions so other OOP's can use them
        self.rows = rows
        self.cols = cols
       #creates a np grid of 1 which is material.
        self.grid = np.ones((rows, cols), dtype=int)
    def apply_mask(self, mask_pattern):
        """
        This function is used to make the mask on the array.
        """
        #Loop through every row and column of the grid
        for row in range(self.rows):
            for col in range(self.cols):
                #This function makes the mask pattern on material. Follows the predefined maskpattern.
                if mask_pattern[row][col] and self.grid[row][col] == MATERIAL:
                    self.grid[row][col] = MASK
    def remove_mask(self):
        """
        This function is to get rid of the mask once the etching has occured.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == MASK:
                    self.grid[row][col] = MATERIAL
    def reset(self):
        """This is just used to reset back to 1's where we started."""
        #Replace the entire grid with a fresh array of 1s (MATERIAL)
        self.grid = np.ones((self.rows, self.cols), dtype=int)
    def copy(self):
        """
        This function is essential for the before and after final images and takes a coppy of the 
        before wafer with mask appliied.
        """
        new_wafer = Wafer(self.rows, self.cols)
        new_wafer.grid = self.grid.copy()  
        return new_wafer
    def get_stats(self):
        """
        A little data tracker
        Returns:
            {"etched": 500, "material": 200, "masked": 300}
        """
        etched_num   = 0
        material_num = 0
        mask_num     = 0

        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                if cell == ETCHED:
                    etched_num += 1
                elif cell == MATERIAL:
                    material_num += 1
                else:
                    mask_num += 1

        return {"etched": etched_num,"material": material_num,"masked": mask_num,}
    def __repr__(self):
        """
        prints the stats onto the output terminal so we know how the wafer compares through the process.
        """
        stats = self.get_stats()
        return (f"Wafer({self.rows}x{self.cols}) | "
            f"etched={stats['etched']}, "
            f"material={stats['material']}, "
            f"masked={stats['masked']}")
