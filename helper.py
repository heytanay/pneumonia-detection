"""
Author: Tanay Mehta
Github: @heytanay
---------------------
A few helper function(s)
"""
import os
import sys

def get_arg(arg_idx: int):
    """
    Try to get an argument at a specific index
    If not found, return -1
    """
    try:
        arg = sys.argv[arg_idx]
    except IndexError:
        return -1
    return arg