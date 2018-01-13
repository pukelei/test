#!/usr/bin/env python
# _*_ coding:utf8 _*_
#author:pukelei
import sys

user_lock_file="user_lock.txt"  # 用户所锁文件
user_file="user.txt"  # 用户文件
retry_limit = 3  # 输入的限制次数，若超过此次数，就将用户锁定
retry_count = 0   # 用户输入次数的计数器

while retry_limit >retry_count:
    user_name=raw_input("\033[31m请输入用户名：\033[0m")
    # 开始检测输入的用户名是否被锁
    lock_check = open(user_lock_file)  # 当输入用户名之后，打开锁文件判断用户是否以被锁。
    for line in lock_check.readlines():  # 循环锁文件，判断用户是否被锁
        if user_name in line:
            sys.exit("\033[31m %s is locked!\033[0m" %user_name)
    user_password=raw_input("\033[31m请输入密码:\033[0m")
    # 当用户不在锁文件中，输入密码，开始检测用户名和密码
    flag = False  # 用来记录是否用户名和密码是否匹配成功
    user_check = open(user_file,"rb")
    for line in user_check.readlines():
        user,password = str(line).split(" ");
        if user_name == user and user_password == password.strip("\n"):
            flag = True
            break
        else:
            flag = False
    user_check.close()
    if flag:
        print("Welcome to Oldboy IT System!I wait you too long!")
        break
    else:
        print("User not matched!")
        retry_count += 1
else:
    print("您输入用的次数已到，用户已被锁！")
    add_lock=open(user_lock_file,"w")
    add_lock.write(user_name)  # 当用户的输入次数大于规定的次数后，用户被添加到锁文件中
    add_lock.close()
