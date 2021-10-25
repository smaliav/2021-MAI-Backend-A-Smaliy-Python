from LRUCache import LRUCache

data = {
    "Mike": "London",
    "Jenny": "Berlin",
    "Andrew": "Moscow",
    "John": "USA",
    "Jenny": "Glasgow"  # Overriding test
}

if __name__ == "__main__":
    lruCache = LRUCache(capacity=10)

    for key, value in data.items():
        lruCache.set(key, value)

    print(lruCache.to_string())
