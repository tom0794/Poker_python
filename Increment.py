import random

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


def random_indices(number_of_indices, collection_size):
    """
    Generates a list of random numbers between 0 and a given
    maximum, with no repeating numbers
    :param number_of_indices: Number of elements in the list
    to return
    :param collection_size: Size of collection random numbers
    are being created for
    :return: A list of random numbers between 0 and
    collection_size - 1, with no repeating numbers
    """
    available_indices = []
    for i in range(collection_size):
        available_indices.append(i)
    index_list = []
    for j in range(number_of_indices):
        index = random.randrange(0, len(available_indices) - 1)
        index_list.append(available_indices[index])
        available_indices.remove(available_indices[index])

    return index_list


