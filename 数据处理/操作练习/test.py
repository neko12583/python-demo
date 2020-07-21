total_time = 0

def output_bridge_method(target_list):
    """
    打印过桥方法
    :param target_list: 过桥人物信息列表
    """
    print(target_list[0][0],target_list[1][0],"拿着灯过桥了")
    print(target_list[0][0],"带着的灯回来了")
    print(target_list[-1][0],target_list[-2][0],"拿着灯过桥了")
    print(target_list[1][0], "带着的灯回来了")


preson_str=input("格式：[['姓名',所用时间]...]\n请输入过桥人物信息：")
# [["小明",1],["弟弟",3],["爸爸",6],["妈妈",8],["爷爷",12]] 乱序

preson_list=list(eval(preson_str))
preson_list.sort(key=lambda item:item[1])
# [["小明",1],["弟弟",3],["爸爸",6],["妈妈",8],["爷爷",12]] 已排序

while 1:
    if len(preson_list)>=4:
        output_bridge_method(preson_list)
        total_time += preson_list[1][1]*2
        total_time += preson_list[0][1]
        total_time += preson_list[-1][1]
        del preson_list[-1],preson_list[-1]
    elif len(preson_list)==3:
        print(preson_list[0][0], preson_list[1][0], "拿着灯过桥了")
        total_time += preson_list[1][1]
        print(preson_list[0][0], "带着的灯回来了")
        total_time += preson_list[0][1]
        print(preson_list[0][0], preson_list[-1][0], "拿着灯过桥了")
        total_time += preson_list[-1][1]
        del preson_list[0],preson_list[0],preson_list[0],
    elif len(preson_list)==2:
        print(preson_list[0][0], preson_list[1][0], "拿着灯过桥了")
        total_time += preson_list[1][1]
        del preson_list[0], preson_list[0]
    else :
        break

print("所有人已过河,所用时间为：",total_time,"秒")



