#!/usr/bin/python3

def canUnlockAll(boxes):
  """
  This function determines if all boxes can be opened given a list of lists representing keys in each box.

  Args:
      boxes: A list of lists, where each sub-list represents the keys found in a box.

  Returns:
      True if all boxes can be opened, False otherwise.
  """
  visited = set() 
  opened = [True] * len(boxes) 

  def dfs(box_index):
    """
    Recursive helper function to explore reachable boxes using keys.

    Args:
        box_index: The index of the current box being explored.
    """
    if box_index in visited:
      return

    visited.add(box_index)
    for key in boxes[box_index]:
      if not opened[key]:
        opened[key] = True
        dfs(key)

  dfs(0)  
  return all(opened)  
