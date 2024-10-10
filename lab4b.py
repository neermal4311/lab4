#!/usr/bin/env python3

def join_lists(l1, l2):
    """
    join_lists returns a list that contains every unique value from both l1 and l2.
    The order of elements is determined by the order of insertion in the union of both sets.
    
    Args:
        l1 (list): First list of integers.
        l2 (list): Second list of integers.
    
    Returns:
        list: Combined list with unique elements.
    """
    # Perform set union and convert back to list
    return list(set(l1) | set(l2))

def match_lists(l1, l2):
    """
    match_lists returns a list that contains all values found in both l1 and l2.
    
    Args:
        l1 (list): First list of integers.
        l2 (list): Second list of integers.
    
    Returns:
        list: List of common elements.
    """
    # Perform set intersection and convert back to list
    return list(set(l1) & set(l2))

def diff_lists(l1, l2):
    """
    diff_lists returns a list that contains all values which are not shared between l1 and l2.
    
    Args:
        l1 (list): First list of integers.
        l2 (list): Second list of integers.
    
    Returns:
        list: List of symmetric difference elements.
    """
    # Perform set symmetric difference and convert back to list
    return list(set(l1) ^ set(l2))

if __name__ == '__main__':
    list1 = list(range(1, 10))   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = list(range(5, 15))   # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))
