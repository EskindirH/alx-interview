#!/usr/bin/python3

"""
Determines if all the boxes can be unlocked given their
contents.
"""


def can_unlock_all(boxes):
    """
    Determines if all the boxes can be unlocked given their contents.

    Each box may contain keys to other boxes, and the goal is to check if 
    all boxes can be unlocked starting from the first one (which is unlocked by default).

    Args:
        boxes (list of lists): A list where each element represents a box containing 
        a list of keys (integers). Each key corresponds to another box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Example:
        >>> can_unlock_all([[1], [2], [3], [4], []])
        True

        >>> can_unlock_all([[1, 2], [0, 3], [4], [], [2]])
        True

        >>> can_unlock_all([[1], [2], [], [3]])
        False
    """
    # Total number of boxes
    n = len(boxes)

    # Keeps track of which boxes have been unlocked (initially all are locked except the first)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is always unlocked

    # Keys we initially have (from the first box)
    keys = set(boxes[0])

    # List of boxes that are available to be opened
    opened = [0]  # Start with the first box (already unlocked)

    while opened:
        # Pop the last opened box from the list
        box = opened.pop()

        # Iterate through the keys found in this box
        for key in boxes[box]:
            # If the key corresponds to a valid box that hasn't been unlocked yet
            if key < n and not unlocked[key]:
                unlocked[key] = True  # Unlock the box
                opened.append(key)  # Add it to the list of boxes to open
                keys.update(boxes[key])  # Add the new keys found in the opened box to our set

    # Return True if all boxes are unlocked, False otherwise
    return all(unlocked)
