#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for zeroth in range(0, length):
        # the higher valued index should be placed first (0 index) and the smaller index should be placed in the first first (1 index) 
        # If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for `limit - weight`. If it does, then we've found the two items whose weights sum up to the `limit`!

        # If key doesn't exists, then insert and retry
        # If not None, we will return a tuple. 
        # The larger value will = zeroth, the smaller value will = first
        first = hash_table_retrieve(ht, (limit-weights[zeroth]))
        if first != None:
            # Your function will return an instance of an `Answer` tuple that has the following form:
            answer = (zeroth, first)
            print(answer)
            return answer
        # If first 
        else:
            hash_table_insert(ht, weights[zeroth], zeroth)
    # If such a pair doesn’t exist for the given inputs, your function should return `None`.
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
