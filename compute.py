#!/usr/bin/env python
def operator(y,x,op):
    if op == "+": y+=x
    elif op == "-": y-=x
    elif op == "*": y*=x
    elif op == "/": 
        z = float(y)
        y = z
        y/=x    
    return y

def compute(thestring):
    string1 = thestring.replace(" ","")
    answer = float(string1[0])
    op = string1[1]
    for i in range(2,len(string1)):
        j = i%2
        if j == 0:
            answer = operator(answer,float(string1[i]),op)
        elif j ==1:
            op = string1[i]
    return answer
