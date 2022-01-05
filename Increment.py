def increment_indices(index_list, list_size):
    """
    Consumes a list of integers representing indices and the size
    of the list. Returns the next combination of indices if able.
    Returns false if index_list cannot be incremented
    :param index_list: List of integers (indices)
    :param list_size: Size of list
    :return: Updates index_list to the next possible combination if
    able, otherwise returns false
    """
    if len(index_list) == 0 or index_list[0] == list_size - len(index_list):
        return False
    else:
        final_position = list_size - 1
        for i in range(len(index_list) - 1, -1, -1):
            if index_list[i] < final_position:
                index_list[i] += 1
                if i != len(index_list) - 1:
                    for j in range(i + 1, len(index_list)):
                        index_list[j] = index_list[j - 1] + 1
                return index_list
            else:
                final_position -= 1
        return False
