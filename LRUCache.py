import time
import heapq


class LRUCache:
    """
    LRU Cache Implementation based on Hashmap (Python dictionary) and Priority Queue (heapq)
    """
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.data = {}
        self.heap_queue = []

    def __add(self, key: str, value: str) -> None:
        cur_time_ms = round(time.time() * 1000)
        self.data[key] = value
        heapq.heappush(self.heap_queue, (cur_time_ms, key))

    def __update(self, key: str, value: str):
        cur_time_ms = round(time.time() * 1000)
        self.data[key] = value
        i = self.__get_queue_idx(key)
        self.heap_queue[i] = (cur_time_ms, key)
        heapq.heapify(self.heap_queue)
        return

    def __remove_oldest(self) -> None:
        oldest = heapq.heappop(self.heap_queue)
        del self.data[oldest[1]]

    def __get_queue_idx(self, key: str):
        for i, (_, k) in enumerate(self.heap_queue):
            if k == key:
                return i

    def get(self, key: str) -> str:
        return self.data.get(key)

    def set(self, key: str, value: str) -> None:
        if key in self.data:
            self.__update(key, value)
            return
        elif len(self.data) == self.capacity:
            self.__remove_oldest()
        self.__add(key, value)

    def remove(self, key: str) -> None:
        del self.data[key]
        i = self.__get_queue_idx(key)
        del self.heap_queue[i]
        heapq.heapify(self.heap_queue)
        return

    def to_string(self) -> str:
        res = "LRU Cache, the higher - the older. Columns: idx, key, value, priority\n"
        for i, (priority, key) in enumerate(self.heap_queue):
            idx = self.__get_queue_idx(key)
            res += f"|\t{idx}\t|\t{key}\t|\t{self.data[key]}\t|\t{priority}\t|\n"
        return res
