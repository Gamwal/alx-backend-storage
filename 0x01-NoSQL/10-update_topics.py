#!/usr/bin/env python3
"""
function that changes all topics of
a school document based on the name

"""


def update_topics(mongo_collection, name, topics):
    """
    function to updates documents in a collection

    Args:
        mongo_collection (pymongo collection object): db to query
        name (dict): dictionary of documents to insert in ollection

    Returns:
        result (pymongo collection object): updated mongodb collection
    """

    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
        )
    return result
