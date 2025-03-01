from src.lru_cache import LRUCache
from src.mru_cache import MRUCache

def demo_cache(cache):
    cache.put(1, 'A')
    cache.put(2, 'B')
    cache.put(3, 'C')
    cache.get(1)  # Hace que 1 sea el más reciente
    cache.put(4, 'D')  # Expulsa un elemento
    print(cache.cache)

if __name__ == "__main__":
    print("LRU Cache Demo:")
    lru_cache = LRUCache(capacity=3)
    demo_cache(lru_cache)

    print("\nMRU Cache Demo:")
    mru_cache = MRUCache(capacity=3)
    demo_cache(mru_cache) 