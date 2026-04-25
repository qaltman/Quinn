import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from wafer import ETCHED, MATERIAL, MASK


"""For each material, etched, and mask, I decided to use a red green blue color scheem 
because it was easier to get the colors I wanted 
I could just look the codes up online."""
CELL_COLORS = {ETCHED:[0.10, 0.14, 0.49],MATERIAL:[0.69, 0.75, 0.77] ,MASK:[0.98, 0.66, 0.15],} # Dark blue, grey, yellow

# legend values
CELL_LABELS = {ETCHED:"Etched (void)", MATERIAL:"Material (Silicon)", MASK:"Mask (photoresist)",}


def make_rgb_image(wafer):
    """
    This is going to turn our 2D array into a colored a plotable image using the parameters above.
    """
    # Create an empty image initalizing as all 0
    # The shape (rows, cols,) 3 represents pixels which is used with R/G/B
    image = np.zeros((wafer.rows, wafer.cols, 3))
    for row in range(wafer.rows):
        for col in range(wafer.cols):
            cell_state = wafer.grid[row][col]   # 0, 1, or 2
            image[row][col] = CELL_COLORS[cell_state]  # look up the color
    return image


def make_legend_items():
    """
    Build a list of colored patches to use as a legend.
    mpatches.Patch creates a small colored rectangle.
    We pass these to ax.legend() or fig.legend() so matplotlib
    knows what color means what.
    """
    patches = []
    for state in [ETCHED, MATERIAL, MASK]:
        patch = mpatches.Patch(
            color=CELL_COLORS[state],
            label=CELL_LABELS[state],
        )
        patches.append(patch)
    return patches


def plot_wafer(wafer, title="Wafer"):
    """
    Display a single wafer as a colored grid image.

    Parameters:
        wafer - the Wafer object to visualize
        title - the title shown above the plot
    """
    # Build the colored image from the wafer grid
    image = make_rgb_image(wafer)

    # Create a new figure and a single set of axes
    fig, ax = plt.subplots(figsize=(6, 6))

    # imshow() treats the array as an image and draws each cell as a pixel
    ax.imshow(image)

    # Add labels
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")

    # Add the legend in the upper-right corner
    ax.legend(handles=make_legend_items(), loc="upper right", fontsize=9)

    plt.tight_layout()
    plt.show()


def plot_before_after(before_wafer, after_wafer,
                      title="Semiconductor Etch Simulation",
                      save_path=None):
    """
    Show a side-by-side comparison of the wafer before and after etching.
    Parameters:
        before_wafer- the Wafer snapshot taken before etching
        after_wafer- the Wafer state after etching and mask removal
        title- the big title shown at the top of the figure
        save_path- if provided, save the figure to this file path
                   instead of displaying it on screen
    """
    # Build a colored image for each wafer state
    before_image = make_rgb_image(before_wafer)
    after_image  = make_rgb_image(after_wafer)

    # Create a figure with two subplots side by side
    # 1 row, 2 columns of plots; figsize controls the overall window size
    fig, axes = plt.subplots(1, 2, figsize=(13, 8))

    # Big title for the whole figure (suptitle = "super title")
    fig.suptitle(title, fontsize=15, fontweight="bold")

    # ----- Left subplot: before etching -----
    axes[0].imshow(before_image)
    axes[0].set_title("Before Etch\n(mask applied)")
    axes[0].set_xlabel("Column")
    axes[0].set_ylabel("Row")

    # ----- Right subplot: after etching -----
    axes[1].imshow(after_image)
    axes[1].set_title("After Etch\n(mask removed)")
    axes[1].set_xlabel("Column")
    axes[1].set_ylabel("Row")

    # Add a shared legend centered at the bottom of the figure.
    # bbox_to_anchor=(0.5, -0.04) places it just below the center.
    # ncol=3 puts all three items on one row.
    fig.legend(
        handles=make_legend_items(),
        loc="lower center",
        ncol=3,
        fontsize=10,
        bbox_to_anchor=(0.5, -0.001),
    )

    plt.tight_layout()

    if save_path is not None:
        # Save the figure to a file instead of showing it
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        print("Figure saved to " + save_path)
    else:
        plt.show()
