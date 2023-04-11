#!/usr/bin/env python3
"""
Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
    This function returns the list of school having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The string to be searched.

    Returns:
        lists of school having a specific topic.
    """
    lists = [val for val in mongo_collection.find({"topics": topic})]
    return lists
