ch= "*"
iEnd = 1

'''
By default python’s print() function ends with a newline. 
Python’s print() function comes with a parameter called ‘end’. 
By default, the value of this parameter is ‘\n’, i.e. the new line character. 
You can end a print statement with any character/string using this parameter.
'''
for istart in range(4):
    while iEnd<5:
       print(ch, end =" ")
       iEnd = iEnd + 1
    iEnd = 1
    print(" ")

