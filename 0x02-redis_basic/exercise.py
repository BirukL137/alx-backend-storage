#!/usr/bin/env python3
"""
Task 0. Writing strings to Redis
Task 1. Reading from Redis and recovering original type
Task 2. Incrementing values
Task 3. Storing lists
Task 4. Retrieving lists
"""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """
    Implement a system to count how many times methods of the
    Cache class are called.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A decorator that takes a single method Callable argument
        and returns a Callable
        """

        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Add it's input parameters to one list in redis, and store its
    output into another list, everytime the original function called.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A decorator to store the history of inputs and outputs for
        a particular function.
        """

        inputs_k = f"{method.__qualname__}:inputs"
        outputs_k = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputs_k, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_k, output)
        return output
    return wrapper


def replay(fn: Callable):
    """
    Displays the history of calls of a particular function.
    """

    inputs_k = f"{fn.__qualname__}:inputs"
    outputs_k = f"{fn.__qualname__}:outputs"
    inputs = cache._redis.lrange(inputs_k, 0, -1)
    outputs = cache._redis.lrange(outputs_k, 0, -1)
    print(f"{fn._qualname__} was called {len(inputs)} times: ")
    for i, out in zip(inputs, outputs):
        print(f"{fn.qualname__}(*{i.decode()}) -> {out.decode()}")


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

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[str]:
        """
        Retrieve data from Redis using the specified key.

        Args:
            key (str): The key used to retrieve data from Redis.
            fn (Optional[Callable]): An optional callable used to convert
            the data back to the desired format.

        Returns:
            Optional[str]: The data retrieved from Redis as a string.
        """

        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve string data from Redis using the specified key.

        Args:
            key (str): The key used to retrieve string data from Redis.

        Returns:
            Optional[str]: The string data retrieved from Redis.
        """

        return self.get(key)

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve integer data from Redis using the specified key.

        Args:
            key (str): The key used to retrieve integer data from Redis.

        Returns:
            Optional[int]: The integer data retrieved from Redis.
        """

        return self.get(key, fn=int)
