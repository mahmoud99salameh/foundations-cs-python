def even(ls):
    final_list=[]
    for i in ls:
        if i%2==0:
            final_list.append(i)
    print(final_list)
even([1,2,3,4,5,6,7,7,8])
