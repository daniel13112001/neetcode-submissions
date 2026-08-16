class TimeMap:

    def __init__(self):
        self.keys = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.keys:
            self.keys[key] = [[timestamp], [value]]
        else:
            self.keys[key][0].append(timestamp)
            self.keys[key][1].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        print(self.keys)
        if not self.keys:
            return ""
        if key not in self.keys:
            return ""
        for idx in range(len(self.keys[key][0])-1, -1, -1):
            if self.keys[key][0][idx] <= timestamp:
                return self.keys[key][1][idx]
        
        return ""