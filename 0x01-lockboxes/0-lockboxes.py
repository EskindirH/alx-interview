#!/usr/bin/python3
"""
This module defines the can_unlock_all function that determines 
if all boxes in a list of lists can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked given their contents.

    Args:
        boxes (list of lists): A list where each element represents a box 
                               containing a list of keys (integers).
                               Each key corresponds to another box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # number of boxes
    unlocked = [False] * n  # initially, all boxes are locked
    unlocked[0] = True  # the first box is unlocked
    opened = [0]  # list of boxes that are unlocked
    keys = set(boxes[0])  # keys found in the first box

    while opened:
        box = opened.pop()  # get an unlocked box
        for key in boxes[box]:  # check all keys inside the box
            if key < n and not unlocked[key]:  # if it unlocks a new box
                unlocked[key] = True  # unlock the box
                opened.append(key)  # add it to the list to be opened
                keys.update(boxes[key])  # update keys with keys from the new box

    return all(unlocked)  # check if all boxes are unlocked
