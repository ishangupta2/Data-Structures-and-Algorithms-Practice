class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        arr = self.map[key]
        L, R = 0, len(arr)-1
        small = ""
        while L<=R:
            mid = (L+R)//2
            if arr[mid][1] < timestamp:
                small = arr[mid][0]
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] > timestamp:
                R = mid-1
            else:
                L = mid+1
        return small

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)