#!/usr/bin/env python3
"""
List all documents in Python
"""


def list_all(mongo_collection):
    """
    This function lists all documents in a collection using pymongo.

    Args:
        mongo_collection: The collection object.

    Returns:
        list: A list of all documents in the collection.
    """
    documents = mongo_collection.find()
    return list(documents)
