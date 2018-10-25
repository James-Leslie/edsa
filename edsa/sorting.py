def bubble_sort(items, ascending=True):
    """
    Bubble sort algorithm O(n^2)

    1. Start at beginning of data set
    2. Compare first two elements
        if first > second: swap elements
    3. Compare next two elements, repeat until end of data set
    4. Repeat steps 1 - 3 until no more swaps -> list is sorted

    Args:
        items (array): list or array-type object containing numerical values.
        ascending (bool): if False, return list in descending order.

    Returns:
        array: sorted items.
    """

    changed = True
    # keep sorting until we make a full pass through the list without any changes
    while changed:
        changed = False
        for i in range(len(items)-1):
            if items[i] > items[i+1]:  # if this item is bigger than next item..
                items[i], items[i+1] = items[i+1], items[i]  # swap the two!
                changed = True

    if ascending:
        return items

    else:
        return items[::-1]


def merge(A, B):
    '''merges two sorted list into one sorted list'''

    new_list = []

    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list


def merge_sort(items):
    """
    Merge sort algorithm O(n.log(n))

    1. Find middle point to divide the array into two halves
    2. Call merge sort for first half
    3. Call merge sort for second half
    4. Merge the two halves sorted in step 2 and 3

    Args:
        items (array): list or array-type object containing numerical values.

    Returns:
        array: sorted items, in ascending order
    """

    len_i = len(items)
    if len_i <= 1:
        return items

    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    return merge(i1, i2)


def quick_sort(items, index=-1):
    """

    Quicksort algorithm O(n.log(n))

    The quick sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Args:
    items (array): list or array-type object containing numerical values.

    index (int, optional): index number at which to choose the split value
        default set to the last item in the input list

    Returns:
        array: sorted items, in ascending order
    """
    less = []
    equal = []
    greater = []

    if len(items) > 1:
        pivot = items[0]
        for x in items:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return quick_sort(less) + equal + quick_sort(greater)

    # You need to hande the part at the end of the recursion
    # - when you only have one element in your array, just return the array.
    else:
        return items
