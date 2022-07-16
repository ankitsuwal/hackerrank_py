class LinearSearch:
    def __init__(self, arr, fin):
        self.arr = arr
        self.fin = fin

    def linear_search(self):
        left, right = 0, len(self.arr) - 1
        position = -1

        for val in range(0, right):

            if self.arr[left] == self.fin:
                position = left
                print("Element found in list at ", position + 1)
                break

            if self.arr[right] == self.fin:
                position = right
                print("Element found in list at ", position + 1)
                break
            left += 1
            right -= 1
        if position == -1:
            print("Element not found.")


# Driver code
arr = [1, 2, 10, 3, 4, 5, 11]
search_element = 3
obj = LinearSearch(arr, search_element)
obj.linear_search()
