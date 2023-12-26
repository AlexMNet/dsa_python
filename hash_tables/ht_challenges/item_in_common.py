"""
 Item In Common
 Write a function item_in_common(list1, list2)
 that takes two lists as input and returns
 True if there is at least one common item
 between the two lists, False otherwise
    EXPECTED OUTPUT:
    ----------------
    True

"""

list1 = [1, 3, 5]
list2 = [2, 4, 5]


def item_in_common(list1, list2):
    items = {}

    for item in list1:
        items[item] = True

    for item in list2:
        if item in items:
            return True

    return False


print(item_in_common(list1, list2))
