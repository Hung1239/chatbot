num_n = 0
num_p = 0
num_ne = 0


with open("E:/ChatBox/Proposed/Dataset/Total_sentence.txt","r") as readDocomment:
    with  open("E:/ChatBox/Proposed/Dataset/Computer_posi.txt","w") as writeDocomment:
        while True:
            for item in readDocomment:
                lst = [x for x in item]
                j = 0
                a1 = a2 = 0
                for i in lst:
                    j += 1
                    if i == '-':a1 = j
                    if i == '+':a2 = j
                    elif i == '#':
                        break
                if a1 < a2 :
                    num_p +=1
                    writeDocomment.write(item)
            break
        #writeDocomment.write("the number of positive sentence is : "+ str(num_p))



with open("E:/ChatBox/Proposed/Dataset/Total_sentence.txt","r") as readDocomment:
    with  open("E:/ChatBox/Proposed/Dataset/Computer_nega.txt","w") as writeDocomment:
        while True:
            for item in readDocomment:
                lst = [x for x in item]
                j = 0
                a1 = a2 = 0
                for i in lst:
                    j += 1
                    if i == '-':a1 = j
                    if i == '+':a2 = j
                    elif i == '#':
                        break
                if a1 > a2 :
                    num_n +=1
                    writeDocomment.write(item)
                    
            break
        #writeDocomment.write("the number of negative sentence is : "+ str(num_n))

# with open("E:/ChatBox/Proposed/Dataset/Test_sentence.txt","r") as readDocomment:
#     with  open("E:/ChatBox/Proposed/Dataset/Computer_neut.txt","w") as writeDocomment:
#         while True:
#             for item in readDocomment:
#                 lst = [x for x in item]
#                 for i in lst:
#                     if i == '-' or i == '+':
#                         break
#                     elif i == '#':
#                         num_ne +=1
#                         writeDocomment.write(item)
#                         break
#             break
        #writeDocomment.write("the number of neutral sentence is : "+ str(num_ne))

# with open("E:/ChatBox/Proposed/Dataset/TotalText.txt","r") as readDocomment:
#     with  open("E:/ChatBox/Proposed/Dataset/Computer.txt","w") as writeDocomment:
#         for item in readDocomment:
#             writeDocomment.write(item.split("##",1)[1])




print("done")