#!/usr/bin/env python3
'''Task 8module'''


def list_all(mongo_collection):
    '''Lists documents in a collection'''
    return [doc for doc in mongo_collection.find()]
