import random
import time	

def random_text(rig,err):
    while True:
        for n in range(0,rig):
            line = random.choice(list(open('E:/ChatBox/Proposed/Dataset/Nega_r.txt')))
            ww.write(line)
        print("Done for 80 persent right Negative \n")
        for n in range(0,err):
            line = random.choice(list(open('E:/ChatBox/Proposed/Dataset/Nega_e.txt')))
            ww.write(line)
        print("Done for 20 persent error Negative \n")
        for n in range(0,rig):
            line = random.choice(list(open('E:/ChatBox/Proposed/Dataset/Posi_r.txt')))
            ww.write(line)
        print("Done for 80 persent right Positive \n")
        for n in range(0,err):
            line = random.choice(list(open('E:/ChatBox/Proposed/Dataset/Posi_e.txt')))
            ww.write(line)
        print("Done for 20 persent error Positive \n")
        break


tic = time.perf_counter() # Start Time

with open("E:/ChatBox/Proposed/Dataset/Total_sentence.txt","w") as ww:
    random_text(288,80)
    # random_text(535,201)
    # random_text(493,7)
    # random_text(1827,173)
    # random_text(2150,350)

toc = time.perf_counter() # End Time

print(f"Build finished in {(toc - tic)/60:0.0f} minutes {(toc - tic)%60:0.0f} seconds")
# For additional Precision
print(f"Build finished in {toc - tic:0.4f} seconds")