while True:
    number=input("enter the number please: ")
    if not number.isnumeric():
        print('please enter a valid integer')
    else:
        number = int(number)
        break
res = 0
for i in range(1,number):
    res +=i*number
print(res)
    




            