"""
main.py is my Semiconductor Etch Simulation

This is the main script that runs the full simulation
The simulation follows this pipeline
Create a wafer (starts as all silicon material), Build a photoresist mask pattern, Apply the mask to the wafer (protect certain areas), Save a copy of the wafer before etching, Run the etch model (removes all exposed MATERIAL cells), Strip the photoresist mask, Display a before / after comparison plot
"""

from wafer import Wafer
from mask import Mask
from etcher import InstantEtcher
from visualizer import plot_before_after


def build_demo_mask(mask):
    """
    Build a mask pattern for the 2D array
    The pattern includes
        - Four rectangular shapes 
        - A horizontal and a vertical line
        - verticle connectors
        - Two small alignment crosses in the corners!
    below builds the wafer patterns. If you want to move some of the shapes from mask around you can just adjust the numbers below. 
    """
    rows = mask.rows
    cols = mask.cols

    # Rectangles
    # Top left  
    mask.add_rectangle(row_start=10, col_start=10, height=20, width=25)
    # Top right 
    mask.add_rectangle(row_start=10, col_start=cols - 35, height=20, width=25)
    # Bottom left
    mask.add_rectangle(row_start=rows - 30, col_start=10, height=20, width=25)
    # Bottom right
    mask.add_rectangle(row_start=rows - 30, col_start=cols - 35, height=20, width=25)

    # lines horizontal and verticle

    # Horizontal 
    mask.add_horizontal_line(row=rows // 2, thickness=3)
    # Vertical
    mask.add_vertical_line(col=cols // 2, thickness=3)

    # Verticle Connectors
    mid_row = rows // 2
    # Left connectors
    mask.add_vertical_line(col=22, row_start=30,      row_end=mid_row,    thickness=2)
    mask.add_vertical_line(col=22, row_start=mid_row, row_end=rows - 10,  thickness=2)

    # Right connectors
    mask.add_vertical_line(col=cols - 22, row_start=30,      row_end=mid_row,   thickness=2)
    mask.add_vertical_line(col=cols - 22, row_start=mid_row, row_end=rows - 10, thickness=2)

    # Add crosses
    mask.add_cross(center_row=5,        center_col=5,        arm_length=3, thickness=1)
    mask.add_cross(center_row=rows- 5, center_col=cols- 5, arm_length=3, thickness=1)


def main():
    
    # Creating the wafer
    # A 120x120 grid of cells of all MATERIAL
    ROWS = 120
    COLS = 120
    wafer = Wafer(rows=ROWS, cols=COLS)
    print("Initial:", wafer)
    
    # Build mask and add it to the wafer
    mask = Mask(rows=ROWS, cols=COLS)
    build_demo_mask(mask)   # fill in the pattern
    mask.apply(wafer)       # put it onto the wafer
    print("Masked:", wafer)

    
    # save wafer for the before visualization
    before_snapshot = wafer.copy()

    # Etch the wafer
    # remove all the cells that arent masked
    etcher = InstantEtcher()
    stats = etcher.etch(wafer)
    print(f"Etched:{stats['cells_etched']} cells ({stats['percent_etched']}% of wafer)")

    
    # get rid of the mask
    # This turns the remaining mask back to material
    wafer.remove_mask()
    print("Post-etch:", wafer)

    # Visualize the before and after wafers
    plot_before_after(before_wafer=before_snapshot, after_wafer=wafer, title="Semiconductor Etch Simulation - Instant Etch Model", )


# I had to add this because I was running into an error when running main. google said this would ensure that it ran this file. 
if __name__ == "__main__":
    main()
