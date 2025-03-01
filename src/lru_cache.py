from .cache_base import CacheBase

class LRUCache(CacheBase):
    def evict(self):
        self.cache.popitem(last=False)  # Expulsa el elemento menos reciente 