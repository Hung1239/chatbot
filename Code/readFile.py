import pandas as pd
import pickle as pkl
unpickled_df = pd.read_pickle("E:/ChatBox/Proposed/Dataset/words.pkl")
print(unpickled_df)
print("---------------------")
unpickled_df = pd.read_pickle("E:/ChatBox/Proposed/Dataset/classes.pkl")
print(unpickled_df)
with open("E:/ChatBox/Proposed/Dataset/words.pkl", "rb") as f:
    object = pkl.load(f)
    
df = pd.DataFrame(object)
df.to_csv(r'E:/ChatBox/Proposed/Dataset/words.csv')
with open("E:/ChatBox/Proposed/Dataset/classes.pkl", "rb") as f:
    object = pkl.load(f)
    
df = pd.DataFrame(object)
df.to_csv(r'E:/ChatBox/Proposed/Dataset/classes.csv')

# with open("E:/ChatBox/Proposed/Computer.txt","r") as readdocoment:
#     for item in readdocoment:
#         print(item.split("##",1)[1])

# with open("E:/ChatBox/Proposed/TotalText.txt","r") as readText:
    # with open("E:/ChatBox/Proposed/Computer.txt","w") as writeText:
        # for item in readText:
            # print(item.split("##",1)[1])