from .cache_base import CacheBase

class MRUCache(CacheBase):
    def __init__(self, capacity: int):
        super().__init__(capacity)
        self.order = []  # Lista para mantener el orden de uso
        print(f"Cache creada con capacidad: {capacity}")

    def get(self, key: int) -> int:
        if key not in self.cache:
            print(f"Clave {key} no encontrada en la caché")
            return -1
        else:
            # Mueve la clave al final de la lista (más reciente)
            print(f"Accediendo a la clave {key}. Orden antes: {self.order}")
            self.order.remove(key)
            self.order.append(key)
            print(f"Orden después: {self.order}")
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Si la clave ya existe, actualiza su valor y la mueve al final
            print(f"Clave {key} ya existe. Orden antes: {self.order}")
            self.order.remove(key)
            self.order.append(key)
            print(f"Orden después: {self.order}")
        else:
            print(f"Insertando nueva clave {key}. Orden antes: {self.order}")
            self.order.append(key)
            print(f"Orden después: {self.order}")
        self.cache[key] = value
        print(f"Cache después de insertar {key}: {self.cache}")
        if len(self.cache) > self.capacity:
            print("La caché está llena. Expulsando el elemento más reciente...")
            self.evict()

    def evict(self):
        # Expulsa el elemento más reciente (el último en la lista)
        mru_key = self.order.pop()
        del self.cache[mru_key]
        print(f"Clave expulsada: {mru_key}")
        print(f"Cache después de expulsar: {self.cache}")
        print(f"Orden después de expulsar: {self.order}")