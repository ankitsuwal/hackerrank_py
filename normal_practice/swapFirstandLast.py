# Python program to interchange first and last elements in a list

class SwapFirstAndLast:
    def __init__(self, ele_list):
        self.ele_lst = ele_list

    def swap_ele(self):
        if self.ele_lst == []:
            return "List is empty.", self.ele_lst
        elif len(self.ele_lst) == 1:
            return "List has only one element", self.ele_lst
        else:
            self.ele_lst[0], self.ele_lst[len(self.ele_lst) - 1] = self.ele_lst[len(self.ele_lst) - 1], self.ele_lst[0]
            return "Swapped list: ", self.ele_lst


input = [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
obj_swap = SwapFirstAndLast(input)
strr, val = obj_swap.swap_ele()
print(strr, val)
