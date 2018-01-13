#!/usr/bin/env python
# coding=utf-8

def outter(Func):
    def wrapper(*args,**kwargs):
        print 'before'
        return Func()
        print 'after'
    return wrapper

@outter
def Function(agrs):
    #print 'in the Function:%s' %agrs
    agrs = 2 * agrs
    return agrs

Function(5)
