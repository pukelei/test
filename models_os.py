#!/usr/bin/env python
# coding=utf-8
print '蒲科磊'

import os


result = os.system("pwd")
print result
print os.popen("pwd").read().strip("\n")



import commands

print commands.getstatusoutput("pwd")[1]
