# LRU and MRU Cache Implementation

This project provides efficient implementations of the **Least Recently Used (LRU)** and **Most Recently Used (MRU)** caching algorithms in Python. These algorithms are commonly used in systems where caching is essential to optimize performance, such as databases, operating systems, and web servers.

## 📖 Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Testing](#testing)
- [Benchmarking](#benchmarking)
- [Contributing](#contributing)

## Introduction
Caching is a crucial technique in computer science to optimize the performance of systems by storing frequently accessed data in memory. This project implements two popular caching strategies:

- **LRU (Least Recently Used)**: Expels the least recently used item when the cache is full.
- **MRU (Most Recently Used)**: Expels the most recently used item when the cache is full.

## Installation
Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/lru_mru_cache.git
cd lru_mru_cache
```

No additional dependencies are required as the project uses Python's standard libraries.

## Usage
You can use the LRU and MRU cache implementations as follows:

```python
from src.lru_cache import LRUCache
from src.mru_cache import MRUCache

# Example usage of LRU Cache
lru_cache = LRUCache(capacity=3)
lru_cache.put(1, 'A')
lru_cache.put(2, 'B')
print(lru_cache.get(1))  # Output: 'A'

# Example usage of MRU Cache
mru_cache = MRUCache(capacity=3)
mru_cache.put(1, 'A')
mru_cache.put(2, 'B')
print(mru_cache.get(1))  # Output: 'A'
```

## Examples
The `main.py` file contains a demo of both LRU and MRU caches. Here's what it does:

```python
from src.lru_cache import LRUCache
from src.mru_cache import MRUCache

def demo_cache(cache):
    cache.put(1, 'A')
    cache.put(2, 'B')
    cache.put(3, 'C')
    cache.get(1)  # Makes 1 the most recently used
    cache.put(4, 'D')  # Evicts an item
    print(cache.cache)

if __name__ == "__main__":
    print("LRU Cache Demo:")
    lru_cache = LRUCache(capacity=3)
    demo_cache(lru_cache)

    print("\nMRU Cache Demo:")
    mru_cache = MRUCache(capacity=3)
    demo_cache(mru_cache)
```

### Expected Output

## Testing
Run the unit tests to ensure the implementations are correct:

```bash
python -m unittest discover tests
```

## Benchmarking
Compare the performance of LRU and MRU:

```bash
python benchmarks/benchmark.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request. 