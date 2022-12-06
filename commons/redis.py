
import redis
from .cost_tracker import track_redis_hit

redis_client = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

# Please don't update these methods. These methods will be replaced at runtime.
def performRedisOps(operation, *args):
    track_redis_hit()
    return getattr(redis_client, operation)(*args)
