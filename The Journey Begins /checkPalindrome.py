def checkPalindrome(inputString):
    # use [::-1], quick to revser string
    reverse_str = inputString[::-1]
    print(reverse_str)
    # the output is boolean type
    return (reverse_str == inputString)
