from collections import OrderedDict

class CacheBase:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        print(f"\n[DEBUG BASE] GET INICIO ({key}) - Estado actual:", self.cache)
        if key not in self.cache:
            print(f"[DEBUG BASE] GET ({key}) no encontrado")
            return -1
        else:
            self.cache.move_to_end(key)
            print(f"[DEBUG BASE] GET ({key}) encontrado. Nuevo orden:", self.cache)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        print(f"\n[DEBUG BASE] PUT INICIO ({key}, {value}) - Estado actual:", self.cache)
        if key in self.cache:
            print(f"[DEBUG BASE] Key {key} existe. Moviendo al final")
            self.cache.move_to_end(key)
        self.cache[key] = value
        print(f"[DEBUG BASE] Después de insertar {key}:", self.cache)
        if len(self.cache) > self.capacity:
            print("[DEBUG BASE] Capacidad excedida. Llamando a evict()")
            self.evict()

    def evict(self):
        raise NotImplementedError("Subclasses must implement this method")