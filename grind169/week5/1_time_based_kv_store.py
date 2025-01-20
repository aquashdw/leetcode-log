class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map.keys():
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map.keys():
            return ""

        values = self.map.get(key)
        n = len(values)
        front = 0
        back = n - 1
        result = ""
        while front <= back:
            mid = (front + back) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]
                front = mid + 1
            else:
                back = mid - 1

        return result


if __name__ == '__main__':
    time_map = TimeMap()
    print("case 0")
    print(time_map.set("foo", "bar", 2))
    print(time_map.get("foo", 0))

    time_map = TimeMap()
    print("case 1")
    print(time_map.set("foo", "bar", 1))
    print(time_map.get("foo", 1))
    print(time_map.get("foo", 3))
    print(time_map.set("foo", "bar2", 4))
    print(time_map.get("foo", 4))
    print(time_map.get("foo", 5))

    time_map = TimeMap()
    print("case 2")
    print(time_map.set("love", "high", 10))
    print(time_map.set("love", "low", 20))
    print(time_map.get("love", 5))
    print(time_map.get("love", 10))
    print(time_map.get("love", 15))
    print(time_map.get("love", 20))
    print(time_map.get("love", 25))

    time_map = TimeMap()
    print("case 3")
    print(time_map.set("foo", "bar", 1))
    print(time_map.set("foo", "toilet", 5))
    print(time_map.set("foo", "bucket", 10))
    print(time_map.set("foo", "bar2", 20))
    print(time_map.get("foo", 15))
