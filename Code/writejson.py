from distutils.file_util import write_file
import json

# edit text file to reading easier:
# with open("E:/ChatBox/Proposed/Dataset/negative_text.txt","r") as readfile:
#     with open("E:/ChatBox/Proposed/Dataset/negative.txt","w") as writefile:
#         for item in readfile:
#             writefile.write('"'+ item.rstrip() + '",')

# with open("E:/ChatBox/Proposed/Dataset/positive_text.txt","r") as readfile:
#     with open("E:/ChatBox/Proposed/Dataset/positive.txt","w") as writefile:
#         for item in readfile:
#             writefile.write('"'+ item.rstrip() + '",')

# Write list from text file 
negative = open("E:/ChatBox/Proposed/Dataset/negative_text.txt","r").read().splitlines()
positive = open("E:/ChatBox/Proposed/Dataset/positive_text.txt","r").read().splitlines()

# Data to be written
# Write_file = {"intents":[ 
#         {"tag":"negative",
#          "patterns":negative,
#          "responses":[" this is negative"],
#          "context":[""]
#         },
#         {"tag":"positive",
#          "patterns":positive,
#          "responses":[" this is positive"],
#          "context":[""]
#         }
#     ]
# }

# Writing to json file
with open("E:/ChatBox/Proposed/intents004.json", "w") as outfile:
    outfile.write('{"intents":[{"tag":"negative","patterns":[')
    for item_neg in negative:
        outfile.write('"' + item_neg.rstrip() + '",\n')
    outfile.write('"0000"],"responses":[" this is negative"],"context":[""]},')
    outfile.write('{"tag":"positive","patterns":[')
    for item_pos in positive:
        outfile.write('"' + item_pos.rstrip()  + '",\n')
    outfile.write('"1111"],"responses":[" this is positive"],"context":[""]}]}')


# my_string="hello python world , ## i'm a beginner"
# print(my_string.split("##",1)[1])