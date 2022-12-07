
import redis
from .cost_tracker import track_redis_hit

redis_client = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

# Please don't update these methods. These methods will be replaced at runtime.
def performRedisOps(operation, *args):
    """
    Please don't update this method. Use this method to get scoreboard from DB.
    Use Ex: performRedisOps("zrevrange", "some_random_key", "0", "-1")
    Parameters:
        operation (str): Redis command. ex: set, get, zadd, expire
        args: All other arguments, Required for Redis command.
    """
    track_redis_hit()
    return getattr(redis_client, operation)(*args)
