"""
Global plotting style for the Life Expectancy project.

This module defines a unified visualization style to ensure
consistent, clean, and professional-looking plots across
all notebooks in the project.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def set_plot_style():
    """
    Apply a global matplotlib and seaborn style configuration.

    This function should be called once at the beginning
    of each notebook to ensure consistent visualization style.
    """

    # ==============================
    # Seaborn global theme
    # ==============================
    sns.set_theme(
        style="whitegrid",
        context="notebook",
        palette="deep"
    )

    # ==============================
    # Matplotlib rcParams
    # ==============================
    plt.rcParams.update({

        # Figure
        "figure.figsize": (10, 6),
        "figure.dpi": 120,
        "figure.autolayout": True,

        # Fonts
        "font.size": 11,
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,

        # Axes
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.3,

        # Lines & markers
        "lines.linewidth": 2,
        "lines.markersize": 6,

        # Save figures
        "savefig.dpi": 300,
        "savefig.bbox": "tight"
    })
