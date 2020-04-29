import os
import random

p = '/Users/kunalkushwaha/Desktop/FRIENDS'
os.chdir(p)

# print(os.listdir(p))
folder_name = random.choice(os.listdir(p))

folder_path = str(os.path.realpath(folder_name))
os.chdir(folder_path)
file_name = random.choice(os.listdir(folder_path))

print("Enjoy!")

# play to file

os.system("open " + file_name) # mac
# os.system("start" + filename) # windows
