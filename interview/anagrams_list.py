# An anagram of a string is another string that contains same characters, only the order of characters can be different.
# For example, “abcd” and “dabc”
# ------------------------------------------------
#
# Problem statement :
# -------------------->
# Given an array of words, print all anagrams together. For example, if the given array is
# {“cat”, “dog”, “tac”, “god”, “act”}, then output may be “cat tac act dog god”.
#
# An anagram of a string is another string that contains same characters, only the order of characters can be different.
# For example, “abcd” and “dabc”
#
# lst = [“cat”, “dog”, “tac”, “god”, “act”, "tac", "odg", "atc","tca", "owl", "lwo", "wol"]
#
# Case 1. Given an array of words, print all anagrams together for e.g.
# result = [[“cat”,“tac”,“act”, "tac", "atc","tca"], [“dog”, “god”,"odg"], ["owl", "lwo", "wol"]]
# Case 2. Also print number of time occurenace of anagram words along with position.
# for e.g. : result_1 = [{'conut':6, 'data':[“cat”,“tac”,“act”, "tac", "atc","tca"]},
# {'count':3, 'data':[“dog”, “god”,"odg"]}, {'count':3, 'data':["owl", "lwo", "wol"]}]


# TODO: Case 1 need to be completed
def anagaram_list(inp):
    result_dict = {}
    result_list = []
    for ele in inp:
        key = ''.join(sorted(ele))
        if key in result_dict.keys():
            result_dict[key].append(ele)
        else:
            result_dict[key] = []
            result_dict[key].append(ele)
    return result_dict


if __name__ == "__main__":
    lst = ["cat", "dog", "tac", "god", "act", "tac", "odg", "atc", "tca", "owl", "lwo", "wol"]
    result = anagaram_list(lst)
    res = []
    for key, val in result.items():
        res.append({"count": len(val), 'data': val})
    print(res)
