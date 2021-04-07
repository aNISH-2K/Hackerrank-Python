'''
Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints
1<=n<=100

Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0
n = 3

Sample Output 0
Weird
'''
n = int(input())
if n % 2 != 0:
    print("Weird")
else:
    if n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
