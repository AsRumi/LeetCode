"""
981. Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
Implement the TimeMap class:
* TimeMap() Initializes the object of the data structure.
* void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
* String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
"""

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.main_dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.main_dictionary[key].append((timestamp, value))
        return None

    def get(self, key: str, timestamp: int) -> str:
        targetList = self.main_dictionary[key]
        if not targetList:
            return ""
        low = 0
        high = len(targetList) - 1
        result = ""
        while low <= high:
            middle = (low + high) // 2
            if targetList[middle][0] <= timestamp:
                result = targetList[middle][1]
                low = middle + 1
            else:
                high = middle - 1
        return result
        
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
# timeMap.get("foo", 1)
# timeMap.get("foo", 3)
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 3))
# timeMap.get("foo", 5)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)