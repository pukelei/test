#!/usr/bin/env python
# _*_ coding:utf8 _*_
#author:GXW
import sys
# 用户打印一级菜单
def menu():
    print("----------------------一级菜单-------------------")
    for index, key in enumerate(province_dic.keys(), 1):
        print index,key
        dic_key[str(index)] = key
    choose1 = raw_input("请选择一级菜单！输入q时，退出系统，输出b时，返回上一级目录: ")
    if choose1 == 'q':
        quit()
    elif choose1 == 'b':
        print("目录为一级目录，不能跳转，请重新选择: ")
        return
    elif dic_key.get(choose1, 0):
        menu2(dic_key[choose1])
    else:
        print("您的输入有误，请重新输入: ")

# 用户打印二级菜单
def menu2(choose1):
    print("----------------------二级菜单---------------------------")
    for index, key in enumerate(province_dic[choose1].keys(), 1):
        print index,key
        dic_key[str(index)] = key
    choose2 = input("请选择二级菜单！输入q时，退出系统，输出b时，返回上一级目录: ")
    if choose2 == 'q':
        quit()
    elif choose2 == 'b':
        menu()
    elif dic_key.get(choose2, 0):
        menu3(choose1, dic_key[choose2])
    else:
        print("您输入有误，请重新输入: ")
def menu3(choose1, choose2):
    print("-----------三级菜单---------------------------------------")
    for index, key in enumerate(province_dic[choose1][choose2], 1):
        print index,key
        dic_key[str(index)] = key
    choose3 = input("请选择三级菜单!输入q,退出系统，输入b，返回b时，返回上一级目录: ")
    if choose3 == 'q':
        print("")
        quit()
    elif choose3 == 'b':
            menu2(choose1)
    else:
        print("您输入有误，请重新输入: ")

province_dic = {
    "山东省":{
        "滨州市":{"惠民县","沾化县","无棣县","邹平县","阳信县"},
        "济南市":{"济阳县","商河县","平阴县","历下区","天桥区"},
        "菏泽市":{"定陶县","单县","巨野县","东明县","开发区"},
        "德州市":{"德城区","夏新县","平原县","陵县","乐陵县"}
    },
    "北京市":{
        "海淀区":{"航天科工","航天科技"},
        "朝阳区":{"巨人教育","老男孩教育"},
        "丰台区":{"下埔","岳各庄"}
    },
    "湖北省":{
        "武汉市":{"武昌区","江汉区","洪山区"},
        "荆州市":{"青山区","硚口区","江夏区"},
        "襄樊市":{"新洲区","南山区","北山区"}
    }
}
if __name__ == '__main__':
    dic_key = {}
    menu()
