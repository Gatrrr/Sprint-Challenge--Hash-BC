import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random

import json


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")
    proof = 1000
    last_hash = f'{last_proof}'.encode() 
    hash_obj = hashlib.sha256(last_hash).hexdigest()

    while valid_proof(hash_obj, proof) is False:
        proof += 1

    

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """

    guess = f'{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:6] == last_hash[-6:]



if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        try:
            data = r.json()
        except ValueError:
            print("Error:  Non-json response")
            print("Response returned:")
            print(r)
            break
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))

# ID is DavidDownes

# Searching for next proof
# Proof found: 64981891 in 87.1300423
# Invalid Proof or valid for block older than last 100 blocks.
# Searching for next proof
# Proof found: 21038768 in 29.963258300000007
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 10255451 in 14.43706259999999
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 32398345 in 46.299722599999996
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 1072605 in 1.4590108000000157
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 18794873 in 25.248077500000022
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 10584097 in 14.577987699999994
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 9940423 in 13.889842999999985
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 10867660 in 14.652564799999993
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 8812689 in 12.232185099999981
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 8285808 in 11.426327800000024
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 30182432 in 42.407738800000004
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 11806446 in 16.75477559999996
# Total coins mined: 1
# Searching for next proof
# Proof found: 16103160 in 22.096344199999976
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 16202243 in 22.598998400000028
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 990278 in 1.3644656999999825
# Total coins mined: 2
# Searching for next proof
# Proof found: 6798576 in 9.536824799999977
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 3030480 in 4.425761899999998
# Total coins mined: 3
# Searching for next proof
# Proof found: 17311155 in 24.070494999999994
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 35965621 in 52.72966609999992
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 13153898 in 18.17885179999996
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 14585222 in 19.83283629999994
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 20598002 in 29.948429200000078
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 15137113 in 22.966892299999927
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 24066097 in 36.470759000000044
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 9785962 in 12.966087000000016
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 63565055 in 89.05580970000005
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 31090206 in 44.440741799999955
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 3279519 in 4.5593589000000065
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 22986053 in 32.36765349999996
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 2387834 in 3.24094510000009
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 28918181 in 39.938198299999954
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 13405194 in 18.696650200000022
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 3717167 in 5.409520000000043
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 4697533 in 6.8828254000000015
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 3878360 in 5.725064400000065
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 7913591 in 11.486300100000108
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 3426694 in 4.983657300000004
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 15398984 in 22.0205904999998
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 6566458 in 9.060400899999877
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 11595014 in 16.54526439999995
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 25572407 in 36.64930319999985
# Invalid Proof or valid for block older than last 100 blocks.
# Searching for next proof
# Proof found: 11823900 in 16.61852470000008
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 21992132 in 29.553868400000056
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 33563 in 0.05033099999991464
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 5537636 in 7.812116799999785
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 5519520 in 7.225924599999871
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 29521003 in 39.0085775
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 6183701 in 9.496314499999926
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 7613568 in 11.423533800000087
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 28938531 in 43.19794060000004
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 10779769 in 14.471008199999915
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 8688668 in 12.318147099999806
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 21500654 in 28.77186740000002
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 9536383 in 13.803177000000005
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 15370384 in 22.26759170000014
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 24478212 in 36.24672090000013
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 24431198 in 35.26100600000018
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 7018025 in 9.733095999999932
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 1642740 in 2.3202243000000635
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 16066297 in 23.294060800000125
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 10264951 in 15.391923800000086
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 25320061 in 35.47995629999991
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 7119537 in 9.960742499999924
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 37154227 in 54.64971779999996
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 12686732 in 17.4537593
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 3860470 in 5.768295500000022
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 19109458 in 27.707685899999888
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 16836361 in 24.761858500000017
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 40882333 in 61.901595199999974
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 9411988 in 13.802051199999823
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 17673300 in 24.003149600000143
# Proof valid but already submitted.