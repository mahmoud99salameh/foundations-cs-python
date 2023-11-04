def divisors(num):
    ls=[]
    for i in range(1,num+1):
        if(num%i==0):
            ls.append(i)   
    print(ls)
#################################
divisors(16)
divisors(10)

