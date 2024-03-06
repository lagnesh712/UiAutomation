import os
import shutil


day_four=os.listdir("./../secrets/practice_programs")
main=os.listdir("./practice_programs")
print(day_four)
print(main)
src="/home/lagnesh/secrets/practice_programs/"
dst="/home/lagnesh/interview_practice/practice_programs/"
for i in day_four:
    if os.path.isdir(src+i):
        pass
    elif i not in main:
        shutil.copyfile(src+i,dst+i)