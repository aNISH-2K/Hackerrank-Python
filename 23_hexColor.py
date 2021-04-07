'''
CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have  or  digits.
■ Each digit is in the range of  to . ( and ).
■  letters can be lower case. ( and  are also valid digits).

Examples

Valid Hex Color Codes
#FFF 
#025 
#F0A1FB 

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff
You are given  lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

CSS Code Pattern

Selector
{
	Property: Value;
}
Input Format

The first line contains , the number of code lines.
The next  lines contains CSS Codes.

Constraints



Output Format

Output the color codes with '#' symbols on separate lines.

Sample Input

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
'''
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
