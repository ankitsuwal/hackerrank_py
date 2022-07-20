# Count occurrences of an element in a list


Input = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
# Output : 3
# 10 appears three times in given list.

Input1 = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x1 = 22
# Output : 0


class CountOccurrences:
    def __init__(self, ele_list, x):
        self.ll = ele_list
        self.x = x

    def occurrences(self):
        if len(self.ll) == 0:
            return "List is empty.", self.ll
        # elif len(self.ll) == 1:
        #     return "List has only one element", self.ll
        else:
            count = {ele: self.ll.count(self.x) for ele in self.ll}
            return "Occurrence of {} is: ".format(self.x), \
                   count.get(self.x) if count.get(self.x) else 0


obj = CountOccurrences(Input1, x1)
msg, value = obj.occurrences()
print(msg, value)
