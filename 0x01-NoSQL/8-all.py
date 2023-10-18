#!/usr/bin/env python3
"""
function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    function that lists all documents in a collection

    Args:
        mongo_collection (pymongo collection object): db to query

    Returns:
        list of documents in a collection
    """

    result = mongo_collection.find()
    return result
