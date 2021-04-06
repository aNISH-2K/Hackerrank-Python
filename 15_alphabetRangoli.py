def print_rangoli(size):
    # your code goes here
    import string
    alpha = string.ascii_lowercase

    list = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        list.append((s[::-1]+s[1:]).center(4*n-3, "-"))

    print('\n'.join(list[:0:-1]+list))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
