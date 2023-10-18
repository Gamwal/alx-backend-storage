#!/usr/bin/env python3
"""
function that inserts a new document
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    function to insert a new document in a collection

    Args:
        mongo_collection (pymongo collection object): db to query
        kwargs (dict): dictionary of documents to insert in ollection

    Returns:
        result (pymongo collection object): updated mongodb collection
    """

    result = mongo_collection.insert(kwargs)
    return result
