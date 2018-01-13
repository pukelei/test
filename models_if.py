#!/usr/bin/env python
# coding=utf-8

cnt = 0
alex_age = 50
while cnt < 3:
    guess_age= int (input("plz input your age: "))
    if alex_age == guess_age:
        print 'You are lucky,you got it!'
        break
    elif alex_age > guess_age:
        print 'think bigger'
    else:
        print 'think  smaller'
    cnt +=1
else:
    print 'you input number is too much ,fuck off!'
