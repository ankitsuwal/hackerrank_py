# Input: arr = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170, x = 110
# Output: 6
# Explanation: Element x is present at index 6.
#
# Input: arr = [10, 20, 30, 40, 60, 110, 120, 130, 170], x = 175
# Output: -1
# Explanation: Element x is not present in arr[].


class BinarySearch:
    def __init__(self, arr, x):
        self.arr = arr
        self.x = x
        self.rr = len(arr) - 1
        self.ll = 0
        self.mid = 0

    def search_ele(self):
        if self.rr >= self.ll:
            self.mid = self.ll + (self.rr-self.ll) // 2
            if self.arr[self.mid] == self.x:
                return self.mid
            elif self.arr[self.mid] > self.x:
                self.rr = self.mid
                return self.search_ele()
            else:
                self.ll = self.mid + 1
                return self.search_ele()
        else:
            return -1


arr = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
x = 1101


obj = BinarySearch(arr, x)
result = obj.search_ele()

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not present in array")
