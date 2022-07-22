# Input: khokho
# Output:
# The entered string is symmetrical
# The entered string is not palindrome
#
# Input:amaama
# Output:
# The entered string is symmetrical
# The entered string is palindrome


class PalindromSymmetric:
    def __init__(self, inp):
        self.str = inp
        self.ll = len(inp)

    def check_symmetric(self):
        first = self.str[:self.ll//2]
        second = self.str[self.ll//2:]
        if first == second:
            print("The entered string is symmetrical")
        else:
            print("The entered string is not symmetrical")

    def check_palindrom(self):
        # rev = reversed(self.str)
        rev = self.str[::-1]
        print(rev, self.str)
        if rev == self.str:
            print("The entered string is palindrome.")
        else:
            print("The entered string is not palindrome.")


if __name__ == "__main__":
    inp = "amaama"
    obj = PalindromSymmetric(inp)
    obj.check_symmetric()
    obj.check_palindrom()