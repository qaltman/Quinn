import numpy as np
from wafer import Wafer


class Mask:
    """
    Builds a photoresist mask pattern and applies it to a Wafer.

    This OOP is used almost as a sketch where we are gooing to be using shapes and lines 
    to represent different etches and photoresists that are common in legit 
    semi conductor etching. 

    Internally the mask stores a 2D grid of true and false values 
    where true represents the wafer being protected and false represents 
    unprotected silicone

    Coordinate convention: (row, col) where row 0 is the TOP of the wafer.

    """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        #Here we make our inital mask using np zeros to make array of zeros 
        #bool sets the values to false as I saif above
        self._pattern = np.zeros((rows, cols), dtype=bool)


    def add_rectangle(self, row_start, col_start, height, width):
        """
        Protect a rectangular region of the wafer.
            row_start gives the top row of the rectangle
            col_start is the left column of the rectangle
            height gives you how many rows tall the rectangle is
            width is how many columns wide the rectangle is
        The rectangle covers rows [row_start, row_start+height)
        and columns [col_start, col_start+width).
        """
        #this section was suggested to prevent negative indexing so we stay within the 2D array of the wafer 
        #essentially we are defining an area for the patter to be laid out on within the 2D array. The variables used are 
        #defined in a parameter that sits within main when the function is called later on
        r0 = max(row_start, 0) #row max 
        c0 = max(col_start, 0)#column max
        r1 = min(row_start + height, self.rows)#row min
        c1 = min(col_start + width,  self.cols)#column min

    
        self._pattern[r0:r1, c0:c1] = True #sets the entire defined rectangle array to true

    def add_horizontal_line(self, row, col_start=0, col_end=None, thickness=1):
        """
        A layer of photo resist that looks like a horizontal stripe across the wafer.
            row is the center row of the stripe
            col_start is where the stripe starts (left edge, column 0)
            col_end is where the stripe ends   (right edge)
            thickness shows how many rows thick the stripe is
        """
    
        if col_end is None:
            col_end = self.cols #essentialy says if there is no end listed it extends to the edge of the 2D array

        # A stripe of thickness N is centered on the defined row for parameter
        # Example: row=50, thickness=3 → rows 49, 50, 51
        half = thickness // 2 #use of floor division so we keep that values as whole intergers
        r0 = max(row - half, 0)
        r1 = min(row - half + thickness, self.rows)
        c0 = max(col_start, 0)
        c1 = min(col_end, self.cols)

        self._pattern[r0:r1, c0:c1] = True #makes the values true

    def add_vertical_line(self, col, row_start=0, row_end=None, thickness=1):
        """
       Essentailly the same as above just going verticle now
        """
        # shows that if there is no row end then the verticle stripe extends to the end of the array
        if row_end is None:
            row_end = self.rows

        half = thickness // 2
        c0 = max(col - half, 0)
        c1 = min(col - half + thickness, self.cols)
        r0 = max(row_start, 0)
        r1 = min(row_end, self.rows)

        self._pattern[r0:r1, c0:c1] = True #sets the defined photo resist to true once complete.

    def add_cross(self, center_row, center_col, arm_length, thickness=2):
        """
        wanted to make a shape using the verticle and horizontal line methods. 
        This is a convenience method - it simply calls add_horizontal_line
        and add_vertical_line to form a cross shape.
            center_row, center_col gives the center point of the cross
            arm_length is how far each arm extends from the center
            thickness gives how thick the arms are (in cells)
        """
        # Horizontal arm of the cross using the horizontal line function to create the cross
        self.add_horizontal_line(row=center_row,col_start=center_col - arm_length,col_end=center_col + arm_length,thickness=thickness,)
        # Vertical arm of the cross using the verticle line fucntion to create the cross
        self.add_vertical_line(col=center_col, row_start=center_row - arm_length, row_end=center_row + arm_length, thickness=thickness,)

    def clear(self):
        """Used the reset the entire process"""
        self._pattern[:] = False

    def get_pattern(self):
        """Call this to get the defined pattern"""
        return self._pattern


    def apply(self, wafer):
        """
        After calling this, the wafer's cells that were True in the
        pattern will be set to MASK (2), protecting them from etching.
        """
        wafer.apply_mask(self._pattern)
