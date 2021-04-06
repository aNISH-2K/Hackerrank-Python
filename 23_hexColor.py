import re

n = int(input().strip())
inside = False
for _ in range(n):
    line = input()

    for i in line.split(' '):
        if i == "{":
            inside = True
            continue
        elif i == "}":
            inside = False
            continue
        elif inside:
            found = re.search(r'\#[0-9a-fA-F]{3,6}', i)
            if found:
                print(found.group(0))
