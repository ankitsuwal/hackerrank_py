# Reversing a List in Python

class ReverseList:
    def __init__(self, ele_list):
        self.ll = ele_list

    def reverse(self):
        print(">>>: ", self.ll)
        if len(self.ll) == 0:
            return "list is empty.", self.ll
        else:
            return "Reversed list: ", self.ll[::-1]
            # self.ll.reverse()
            # return "Reversed list: ", self.ll
            # return "Reversed list: ", reversed(self.ll)


Input = [10, 11, 12, 13, 14, 15]
# Output : [15, 14, 13, 12, 11, 10]
obj = ReverseList(Input)
msg, val = obj.reverse()
print(msg, val)




