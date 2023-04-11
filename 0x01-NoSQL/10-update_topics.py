#!/usr/bin/env python3
"""
Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: The pymongo collection.
        name (str): The school name to update.
        topics (list of str): The list of topics in the school.

    Returns:
        The updated arguments
    """
    new_name = {"name": name}
    new_topic = {"$set": {"topics": topics}}
    return mongo_collection.update_many(new_name, new_topic)
