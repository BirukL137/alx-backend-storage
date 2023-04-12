#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""

import redis
import requests
import functools
from time import time
from typing import Callable

cache = {}


def cache_decorator(func: Callable) -> Callable:
    """
    cache decorator function
    """
    @functools.wraps(func)
    def wrapper(url: str) -> str:
        """
        This function will track how many times a particular URL
        was accessed in the key "count:{url}" and cache the result
        with an expiration time of 10 seconds.
        """
        
        if url in cache and time() - cache[url]['time'] < 10:
            cache[url]['count'] += 1
            return cache[url]['content']
        else:
            response = requests.get(url)
            content = response.content
            cache[url] = {'content': content, 'count': 1, 'time': time()}
            return content
        return wrapper

@cache_decorator
def get_page(url: str) -> str:
    """
    Returns response content 
    """

    response = requests.get(url)
    return response.content

