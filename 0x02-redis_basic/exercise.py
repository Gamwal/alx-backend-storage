"""
Class object to write strings to Redis
"""

import redis
import uuid


class Cache:
    """
    A class for storing and retrieving strings in Redis.

    This class provides methods for storing strings in Redis
    and retrieving them later using unique identifiers.

    Attributes:
        _redis (redis.Redis): A connection to the Redis database

    """

    def __init__(self) -> None:
        """
        Initializes a new Cache instance and connects to a Redis database.

        The Redis database is flushed (all data is deleted)
        upon initialization.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """
        Stores a string in Redis and returns a unique identifier for retrieval.

        Args:
            data (str): The string data to be stored in Redis.

        Returns:
            str: A unique identifier (UUID) that can be
            used to retrieve the data later.
        """
        id = str(uuid.uuid4())
        self._redis.mset({id: data})
        return id
