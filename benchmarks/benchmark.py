import timeit
from src.lru_cache import LRUCache
from src.mru_cache import MRUCache

def benchmark_cache(cache_class, capacity, operations):
    cache = cache_class(capacity)
    for op in operations:
        if op[0] == 'put':
            cache.put(op[1], op[2])
        elif op[0] == 'get':
            cache.get(op[1])

if __name__ == "__main__":
    operations = [('put', i, i) for i in range(1000)] + [('get', i) for i in range(1000)]
    
    lru_time = timeit.timeit(lambda: benchmark_cache(LRUCache, 100, operations), number=100)
    mru_time = timeit.timeit(lambda: benchmark_cache(MRUCache, 100, operations), number=100)
    
    print(f"LRU Cache Time: {lru_time}")
    print(f"MRU Cache Time: {mru_time}") 