#!/usr/bin/env python3
"""
function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that lists all schools having a specific topic

    Args:
        mongo_collection (pymongo collection object): db to query
        topic (string): specified topic to search

    Returns:
        result (pymongo collection object): results from search
    
    
    """
    result = mongo_collection.find({'topics': topic})
    return result
