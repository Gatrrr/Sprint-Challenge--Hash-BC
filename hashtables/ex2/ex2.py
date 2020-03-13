#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)
    #initialize an empty list 
    flights = []
    #find the origin
    destination = hash_table_retrieve(hashtable, 'NONE')

    while destination != 'NONE':
        #loop inserting hashtable then stopping at 'NONE'
        flights.append(destination)
        destination = hash_table_retrieve(hashtable, destination)
        print(flights)
    return flights


