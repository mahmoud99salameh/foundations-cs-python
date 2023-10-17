def stats_measures(ls):
    #Calculate Mean
    mean=0
    for i in ls:
        mean+=i
    # return mean/len(ls)
    #Calculate Median
    median=float(0)
    for i in ls:
        if len(ls)%2==0:
            median=(ls[(len(ls)//2)]+ls[(len(ls)//2)-1])
        else:
            median=(ls[len(ls)//2])
        # return median
    #Calculate Mode
    