#!/usr/bin/python3
"""Module that solves the lockboxes problem."""


def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists, where each inner list represents
            the keys found inside the box at that index.

    Returns:
        bool: True if all boxes can be opened starting from box 0,
            False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
