class LRUCache:
    """
    LRU Cache Implementation
    """
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.data = {}

    def get(self, key: str) -> str:
        return self.data.get(key)

    def set(self, key: str, value: str) -> None:
        self.data[key] = value

    def remove(self, key: str) -> None:
        self.data.pop(key)

    def to_string(self) -> str:
        res = ""
        for key, value in self.data.items():
            res += f"{key}\t|\t{value}\n"
        return res
