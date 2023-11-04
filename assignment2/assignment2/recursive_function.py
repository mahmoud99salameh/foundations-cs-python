print(" 1. Count Digits \n 2.Find Max \n 3.1. Count tags \n 3.2. Count Normalized Columns \n 4. Exit \n ---------------------------" )
############################################################
input0=int(input("Enter a choice: "))
############################################################
def checkifint(input1):
    while True:
        if not input1.isnumeric():
            print('please enter a valid integer')
        else:
            input1 = int(input1)
            break
############################################################   
def count(input1):
    input1 = str(input1)
    # Check if the input is a single digit number
    if len(input1) == 1:
        return 1
    else:
        # If not, call the function again with the length of the remaining input
        return 1 + count(len(input1[1:]))
#############################################################
def findmax(ls):
    max=0
    for i in range(len(ls)):
        if str(ls[i])>str(max):
            max=ls[i]
            findmax(ls[1:])
    return max
#############################################################
if input0==1:
    input1 = input("Enter a input: ")
    # Print the result of the count function
    print(count(input1))
elif input0==2:
    input1 = input("Enter a list: ")
    print(findmax(input1))
else:
    print("Not in choices")
#############################################################
