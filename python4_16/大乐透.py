# 1-33 5个
#1-16  2个
#定义7位数的数组
arr_list=[]
arr_lists=[]
# 定义红球
list1=[i for i in range(1,36)]
#定义蓝球
list2=[i for i in range(1,13)]
print(list1,list2)
for tmp1 in list1:
    arr_list=[]
    arr_list[0]=tmp1
    for tmp2 in list1:
        arr_list[1]=tmp2
        for tmp3 in list1:
            arr_list[2]=tmp3
            for tmp4 in list1:
                arr_list[3]=tmp4
                for tmp5 in list1:
                    arr_list[4]=tmp5
                    for tmp6 in list1:
                        arr_list[5]=tmp6
                        for tmp7 in list1:
                            arr_list[6]=tmp7
                            arr_lists.append(arr_list)
                            print(arr_list)