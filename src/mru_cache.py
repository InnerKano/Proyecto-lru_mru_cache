from .cache_base import CacheBase

class MRUCache(CacheBase):
    def __init__(self, capacity: int):
        super().__init__(capacity)
        self.access_counter = 0
        self.key_access = {}

    def get(self, key: int) -> int:
        val = super().get(key)
        if val != -1:
            self.key_access[key] = self.access_counter
            self.access_counter += 1
        return val

    def evict(self):
        # Encontrar clave con mayor access_counter
        mru_key = max(self.key_access, key=lambda k: self.key_access[k])
        del self.cache[mru_key]
        del self.key_access[mru_key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # Insertar al PRINCIPIO (no marca como reciente)
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
        else:
            self.cache.move_to_end(key)
        
        if len(self.cache) > self.capacity:
            self.evict()