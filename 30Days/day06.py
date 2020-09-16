n = int(input())
strs = [input() for i in range(n)]

for s in strs:
    even = ''
    odd = ''
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i]
        else:
            odd += s[i]
    print(even, odd)