n = int(input())

phoneBook = {}
for i in range(n):
    key, value = input().split()
    phoneBook[key] = value

while 1:
    try:
        name = input()
    except:
        break

    if name in phoneBook:
        print(name + '=' + phoneBook[name])
    else:
        print('Not found')