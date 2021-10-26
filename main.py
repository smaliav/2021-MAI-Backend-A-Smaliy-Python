import time

from LRUCache import LRUCache

initial_capacity = 3
add_latency_sec = 0.5

data = [
    ("Mike", "London"),
    ("Jenny", "Berlin"),
    ("Andrew", "Moscow"),
    ("John", "USA"),
    ("Alex", "Brno"),
    ("Teddy", "Brazil"),
    ("Alex", "Prague"),
    ("Kira", "Paris")
]

if __name__ == "__main__":
    lruCache = LRUCache(capacity=initial_capacity)

    for key, value in data:
        lruCache.set(key, value)
        time.sleep(add_latency_sec)

    print(lruCache.to_string())
