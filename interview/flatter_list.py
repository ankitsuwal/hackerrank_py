# Input: [1, 2, [3, 4, [5, 6], 7], [[[8, 9], 10]], [11, [12, 13]]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]
#
# Input: [1, [2, 3]]
#
# Output: [1, 2, 3]

# from iteration_utilities import deepflatten
#
# l = [1, 2, [3, 4, [5, 6], 7], [[[8, 9], 10]], [11, [12, 13]]]
#
# ans = list(deepflatten(l))
# print("Answer: ", ans)
# ==============================================================================

output = []
def flatter_list(input_list):
    for ele in input_list:
        if type(ele) == list:
            flatter_list(ele)
        else:
            output.append(ele)


input_list = [1, 2, [3, 4, [5, 6], 7], [[[8, 9], 10]], [11, [12, 13]]]
flatter_list(input_list)
print(output)

