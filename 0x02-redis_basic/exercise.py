#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import redis
from uuid import uuid4


class Cache:
    """
    A class to represent a cache.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the cache object.
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str) -> str:
        """
        This function Store input data in Redis using
        a random key generated by uuid4().

        Args:
            data (str): The data to be stored in Redis.

        Returns:
            str: The random key generated by uuid4().
        """
        
        key = str(uuid4())
        self._redis.set(key, data)
        return key
