from random import *
number=randint(1000,9999)

while True:
    user_number=int(input('inter a 4 digit number :'))
    while not(999<user_number<10000):
        user_number=int(input('inter a 4 digit number :'))
    if user_number==number:
        print('success and the chosen number is : ',number)
        break

    if user_number!=number:
        misplaced=0
        wellplaced=0
        for i in range(4):
            if str(user_number)[i]==str(number)[i]:
                 wellplaced=wellplaced+1
        for i in range(4):
            for j in range(4):
                    if str(user_number)[i]==str(number)[j] and i!=j:
                        misplaced=misplaced+1
                        break
        print("number of correct and misplaced digits : ",misplaced)
        print("number of wellplaced digits : ",wellplaced)
     
        
    