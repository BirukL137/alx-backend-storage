#!/usr/bin/env python3
"""
Top students
"""


def top_students(mongo_collection):
    """
    This function returns all students sorted by average score.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        sorted average score with key.
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
