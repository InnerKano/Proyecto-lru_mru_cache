import unittest
from src.mru_cache import MRUCache

class TestMRUCache(unittest.TestCase):
    def test_mru_cache(self):
        cache = MRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)  # Accede a la clave 1, ahora es la más reciente
        cache.put(3, 3)  # Expulsa la clave 1 (la más reciente)
        self.assertEqual(cache.get(1), -1)  # La clave 1 ya no está
        self.assertEqual(cache.get(3), 3)  # La clave 3 está en la caché

if __name__ == '__main__':
    unittest.main() 