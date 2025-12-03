# 16_docstring_module.py
# Author: Joe O'Regan
# Date: 03-12-2025
# License: GPL v3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Brief: Utility functions to convert between metric and imperial units.

"""
Module for converting distances between metric and imperial systems.

Provides functions for:
- convert_to_metres(feet, inches)
- metres_to_imperial(metres)

This module demonstrates Pythonic functions and NumPy stile docstrings.
"""

def convert_to_metres(feet, inches):
    """
    Convert a distance from feet and inches to metres.
    
    This function assumes feet and inches are non-negative.
    It uses standard conversion: 1 inch = 0.0254 m.

    Parameters
    ----------
    feet : int
        The feet part of the distance.
    inches : float
        The inches part of the distance.
    
    Returns
    -------
    float
        The distance in metres.
    
    Examples
    --------
    >>> convert_to_metres(29, 2.5)
    8.9027
    >>> convert_to_metres(0, 12)
    0.3048
    >>> convert_to_metres(6, 0)
    1.8288
    """
    pass