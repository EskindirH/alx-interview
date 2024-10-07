def can_unlock_all(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list of lists): List where each element contains keys for other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # number of boxes
    unlocked = [False] * n  # initially, all boxes are locked
    unlocked[0] = True  # the first box is already unlocked
    keys = set(boxes[0])  # initially, we have keys from the first box
    opened = [0]  # the first box is opened

    while opened:
        box = opened.pop()  # get an opened box
        for key in boxes[box]:  # check the keys inside
            if key < n and not unlocked[key]:  # if the key opens a new box
                unlocked[key] = True  # mark it as unlocked
                opened.append(key)  # add it to the list of boxes to open
                keys.update(boxes[key])  # add keys from the new box to our set

    return all(unlocked)  # check if all boxes are unlocked

