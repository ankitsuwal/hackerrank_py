# Input : str =" geeks quiz practice code"
# Output : str = code practice quiz geeks
# Input : str = "my name is laxmi"
# output : str= laxmi is name my

def reverse_words(inp):
    print(' '.join(inp.split()[::-1]))


if __name__ == "__main__":
    inp = "geeks quiz practice code"
    inp1 = "Ankit is name my"
    reverse_words(inp1)
