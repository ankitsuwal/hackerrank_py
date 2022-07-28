# 34, 51, 24, 76, 87
# output = {
#     '34,76': [],
#     '51,76': [],
#     '24,76': ['Economics'],
#     '76,87': ['Economics'],
#     '34,51': ['Anthropology'],
#     '24,34': ['Anthropology', 'Human Geography', 'Environmental Management'],
#     '34,87': [],
#     '24,51': ['Anthropology'],
#     '51,87': [],
#     '24,87': ['Economics'],
# }

input = [
    ["34", "Anthropology"],
    ["51", "Anthropology"],
    ["34", "Film & Television"],
    ["24", "Human Geography"],
    ["24", "Environmental Management"],
    ["24", "Anthropology"],
    ["76", "Economics"],
    ["34", "Human Geography"],
    ["24", "Economics"],
    ["51", "Anthropology"],
    ["34", "Environmental Management"],
    ["87", "Economics"],
]

# {"{'34', '51'}": ['Anthropology', 'Environmental Management'],
#  "{'24', '34'}": ['Economics', 'Environmental Management'],
#  "{'34', '76'}": ['Economics', 'Environmental Management'],
#  "{'34', '87'}": ['Economics', 'Environmental Management'],
#  "{'24', '51'}": ['Economics', 'Anthropology'],
#  "{'51', '76'}": ['Economics', 'Anthropology'],
#  "{'51', '87'}": ['Economics', 'Anthropology'],
#  "{'24', '76'}": ['Economics'],
#  "{'24', '87'}": ['Economics'],
#  "{'87', '76'}": ['Economics']}

from itertools import combinations

output = {}
set_ = set()


def combination(inp):
    res = list(combinations(inp, 2))
    print(">>>: ", res)
    for val in res:
        temp = set()
        set_ = set()
        for val1 in val:
            set_.add(val1[0])
            temp.add(val1[1])
        if len(set_) > 1:
            output[str(set_)] = list(temp)
    print("###: ", output)


combination(input)
# print("3333333333")