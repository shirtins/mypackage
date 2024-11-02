def top_n(items, n):
    """Returns the top n items in an array, in desc order.

    Args:
        items (Array): list of array-like object
        n (int): num of items to return

    Return:
        array: top n items, in desc order

    Egs:
        >>> top_n([7,3,6,8,6], 4)
        [8,7,6,6]
    """
    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]: # if this item is bigger than the next item...
                items[j], items[j+1] = items[j+1], items[j] # swap the two!

    # get last two items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]