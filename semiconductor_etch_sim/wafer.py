import numpy as np

ETCHED   = 0   # the material has been removed (empty void)
MATERIAL = 1   # silicon substrate is present
MASK     = 2   # protected by photoresist mask (won't be etched)


class Wafer:
    """
    This OOP shows the 2D semiconductor wafer.
    Each cell in the grid holds one of three integer values: etched, material, and mask as defined above
    The grid is stored as a NumPy 2D array so that matplotlib can display it in a diagram later using visualizer.
    """

    def __init__(self, rows=100, cols=100):
        # Save the dimensions so other OOP's can use them
        self.rows = rows
        self.cols = cols

       #creates a np grid of 1 which is material as whole interger values.
        self.grid = np.ones((rows, cols), dtype=int)

    def apply_mask(self, mask_pattern):
        """
        Overlay a mask pattern onto the wafer.
        mask_pattern is a 2D array of True/False values the same size
        as the wafer.  Where mask_pattern is True, the corresponding
        wafer cell is protected (set to MASK).
        We only protect cells that currently hold MATERIAL - we never
        "re-protect" a cell that was already etched away.
        """
        # Loop through every row and column of the grid
        for row in range(self.rows):
            for col in range(self.cols):
                # Only mark a cell as MASK if:
                # the mask pattern says to protect this spot, AND
                # there is still material here (not already etched)
                if mask_pattern[row][col] and self.grid[row][col] == MATERIAL:
                    self.grid[row][col] = MASK

    def remove_mask(self):
        """
        Strip the photoresist after etching.
        In real chip manufacturing, the photoresist is dissolved away
        with a chemical wash once etching is complete.  Here we just
        set every MASK cell back to MATERIAL.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == MASK:
                    self.grid[row][col] = MATERIAL

    def reset(self):
        """Restore the wafer to its original all-material state."""
        # Replace the entire grid with a fresh array of 1s (MATERIAL)
        self.grid = np.ones((self.rows, self.cols), dtype=int)

    def copy(self):
        """
        Return an independent copy of this wafer.

        We use this to take a "before" snapshot so we can compare
        the wafer state before and after etching.

        Important: we call .copy() on the NumPy array so that the new
        wafer has its own separate data - without it, both wafers would
        share the same array and changes to one would affect the other.
        """
        new_wafer = Wafer(self.rows, self.cols)
        new_wafer.grid = self.grid.copy()  # .copy() makes an independent duplicate
        return new_wafer

    def get_stats(self):
        """
        Count how many cells are in each state.

        Returns a plain dictionary, for example:
            {"etched": 500, "material": 200, "masked": 300}
        """
        etched_count   = 0
        material_count = 0
        mask_count     = 0

        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                if cell == ETCHED:
                    etched_count += 1
                elif cell == MATERIAL:
                    material_count += 1
                else:  # cell == MASK
                    mask_count += 1

        return {
            "etched":   etched_count,
            "material": material_count,
            "masked":   mask_count,
        }

    def __repr__(self):
        """
        Controls how the wafer looks when you print() it.
        """
        stats = self.get_stats()
        return (
            f"Wafer({self.rows}x{self.cols}) | "
            f"etched={stats['etched']}, "
            f"material={stats['material']}, "
            f"masked={stats['masked']}"
        )
